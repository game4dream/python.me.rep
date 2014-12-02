#!/usr/bin/env python
#encoding=utf-8

'''
Created on 2013-11-1
@author: chenming
'''

import os, sys
from optparse import OptionParser, OptionGroup
import urllib, urllib2, cookielib, socket
import time
import shutil

# 重设编码格式
reload(sys)
sys.setdefaultencoding('utf8') 
os.environ['LC_ALL'] = "en_US.UTF-8" # cron环境问题导致中文乱码

readme = u'''脚本简介'''

# 当天日期，可用于数据查询日期的标记
nowday = time.strftime('%Y-%m-%d',time.localtime(time.time()))
nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 命令行运行时，取脚本全路径
scriptName = sys.argv[0] 
_, f = os.path.split(scriptName);  
# 临时数据、结果数据存放目录，以脚本名.tmp为文件夹名，创建到脚本当前目录
# 若已存在，则删除，重新创建文件夹，用于清空临时数据
tmpPath = f + '.tmp'
if os.path.exists(tmpPath):
    shutil.rmtree(tmpPath) 
os.mkdir(tmpPath)
# 数据文件路径
pathResult = tmpPath + os.sep + f + '.txt'
os.system('echo "' + readme + '" >> ' + pathResult)
os.system(u'echo "执行时间：' + nowtime + '" >> ' + pathResult)

def analysis():
    usage = '%prog'
    parser = OptionParser(usage, prog=u'临时查询', version='%prog 1.0')
    group = OptionGroup(parser, 
                        'desc and example', 
                        readme)
    parser.add_option_group(group)
    (options, _) = parser.parse_args()
    return options

# 控制台及时输出，不换行
def log(i):
    sys.stdout.write(i)
    sys.stdout.flush()

def doBuz(options):
    log('>')

if __name__ == '__main__':
    options = analysis()
    doBuz(options)
    print('\nsucc')
   
