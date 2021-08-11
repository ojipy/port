import csv

class GetCompetitors:

    def __init__(self, query):
        self.query = query
    
    #sarpを格納したtsvファイルの整頓
    def openTSV(self):

        arrangedL = []

        with open('data/results/' + f'{self.query}.tsv', encoding = 'utf-8', newline = '') as f:
            for cols in csv.reader(f, delimiter = '\t'):
                arrangedL.append(cols)

            #colsは[[一行目のヘッダ], [日付, 順位, domain, title, url. discription]...]
            #titleが3, urlが4

        return arrangedL

if __name__ == '__main__':

    ins = GetCompetitors('クレジットカード おすすめ')
    print(ins.openTSV())