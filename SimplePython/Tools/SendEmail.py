#-*- coding:cp936 -*-
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib,datetime

msg=MIMEMultipart()
att=MIMEText(open(u'd:\\text.txt','rb').read(),'base64','gb2312')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="text.ttx"'
msg.attach(att)

msg['to']='371111@qq.com'
msg['from']='rollngzhang@gmail.com'
msg['subject']=Header('test'+datetime.date.today(),'gb2312')

server=smtplib.SMTP('smtp.qq.com')
server.login('371111','123')
error=server.sendmail(msg['from'],msg['to'],msg.as_string())
server.close()
print error