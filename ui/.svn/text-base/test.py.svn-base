#coding: utf-8
import re
# import urllib2, urllib

# def get(url):
#     req = urllib2.Request(url)
#     #enable cookie  
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
#     response = opener.open(req)  
#     data = response.read()
#     return data

# def ucasLib(title):
#     url = 'http://159.226.100.16/X?op=find&base=cas01&request='+title.encode('utf-8')+'&user_name=www-x&user_password=www-x'
#     return get(url)
s = ''
with open('xml.txt', 'r') as f:
    s = f.read()
s = re.sub(r'[\r,\n]', '', s)
print s
regex  = r'\<varfield id\=\"905\".*?'
regex += r'\<subfield label\=\"d\"\>(.*?)\<\/subfield\>.*?'
regex += r'\<subfield label\=\"e\"\>(.*?)\<\/subfield\>'
print regex
print  re.findall(regex, s)
