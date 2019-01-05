import urllib.request


class HtmlDownloader(object):

# 方法 返回读取到的数据
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
