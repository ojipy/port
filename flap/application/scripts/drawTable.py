class DrawTable():

    def __init__(self, fookL, bodyL, tableFile):
        self.fook = fookL
        self.body = bodyL
        self.file = tableFile

    def drawFook(self):

        with open('flap/application/scripts/tempo/memo.txt') as m:
            wl = [e for e in m.readlines()]
        wl.remove(wl[0])
        for i, e in enumerate(wl):
            if '\n' in e:
                wl[i] = e.replace('\n', '')

        with open(f'{self.file}', 'w') as f:
            f.writelines("{% extends 'layout.html' %}\n")
            f.writelines("{% block head %}{% endblock %}\n")
            f.writelines("{% block body %}\n")

            f.writelines('<div class="container">\n')
            f.writelines('<table class="table">\n')
            
            f.writelines('<thead>\n')
            f.writelines('<tr>\n')

            f.writelines('<th>#</th>')
            f.writelines('<th>フックと見出し2</th>\n')
            f.writelines('<th>サジェスト</th>\n')

            f.writelines('</tr>\n')
            f.writelines('</thead>\n')

            f.writelines('<tbody>\n')

            f.writelines('<tr>\n')

            f.writelines('    <th scope="row">0</th>\n')
            f.writelines('    <td>フック文</td>\n')
            f.writelines('    <td>\n')
            f.writelines('    <table class="table">\n')
            f.writelines('    <tr>\n')
            for element in wl:
                f.writelines(f'<td>{element}</td>\n')
                pass
            f.writelines('    </tr>\n')
            f.writelines('    <tr>\n')
            for element in wl:
                f.writelines(f'<td>{self.fook[element]}</td>\n')
                pass
            f.writelines('    </tr>\n')
            f.writelines('    </td>\n')

            f.writelines('    </tr>\n')
            f.writelines('    </table>\n')
            f.writelines('    </td>\n')

            f.writelines('</tr>\n')

            titles = []
            suggests = []


            #まず見出しの数だけループ
            for i, heads in enumerate(self.body):
                if type(heads) == str:
                    titles.append(heads)
                else:
                    suggests.append(heads)


            for num, title in enumerate(titles):

                f.writelines('    <tr>\n')
                f.writelines(f'    <th scope="row">{num + 1}</th>\n')
                f.writelines(f'    <td>{title}</td>\n')
                f.writelines('    <td>\n')
                f.writelines('    <table class="table">\n')
                f.writelines('    <tr>\n')

                #サジェストの数だけループ
                for element in wl:
                    f.writelines(f'    <td>{element}</td>\n')
                    pass
                
                f.writelines('    </tr>\n')
                f.writelines('    <tr>\n')

                #サジェスト同数の登場回数
                for element in wl:
                    f.writelines(f'    <td>{suggests[num][element]}</td>\n')

                f.writelines('    </tr>\n')
                f.writelines('    </table>\n')
                f.writelines('    </td>\n')
                f.writelines('    </tr>\n')



            f.writelines('</tbody>\n')
            f.writelines('</table>\n')
            f.writelines('</div>\n')

            f.writelines("{% endblock %}\n")

