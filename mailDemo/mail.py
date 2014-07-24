# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import random
import time

# ！！
mail_port=465

def sendMail(mail_server, mail_user, mail_psw, to, content, subject="subject"):
    server = smtplib.SMTP_SSL()
    server.connect(mail_server, mail_port)
    server.login(mail_user, mail_psw)
    
    print('login ok!')

    # Create message container - the correct MIME type is multipart/alternative.  
    msg = MIMEMultipart('alternative')  
    msg['Subject'] = subject
    msg['From'] = '***@163.com'
    msg['To'] = '***@qq.com;' + to
      
    # Create the body of the message (a plain-text and an HTML version).  
    text = '' 
    html = """
    <html> 
      <head></head> 
      <body> 
        <a center href='""" + content + """''>耐克品牌商业特卖</a>
        <br/><br/><br/><p center >点一点，看一看，点不了吃亏，看不了上当（^.^）</p>
      </body> 
    </html> 
    """
    
    part2 = MIMEText(html, 'html')
    msg.attach(part2)  
    
    
    #msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"% (mail_user, send_to, subject, msg.as_string()))
    server.sendmail(mail_user, msg['To'], msg.as_string())

def getQQMail():
    to = ''
    for i in xrange(0, 50):
        q = random.randint(100000, 1769678889)
        to += str(q) + '@qq.com;'
    return to

if __name__ == "__main__":
    server = {
        'qq':'smtp.qq.com',
        '163':'smtp.163.com'
    }
    f = open('user.txt', 'r')

    user="****@163.com"
    psw="****"
    ls = f.readlines()
    for x in ls:
        x = str(x).strip()
        print(x)
        if x == '':
            continue;
        else:
            li = x.split(' ')
            user = str(li[0])
            psw = str(li[1])
            
            to = getQQMail()
            
            mtype = user[user.index('@') + 1 : user.index('.')]

            start = time.time()
            print(start)
            print('server:' + server[mtype] + ' ' + 'user:' + user + ' ' + 'psw:' + psw + ' ' + 'to:' + to)

            sendMail(
                server[mtype],
                user,
                psw,
                to, 
                "**",
                '耐克品牌商业特卖',

                )
            end = time.time()
            print(end)
            print('发送到:' + to)
            print('花费时间毫秒数' + str(end - start))
    print('ok')