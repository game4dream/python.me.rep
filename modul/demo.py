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
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
import email.Encoders as encoders

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
    group.add_option('-l', action='store', dest='lv', default='60', help=u'描述')
    parser.add_option_group(group)
    (options, _) = parser.parse_args()
    return options

def send_mail(mail_from, mail_to, subject, msg_txt, files=[]):
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to

    
    # 文本方式邮件内容
    #text = msg
    #part1 = MIMEText(text, 'plain')

    # html方式邮件内容
    html = msg_txt
    part2 = MIMEText(html, 'html')

    # 加入内容
    #msg.attach(part1)
    msg.attach(part2)

    # 附件
    for f in files:
        #octet-stream:binary data
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
    # smtp host
    s = smtplib.SMTP('mail.game-reign.com')

    mailto_list = mail_to.strip().split(";")
    s.sendmail(mail_from, mailto_list, msg.as_string())

    s.quit()
    return True

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
   
