# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:31:42 2017
@author: lart
"""
# import urllib.request as url_req
import urllib2 as url_req
import re, socket, time
import sys
 
reload(sys)
sys.setdefaultencoding('utf-8')

k_chapter = 5
k_urlopen_timeout = 5
k_fetch_interval = 1

def r_o_html(url):
    # print('r_o_html begin')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}

    request = url_req.Request(url, headers=headers)

    NET_STATUS = False
    while not NET_STATUS:
        try:
            response = url_req.urlopen(request, data=None, timeout=5)
            html = response.read().decode('GBK')
            print('NET_STATUS is good')
            print('r_o_html end')
            return html
        except socket.timeout:
            print('NET_STATUS is not good')
            NET_STATUS = False

def re_findall(re_string, html):
    print('re_findall begin')
    pattern = re.compile(re_string, re.I)
    result = pattern.findall(html)
    print('re_findall end')
    return result


if __name__ == '__main__':
    url_base = 'http://www.piaotian.com/html/8/8337/'

    html = r_o_html(url_base+'index.html')

    r_titles = re_findall(r'<h1>(.*)</h1>', html)
    novel_title = r_titles[0]
    print(r_titles)
    # url, title
    # findall_chapter = re_findall(r'<dd class="col-md-3"><a href=[\',"](.+?)[\',"] title=[\',"](.+?)[\',"]>', html)
    findall_chapter = re_findall(r'<li><a href="(.*)">(.*)</a></li>', html)

    with open(novel_title + '.txt', 'w') as open_file:
        print('chapters count:', len(findall_chapter))
        end = len(findall_chapter)
        start = max(0, end - k_chapter)
        for i in range(start, end):
            print('第' + str(i) + '章', findall_chapter[i])

            open_file.write('\n\n\t' + findall_chapter[i][1] + '\n --------------------------------------------------------------------- \n')

            url_chapter = url_base + findall_chapter[i][0]

            html_chapter = r_o_html(url_chapter)

            findall_article = re_findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />', html_chapter)
            findall_article_next = findall_chapter[i][0].replace('.html', '_2.html')

            url_nextchapter = url_base + findall_article_next

            for text in findall_article:
                open_file.write(text + '\n')

            time.sleep(1)

    print('文件写入完毕')
