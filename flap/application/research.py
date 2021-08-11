from flask import request, redirect, url_for, render_template, session, Response
from flap import app

#APIとその描画に関する機能を実装
from flap.application.scripts import getAppearance, getComSource, createTable, robot, translate
from data import arrangeData
import os

@app.route('/edit', methods=['GET', 'POST'])
#作成中のページソースを貼り付け
def edit():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        with open('flap/application/trush/article.html', 'w') as f:
            f.writelines(request.form['article'])

        return redirect(url_for('inside'))


    return render_template('article.html')


#記事か競合かを選ぶリンクだけのフォーム
@app.route('/alter', methods=['GET', 'POST'])
def quux():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    #本当はこの時点で処理を開始しているかのテストをしたい

    return render_template('quux.html')


#APIの起動と翻訳したtsvファイルの読み取りと表示
@app.route('/competitors', methods=['GET'])
def competitors():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    insAppearance = getAppearance.GetLung('ans.html')
    #[query, [suggests]]
    l = insAppearance.openMemo()

    if os.path.exists(f'data/results/{l[0]}.tsv') == False:

        #APIを起動
        robot.getSearchResponse(l[0])

        #jsonを翻訳
        translate.makeSearchResults(l[0])

    #l[0]を引数にtsvを翻訳
    insArrangedata = arrangeData.GetCompetitors(l[0])
    arrangedL = insArrangedata.openTSV()
    #colsは[[一行目のヘッダ], [日付, 順位, domain, title, url. discription]...]
    #titleが3, urlが4

    materialTable = []

    for i,sarpE in enumerate(arrangedL):

        if i == 0:
            continue

        compeTitle = sarpE[3]
        compeURL = sarpE[4]

        #urlにリクエスト
        insComSource = getComSource.GetPage(compeURL, 'tempoCopy')
        insComSource.reqHTML()

        insComSourceInside = getComSource.FindHead('tempoCopy')
        insComSourceInside.createCounted(insComSourceInside.sepaArtiOpen(insComSourceInside.findH2()))

        resultL =  insAppearance.countWords(insAppearance.arrangeFile(), l[1], insComSourceInside.findH2())

        resultL.insert(0, f'<a href="{sarpE[4]}">{sarpE[3]}</a>')
        resultL.insert(0, i)

        materialTable.append(resultL)
        #それぞれの辞書を格納した結果を返し、html整形の引数にする

    createTable.create(materialTable)
    #言語処理,結果をhtmlに記述

    return render_template('table.html')



@app.route('/foo')
def foo():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    pass