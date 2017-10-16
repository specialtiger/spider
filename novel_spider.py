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

k_chapter = 2
k_urlopen_timeout = 5
k_fetch_interval = 1

def r_o_html(url):
    print('r_o_html begin')

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

def re_findall(re_string, operation, html):

    print('re_findall begin')
    pattern = re.compile(re_string, re.I)

    if operation == 'findall':
        result = pattern.findall(html)
    else:
        print('this operation is invalid')
        exit(-1)

    print('re_findall end')
    return result

def write_html_head(open_file):
    head = '''<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="maximum-scale=1.0, minimum-scale=1.0, user-scalable=0, initial-scale=1.0, width=device-width"/>
    <meta name="format-detection" content="telephone=no, email=no, date=no, address=no">
    <link rel="stylesheet" type="text/css" href="../css/api.css" />
    <style>
        body {
            background-color: #e4ebf1;
        }
    </style>

</head>'''
    open_file.write(head+'\n')

def write_html_tail(open_file):
    open_file.write('</html>\n')

if __name__ == '__main__':
    url_base = 'http://www.7kankan.la/book/1/'

    html = r_o_html(url_base)

    findall_title = re_findall(r'<h1 class="bookTitle">(.*)</h1>', 'findall', html)

    findall_chapter = re_findall(r'<dd class="col-md-3"><a href=[\',"](.+?)[\',"] title=[\',"](.+?)[\',"]>', 'findall', html)

    # with open(findall_title[0] + '.txt', 'w+', encoding='utf-8') as open_file:
    with open('novel.html', 'w') as open_file:
        write_html_head(open_file)
        print('article文件打开', findall_chapter)
        end = len(findall_chapter)
        start = max(0, end - k_chapter)
        open_file.write("<p>")
        for i in range(start, end):
            print('第' + str(i) + '章')

            open_file.write('<h2>' + findall_chapter[i][1] + '</h2>\n')

            url_chapter = url_base + findall_chapter[i][0]

            html_chapter = r_o_html(url_chapter)

            findall_article = re_findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />', 'findall', html_chapter)

            findall_article_next = findall_chapter[i][0].replace('.html', '_2.html')

            url_nextchapter = url_base + findall_article_next

            html_nextchapter = r_o_html(url_nextchapter)

            if html_nextchapter:
                findall_article.extend(re_findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />', 'findall', html_nextchapter))

                for text in findall_article:
                    open_file.write('<br>&nbsp;&nbsp;&nbsp;&nbsp;%s<br />\n'%text)

            time.sleep(1)
        open_file.write("</p>\n")

        write_html_tail(open_file)

    print('文件写入完毕')
