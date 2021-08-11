from flask import request, redirect, url_for, render_template, session, Response
from flap import app

from flap.application.scripts import getComSource, getAppearance, arrangeInside, drawTable

@app.route('/arti')
def inside():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    #trushのarticle.htmlを読み込んで、記事の内容を返す。
    #getAppearanceをちょっと書き換えて実装 

    with open('flap/application/trush/article.html') as f:
        l = [line for line in f.readlines()]
    #ひどいからきちんとpathは整理したい
    with open('flap/application/scripts/tempo/insideArticle.html', 'w') as f:
        for line in l:
            f.writelines(line)        


    inst = getComSource.FindHead('insideArticle')
    htmlDraft = inst.sepaArtiOpen(inst.findH2())

    with open('flap/application/scripts/tempo/insideDraft.html', 'w') as f:
        for line in htmlDraft:
            f.writelines(line)

    #割と書き換え部分多いから整理した方が得策

    insta = getAppearance.GetLung('insideDraft.html')

    lis = insta.openMemo()#memoを開いた結果のタプル(query, list[suggests])

    resultL = insta.countWords(insta.arrangeFile(), lis[1], inst.findH2())
    #[h2タイトルの文字列, suggestsの辞書]と交互に格納されたリスト

    taiyaki = arrangeInside.AdjustArti('flap/application/scripts/tempo/memo.txt' ,'flap/application/scripts/tempo/insideDraft.html')

    taiyaki.adjustFile()
    resultFook = taiyaki.findFook(lis[1])#フックの計測結果を格納した辞書

    #htmlファイルの形成

    imagawa = drawTable.DrawTable(resultFook, resultL, 'flap/templates/hoge.html')
    imagawa.drawFook()


    return render_template('hoge.html')

@app.route('/test')
def test():
    return render_template('table.html')