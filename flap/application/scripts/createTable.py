def create(returnL):

    with open('flap/application/scripts/tempo/memo.txt') as m:
        wl = [e for e in m.readlines()]
    wl.remove(wl[0])
    for i, e in enumerate(wl):
        if '\n' in e:
            wl[i] = e.replace('\n', '')



    with open('flap/templates/table.html', 'w') as f:
        f.writelines("{% extends 'layout.html' %}\n")
        f.writelines("{% block head %}{% endblock %}\n")
        f.writelines("{% block body %}\n")

        f.writelines('<div class="container">\n')

        for l in returnL:
            #30個のテーブルを作成
            f.writelines('<table style="border-collapse: collapse; width: 80%;" border size="1" class="table">\n')
            f.writelines('<tbody>\n')
            f.writelines('<tr>\n')
            f.writelines('<td>順位</td>\n')
            try:
                exists = l[3]
            except IndexError:
                l.append('nodata')
                l.append({'KW':'nodata'})#クレカ単体でのエラー参照&検証, h2Titleも格納が必要そう
            f.writelines(f'<td colspan="{len(l[3]) + 1}">サイト名</td>\n')
            f.writelines('</tr>\n')
            #ここまでが1行目のヘッダ

            f.writelines('<tr>\n')
            f.writelines(f'<td>{l[0]}</td>\n')
            f.writelines(f'<td colspan="{len(l[3]) + 1}">{l[1]}</td>\n')
            f.writelines('</tr>\n')
            f.writelines('<tr>\n')
            f.writelines(f'<td rowspan="{len(l) - 2}">見出し</td>\n')

            if l[3] == {'KW':'nodata'}:
                f.writelines('</tr>\n')
                f.writelines('</tbody>\n')
                f.writelines('</table>\n')
                f.writelines('<br>\n')
                f.writelines('<br>\n')
                f.writelines('<br>\n')
                continue

            maxNum = (len(l) - 2)//2

            dic = wl#都度memo.txtをimportする

            for i, e in enumerate(range(maxNum)):

                if i == 0:
                    f.writelines(f'<td rowspan="2">{l[2]}</td>\n')
                else:
                    f.writelines(f'<td rowspan="2">{l[i * 2 + 2]}</td>\n')

                for kw in dic:
                    if i == 0:
                        f.writelines(f'<td>{kw}</td>\n')#複数個ある
                    else:
                        f.writelines(f'<td>{kw}</td>\n')
                    
                f.writelines('</tr>\n')
                f.writelines('<tr>\n')

                for kw in dic:

                    if i == 0:
                        f.writelines(f'<td>{l[2 + 1][kw]}</td>\n')
                    else:
                        f.writelines(f'<td>{l[i * 2 + 3][kw]}</td>\n')
                    
                f.writelines('</tr>\n')


            f.writelines('</tbody>\n')
            f.writelines('</table>\n')
            f.writelines('<br>\n')
            f.writelines('<br>\n')
            f.writelines('<br>\n')

        f.writelines('</div>\n')
        f.writelines("{% endblock %}\n")

if __name__ == '__main__':

    URL = 'https://www.google.com'
    siteName = 'google'

    l = [1, f'<a href="{URL}">{siteName}</a>', 'h2Title1', {'KW1':10, 'KW2':5, 'KW3':15}, 'h2Title2', {'KW1':10, 'KW2':5, 'KW3':15}, 'h2Title3', {'KW1':10, 'KW2':5, 'KW3':15}]
    #これをさらにリストを増やして、30サイト分ループ

    returnL = [l, l, l, l, l]    

    createTable(returnL)