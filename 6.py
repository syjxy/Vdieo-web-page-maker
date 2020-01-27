
#/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/div/div[51]/a

import lxml
from lxml import etree
import random
s = ['Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',
	'Mozilla/5.0 (Android; Tablet; rv:14.0) Gecko/14.0 Firefox/14.0',
	'Mozilla/5.0 (Linux; Android 4.1.2; Nexus 7 Build/JZ054K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
	'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3']
html = etree.parse('./jyzx.html',etree.HTMLParser())
yourname = "爱情公寓5"
for i in range(1,21):
    n = random.randint(0,5)
    head = s[n]
    headers = {'User-Agent': head}
    a = str(i)
    s1 = '//*[@id="j-body"]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[5]/div/ul[2]/li[{}]/a/@href'.format(a)
    print(s1)
    s2 = yourname+"第 {} 集".format(a)
    a = str(a)
    url = html.xpath(s1)
    name = 'https://vip.bljiex.com/?v='+url[0]
    rurl= '<center><h1><a href="{0}">{1}</a></h1></center>'.format(name, s2)
    with open('./6.txt','a+') as f:
        f.write(rurl)
        f.write('\n')
    print(rurl)

#https://www.1717yun.com/jx/ty.php?url=
#https://vip.bljiex.com/?v=
