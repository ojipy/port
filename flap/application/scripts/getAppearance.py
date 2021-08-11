#count words in HTML file marked
from bs4 import BeautifulSoup
import MeCab

class GetLung():

    def __init__(self, fileName):
        
        self.fileName = fileName

        pass

    def openMemo(self):
    #例外の文字やスペース全角半角などをフィルタリングする必要がある

        with open('flap/application/scripts/tempo/memo.txt') as f:
            l = [e for e in f.readlines()]

        q = l[0].replace('\n', '')

        l.remove(l[0])
        for i, e in enumerate(l):
            if '\n' in e:
                l[i] = e.replace('\n', '')
        
        return q, l

    #対象サイトのhtmlを見出し毎で文字列をリストに格納
    def arrangeFile(self):

        with open(f'flap/application/scripts/tempo/{self.fileName}') as f:
            l = f.readlines()
            #htmlの行数　＝＝ len(l)

        soup = BeautifulSoup(open(f'flap/application/scripts/tempo/{self.fileName}'), 'html.parser')

        headNum = soup.findAll('h2')
        
        artiTexts = []#各見出しのテキストを格納

        memoL = []#見出しの開始行番号を格納

        for num in range(len(headNum)):

            for i, artiText in enumerate(l):

                if f'<head_posi_{num}>' in artiText:
                    memoL.append(i)

        for n in range(len(memoL)):

            txtMemoL = []

            for i, artiText in enumerate(l):

                if i < memoL[n]:
                    continue

                if n < len(memoL) - 1:
                    if i >= memoL[n] and i < memoL[n + 1]:
                        txtMemoL.append(artiText)
                    elif i == memoL[n + 1]:
                        artiTexts.append(txtMemoL)
                        break

                elif n == len(memoL) - 1:
                    if i >= memoL[n] and i < len(l) - 1:
                        txtMemoL.append(artiText)
                    elif i == len(l) - 1:
                        artiTexts.append(txtMemoL)
                        break

        arrangedTextsL = []

        for n in range(len(artiTexts)):

            for i, e in enumerate(range(len(artiTexts[n]))):
                if i == 0:
                    continue
                baseTxtL = artiTexts[n]
                baseTxtL[1] = baseTxtL[0] + baseTxtL[1]
                del baseTxtL[0]
            
            import re
            p = re.compile(r'<[^>]*?>')
            tag_str = 'NO DATA'
            try:tag_str = artiTexts[n][0]
            except IndexError:pass
            answer = p.sub('', tag_str)  # Return 文字列のみ

            para = answer.replace('\n', '')

            arrangedTextsL.append(para)
                    

        #beautifulsoupじゃなくてもできるはず!!!!!!!!!!!!!!!!!!!!!!!!!!

        #for num in range(20):
            #headWords = soup.findAll(f'head_posi_{num}')

            #if not headWords == None:
                #artiTexts.append(headWords.text)

        #この返り血が文字列を格納したリストであれば良い。
        return arrangedTextsL

    #見出し毎にKWの出現をカウント
    def countWords(self, artiTexts, suggests, h2Titles):
    #h2TitlesはgetComSource.findH2の返り値を参照
        resultL = []

        sep = MeCab.Tagger('-Owakati')

        for i, e in enumerate(range(len(artiTexts))):
            wordsDic = {}
            try:lSeped = sep.parse(artiTexts[i]).split()
            except AttributeError:break

            for suggest in suggests:
                appearance = lSeped.count(suggest)

                for oneWord in lSeped:
                    if suggest in oneWord and suggest != oneWord:
                        appearance = appearance + 1

                if appearance == 0:
                    for num in range(len(lSeped)):

                        if num < len(lSeped) - 1 and lSeped[num] + lSeped[num + 1] == suggest:
                            appearance = appearance + 1

                wordsDic[suggest] = appearance

            try: t = h2Titles[i].text
            except IndexError:t = 'nodata'
            w = wordsDic
            #print(w)

            resultL.append(t)
            resultL.append(w)

        #print(resultL)

        return resultL






if __name__ == '__main__':
    
    ins = GetLung()
    ins.countWords(ins.arrangeFile(), ins.openMemo()[1])