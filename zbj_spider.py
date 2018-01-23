
# coding=utf-8
from get_proxies import hasPoxies 
import requests
from lxml import etree

def get_url():
    for i in range(33):
        url = 'http://task.zbj.com/t-ppsj/p{}s5.html'.format(i+1)
        spiderPage(url)


def spiderPage(url):
    if url is None:
        return None


    proxiy_url = 'http://www.xicidaili.com/nn/'
    proxiy_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        
     #修改请求头
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'

    headers = {'User-Agent': user_agent}
    proxies_ob = hasPoxies(proxiy_url,proxiy_headers)
    # proxies = proxies_ob.get_proxies()
    # print(proxies)
    # htmlText = requests.get(url).text
    # print(htmlText)
    # selector = etree.HTML(htmlText)
    # tds = selector.xpath('//*[@class="tab-switch tab-progress"]/table/tr')
    try:


        proxies = {
            'http': 'http://218.15.25.153:808'
        }

       
        htmlText = requests.get(url, headers=headers,proxies=proxies).text


        
        selector = etree.HTML(htmlText)
        tds = selector.xpath('/html/body/div[4]/div[1]/div/div/div[5]/table/tr')

        

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
            spiderDetail(href)
    except:
        print('出错1')

def spiderDetail(url):
    if url is None:
        return None
    try:
        htmlText = requests.get(url).text
        selector = etree.HTML(htmlText)
        aboutHref = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/a/@href')
        price = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/div/p[1]/text()')
        title = selector.xpath('//*[@id="utopia_widget_10"]/div[1]/div/div/h2/text()')
        contentDetail = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/div[1]/text()')
        publishDate = selector.xpath('//*[@id="utopia_widget_10"]/div[2]/div/div[1]/p/text()')
        aboutHref = aboutHref[0] if len(aboutHref) > 0 else ''  # python的三目运算 :为真时的结果 if 判定条件 else 为假时的结果
        price = price[0] if len(price) > 0 else ''
        title = title[0] if len(title) > 0 else ''
        contentDetail = contentDetail[0] if len(contentDetail) > 0 else ''
        publishDate = publishDate[0] if len(publishDate) > 0 else ''
        print(aboutHref,price,title,contentDetail,publishDate)
    except:
      print('出错2')

if '_main_':
    get_url()