# coding=utf-8
'''
Created on 2013-7-30

@author: lin.xr
'''
import socket
import urllib2

url = 'http://127.0.0.1:8080/calendar/s?func=calendar:getMessageList&sid=MTM3NTI1MDEwMDAwMDE3NDA0MDY0NQAA000001&cguid=1355226216486'

header = {
          'Host' : '127.0.0.1:8080',
          'Connection' : 'Keep-Alive',
          'User-Agent' : 'android-async-http/1.4.3 (http://loopj.com/android-async-http)',
          'Accept-Encoding' : 'gzip',
          'Content-Type' : 'application/xml; charset=utf-8',
          'Cookie' : 'RMKEY=3208053501375250100'
          }

xml = '<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\' ?><object><int name="comeFrom">7</int><int name="pageIndex">1</int><int name="pageSize">20</int></object>'

timeout = 15
socket.setdefaulttimeout(timeout)

opener = urllib2.build_opener()
req = urllib2.Request(url=url, headers=header, data=xml)
res = opener.open(req)

content = res.read()
res.close()
print content
