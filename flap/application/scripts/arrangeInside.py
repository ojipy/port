from bs4 import BeautifulSoup
import MeCab

class AdjustArti():

    def __init__(self, memoFile, artiFile):
        self.memoFile = memoFile
        self.artiFile = artiFile
        pass

    def openQuery(self):
        with open(f'{self.memoFile}') as f:
            l = [line for line in f.readlines()]
        
        q = l[0].replace('\n', '')

        l.remove(l[0])

        for i, e in enumerate(l):
            if '\n' in e:
                l[i] = e.replace('\n', '')
        
        return q, l

    def adjustFile(self):

        with open(f'{self.artiFile}') as f:
            l = f.readlines()
        #<fook>の追記

        l.insert(0, '<fook>\n')

        for i, e in enumerate(l):
            if '<head_posi_0>' in e:
                l.insert(i, '</fook>\n')
                break
            else:pass

        with open(f'{self.artiFile}', 'w') as f:
            for line in l:
                f.writelines(line)
        
        pass

    def findFook(self, suggests):
        soup = BeautifulSoup(open(self.artiFile), 'html.parser')
        fookTxt = soup.findAll('fook')

        import MeCab
        sep = MeCab.Tagger('-Owakati')

        lSeped = sep.parse(str(fookTxt[0])).split()

        wordsDic = {}

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

        return wordsDic
        
