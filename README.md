# 初识爬虫

---

- 什么是爬虫

	- 简单定义：一段自动抓取互联网信息的程序

	- 价值：互联网数据，为我所用

---

- 简单爬虫架构
	- 爬虫调度端
	- 爬虫
		1. URL管理器
		2. 网页下载器
		3. 网页解析器
	- 应用

---

- URL管理器

	- 管理待抓取URL集合和已抓取URL集合
		1. 防止重复抓取、防止循环抓取
		2. 添加RUL->判断是否重复->判断是否有待爬取URL->获取待爬取URL->将URL从待爬取移动到已爬取
	- 实现方式
		1. 内存->待爬取URL集合：set->已爬取URL集合：set
		2. 关系数据库->mysql urls(url,is_crawled(标识待爬取和已爬取))
		3. 缓存数据库->redis->待爬取URL集合：set->已爬取URL集合：

- 网页下载器

    - 将互联网上URL对应的网页下载的本地的工具
    - 下载器
        1. urllib2->python官方基础模块
        2. requests->第三方包
    - urllib2下载网页的方法
        1. response=urllib2.urlopen(url)
        2. 添加data、http header(request.add_data、request.add_header)->urllib2.Request->urllib2.urlopen(url)
        3. 添加特殊情景的处理器(HTTPCookieProcesspr、ProxyHandler、HTTPSHandler、HTTPRedirectHandler)->opener=urllib2.build_opener(handler)->urllib2.install_opener(opener)->urllib2.urlopen(request)
        
- 网页解析器

    - 从网页中提取有价值数据的工具
    - 解析器
        1. 正则表达式->模糊匹配（文章复杂很麻烦）
        2. html.parser
        3. Beautiful Soup    --->   结构化解析
        4. lxml
