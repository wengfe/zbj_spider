
from lxml import etree
import requests
# url = 'https://music.douban.com/top250'
url = 'http://task.zbj.com/t-ppsj/p1s5.html'
proxies = {
            'http': 'http://218.15.25.153:808'
        }

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'

headers = {'User-Agent': user_agent}

html = requests.get(url,proxies=proxies,headers=headers).text
print(html)
s = etree.HTML(html)
# title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/text()')[0]
tds = s.xpath('/html/body/div[4]/div[1]/div/div/div[5]/table/tr')
for td in tds:
    price = td.xpath('./td/p/em/text()')
    href = td.xpath('./td/p/a/@href')
    title = td.xpath('./td/p/a/text()')
    subTitle = td.xpath('./td/p/text()')
    deadline = td.xpath('./td/span/text()')
    price = price[0] if len(price)>0 else ''
    title = title[0] if len(title)>0 else ''
    href = href[0] if len(href)>0 else ''
    subTitle = subTitle[0] if len(subTitle)>0 else ''
    deadline = deadline[0] if len(deadline)>0 else ''
    print(price,title,href,subTitle,deadline)
    print('----------------------------------------')
    # spiderDetail(href)

# print(title)
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[4]/td[1]
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[1]/td[1]
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[40]/td[1]
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[9]/td[1]
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[1]/td[1]/p[1]/a[1]

# price
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[4]/td[1]/p[1]/em
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[11]/td[1]/p[1]/em
# /html/body/div[4]/div[1]/div/div/div[5]/table/tr[11]/td[1]/p[1]/a