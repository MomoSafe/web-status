#coding:utf8

#from datetime import *
import time 
#starttime=datetime.now()
#import urllib
import datetime
import pycurl
import StringIO
import sys
import smtplib  
from email.mime.text import MIMEText  



#d=(raw_input(u"请输入域名:"))

#starttime=datetime.datetime.now()
#print starttime

#endtime=datetime.datetime.now()
#print endtime

#print str(int((endtime - starttime).microseconds)*0.001)+"u毫秒"

class Test:
        def __init__(self):
                self.contents = ''
        def body_callback(self,buf):
                self.contents = self.contents + buf
def conn(input_url):
    #checkurl="www.baidu.com"

    print u'http代码     数据大小   响应时间   当前时间 '
    while (True):	
        c=pycurl.Curl()
        t=Test()
        c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
        c.setopt(pycurl.URL,input_url)
        c.perform()
        http_code = c.getinfo(pycurl.HTTP_CODE)
        http_conn_time =  c.getinfo(pycurl.CONNECT_TIME)
        http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
        dt=datetime.datetime.now()
        a=http_code


        if a == 200:

            print u"%d          %d      %s   %s 网站正常 "%(http_code,http_size,http_conn_time,(str(dt.strftime('%Y-%m-%d %H:%M:%S')))) 
        
        elif a == 302:
            print u"%d          %d      %f   %s 网站正常"%(http_code,http_size,http_conn_time,(str(dt.strftime('%Y-%m-%d %H:%M:%S')))) 
        else:
            print u"%d $s 网站异常" % (http_code,(str(dt.strftime('%Y-%m-%d %H:%M:%S'))))
            mailto_list=["xxx@mail，com"] 
            mail_host="smtp.126.com"  #设置服务器
            mail_user="test@126.com"    #用户名
            mail_pass="testtest"   #口令 
            mail_postfix="126.com"  #发件箱的后缀
              
            def send_mail(to_list,sub,content):  
                me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
                msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
                msg['Subject'] = sub  
                msg['From'] = me  
                msg['To'] = ";".join(to_list)  
                try:  
                    server = smtplib.SMTP()  
                    server.connect(mail_host)  
                    server.login(mail_user,mail_pass)  
                    server.sendmail(me, to_list, msg.as_string())  
                    server.close()  
                    return True  
                except Exception, e:  
                    print str(e)  
                    return False  
            if __name__ == '__main__':  
                if send_mail(mailto_list,"hello","your web could not connect!!"):  
                    print u"发送成功"  
                else:  
                    print u"发送失败"  

        
        time.sleep(1)



if __name__ == '__main__':
        input_url = sys.argv[1]
        conn(input_url)



