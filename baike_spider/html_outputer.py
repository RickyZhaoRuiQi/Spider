class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 使用的python3，在window下，新文件的默认编码是gbk，python解释器会用gbk编码去解析我们的网络数据流txt，
        # 然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，出现问题。
        # 应写为：fout = open('output.html','w',encoding='utf-8') 同时在html中声明
        fout = open('output.html', 'w', encoding='utf-8')
        #fout.write('<meta charset="UTF-8">')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        # ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
