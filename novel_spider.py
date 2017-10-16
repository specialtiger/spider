#!/usr/bin/env python
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

k_chapter = 8
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

def re_findall(re_string, html):

    print('re_findall begin')
    pattern = re.compile(re_string, re.I)

    result = pattern.findall(html)

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
            font-size: 1.5em;
        }
    </style>

</head>'''
    open_file.write(head+'\n')

def write_html_tail(open_file):
    open_file.write('</html>\n')

if __name__ == '__main__':
    url_base = 'http://www.piaotian.com/html/8/8337/'

    html = r_o_html(url_base+'index.html')

    r_titles = re_findall(r'<h1>(.*)</h1>', html)
    novel_title = r_titles[0]
    print(r_titles)
    # url, title
    findall_chapter = re_findall(r'<li><a href="(.*)">(.*)</a></li>', html)

    # with open(findall_title[0] + '.txt', 'w+', encoding='utf-8') as open_file:
    with open('index.html', 'w') as open_file:
        write_html_head(open_file)
        end = len(findall_chapter)
        start = max(0, end - k_chapter)
        for i in range(start, end):
            open_file.write('<u>' + findall_chapter[i][1] + '</u>\n')

        open_file.write("<p>")
        for i in range(start, end):
            print('第' + str(i) + '章')

            open_file.write('<h2>' + findall_chapter[i][1] + '</h2>\n')

            url_chapter = url_base + findall_chapter[i][0]

            html_chapter = r_o_html(url_chapter)

            findall_article = re_findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />', html_chapter)

            for text in findall_article:
                open_file.write('<br>&nbsp;&nbsp;&nbsp;&nbsp;%s<br />\n'%text)

            time.sleep(1)
        open_file.write("</p>\n")

        write_html_tail(open_file)

    print('文件写入完毕')
