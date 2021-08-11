#未調整

import requests, MeCab
from bs4 import BeautifulSoup

#URLとファイル名を引数にして見出しごとのKW登場回数を数えるクラス
class GetPage():

    def __init__(self, URL, fileName):
        
        headersDic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

        self.req = requests.get(URL, headers=headersDic)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')
        self.fileName = fileName

    def reqHTML(self):

        with open(f'flap/application/scripts/tempo/{self.fileName}.html', 'w') as f:
            f.writelines(str(self.soup))
        pass

#htmlファイルに目印タグを設置するクラス
class FindHead():

    def __init__(self, fileName):
        self.fileName = fileName

    def findH2(self):

        soup = BeautifulSoup(open(f'flap/application/scripts/tempo/{self.fileName}.html'), 'html.parser')
        
        #指定タグの内容をリストに入れて返す。.textでテキスト部分を抽出。
        h2Titles = soup.findAll('h2')
        return h2Titles

    #findH2の戻り値を検索して、imaginationTagで目印をつけ、見出し2毎にhtmlファイルを分ける
    #汎用性が怪しいので疲れてない時に整理する
    def sepaArtiOpen(self, h2Titles):

        with open(f'flap/application/scripts/tempo/{self.fileName}.html') as f:
            lines = f.readlines()

        for num in range(len(h2Titles)):

            #スープで見つけたタグが格納されている場所を見つけて、文字列として見つけたh2タグの直前に目印を設置
            for i, e in enumerate(lines):
                #h2Titlesの要素数だけ繰り返す

                if str(f'{h2Titles[num]}').replace('\n', '') in e:
                        
                    #h2がある文字列で登場箇所は何文字目か
                    positionNum = lines[i].find(f'{h2Titles[num]}')

                    #条件分岐で初めの見出し以外には閉じタグも追加
                    if num != 0:
                        lines[i] = lines[i][:positionNum] + f'</head_posi_{num-1}><head_posi_{num}>' + lines[i][positionNum:]
                    if num == 0:
                        lines[i] = lines[i][:positionNum] + f'<head_posi_{num}>' + lines[i][positionNum:]

                    break

                else:

                    for number in range(6):

                        if number == 0:
                            continue

                        if i < len(lines) - number:

                            base = str(f'{h2Titles[num]}').replace('\n', '')
                            maybe = e

                            if number == 1 and 'h2' in maybe:
                                maybe = maybe + lines[i + 1]
                                maybe = maybe.replace('\n', '')

                            elif number == 2 and 'h2' in maybe:
                                maybe = maybe + lines[i + 1] + lines[i + 2]
                                maybe = maybe.replace('\n', '')

                            elif number == 3 and 'h2' in maybe:
                                maybe = maybe + lines[i + 1] + lines[i + 2] + lines[i + 3]
                                maybe = maybe.replace('\n', '')

                            elif number == 4 and 'h2' in maybe:
                                maybe = maybe + lines[i + 1] + lines[i + 2] + lines[i + 3] + lines[i + 4]
                                maybe = maybe.replace('\n', '')

                            elif number == 5 and 'h2' in maybe:
                                maybe = maybe + lines[i + 1] + lines[i + 2] + lines[i + 3] + lines[i + 4] + lines[i + 5]
                                maybe = maybe.replace('\n', '')

                            if base in maybe:

                                positionNum = maybe.find(base)
                                
                                if positionNum == 0:
                                    if num!= 0:
                                        lines[i] = f'</head_posi_{num-1}><head_posi_{num}>' + lines[i]
                                        break
                                    elif num == 0:
                                        lines[i] = f'<head_posi_{num}>' + lines[i]
                                        break
                                else:
                                    if num != 0:
                                        lines[i] = lines[i][:positionNum] + f'</head_posi_{num-1}>' + f'<head_posi_{num}>' + lines[i][positionNum:]
                                        break
                                    if num == 0:
                                        lines[i] = lines[i][:positionNum] + f'<head_posi_{num}>' + lines[i][positionNum:]
                                        break

                                    break

            #最後の見出しの閉じタグを追加,</html>の後ろはまずい気がする
            if num == len(h2Titles) - 1:
                lines.insert(-1, f'</head_posi_{num}>')

        #タグを追加したlinesでhtmlファイルを更新
        return lines

    #マークをつけたhtmlファイルを作成
    def createCounted(self, lines):
        with open('flap/application/scripts/tempo/ans.html', 'w') as f:
            for line in lines:
                f.writelines(line)

if __name__ == '__main__':

    #メモファイルから読み込み
    #URL = 'https://best-selection.co.jp/media/recommend/'
    
    ins = FindHead('flap/application/scripts/tempo/test')
    ins.createCounted(ins.sepaArtiOpen(ins.findH2()))