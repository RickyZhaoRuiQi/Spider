class UrlManager(object):

# 构造器 初始化一个 new_urls集合 和一个old_urls集合
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

# 方法 添加url到新new_urls集合
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

# 方法 添加urls集合到new_urls集合
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

# 方法 判断待爬取new_urls集合中是否还有url
    def has_new_url(self):
        return len(self.new_urls) != 0

# 方法 循环取出new_urls中的集合爬取，并将爬取过的urls放入old_urls
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
