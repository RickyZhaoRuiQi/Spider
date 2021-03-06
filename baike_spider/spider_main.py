from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):

    # 构造器 构造url管理器 下载器 解析器和输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 执行方法
    def craw(self, root_url):

        # 控制爬取数量 不然会一直爬取下去
        count = 1

        # 将初始url加入url管理器中的待爬取集合中
        self.urls.add_new_url(root_url)

        # 当待爬取集合中还有url存在时
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 获取数据
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except(Exception):
                print(Exception)
                print('craw failed')
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
