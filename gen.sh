#!/bin/bash
pwd=`dirname $0`
cd $pwd
./novel_spider.py
git commit -a -m "gen index html"
git push origin
