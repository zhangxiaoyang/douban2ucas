#coding: utf-8
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import DoubanUser
from django.contrib.auth.models import User
import urllib2, urllib
import json
import re
MAX_ENTRY = 1

def get(url):
    req = urllib2.Request(url)

    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req)  
    data = response.read()
    return data

def getDoubanCols(userID):
    url = 'https://api.douban.com/v2/book/user/'+str(userID)+'/collections'
    data = get(url)
    collections = json.loads(data)['collections']
    return collections

def parseXmlInt(xml, tag):
    regex = '\<' + tag + '\>(\d+)\<\/' + tag + '\>'
    intList = re.findall(regex, xml)
    return intList

def parseXmlShelf(xml):
    xml = re.sub(r'[\r,\n]', '', xml)
    regex  = r'\<varfield id\=\"905\".*?'
    regex += r'\<subfield label\=\"d\"\>(.*?)\<\/subfield\>.*?'
    regex += r'\<subfield label\=\"e\"\>(.*?)\<\/subfield\>'
    shelfList = re.findall(regex, xml)
    return [ d+'/'+e for d,e in shelfList ]

def parseXmlSubLib(xml):
    regex  = r'\<sub\-library\>(.*?)\<\/sub\-library\>'
    sublibs = re.findall(regex, xml)

    regex  = r'\<item\-status\>(.*?)\<\/item\-status\>'
    status = []
    for st in re.findall(regex, xml):
        if st == '11': status.append(True)
        else: status.append(False)
    return sublibs, status

def getUcasLib(ibsn):
    # get set_number
    url = 'http://159.226.100.16/X?op=find&base=cas01&request='+str(ibsn)+'&user_name=www-x&user_password=www-x'
    xml = get(url)

    # ucas lib does not have this book
    if '<error>' in xml:
        return None
    
    set_number = parseXmlInt(xml, 'set_number')[0]
    no_entries = parseXmlInt(xml, 'no_entries')[0]

    entries = int(no_entries)
    entries_list = [ '%09d' % entry for entry in range(1,entries+1) ]
    if len(entries_list) > 10: entries_list = entries_list[:MAX_ENTRY]

    # get doc_number list
    url = 'http://159.226.100.16/X?op=present&set_no='+set_number
    url = url + '&set_entry='+','.join(entries_list)+'&format=marc'
    xml = get(url)
    doc_numbers = parseXmlInt(xml, 'doc_number')
    doc_shelfs = parseXmlShelf(xml)
    
    ret = []
    # get location details
    for index, doc_number in enumerate(doc_numbers):
        url = 'http://159.226.100.16/X?op=item-data&doc_number='+doc_number+'&base=cas01'
        xml = get(url)
        sublib, status = parseXmlSubLib(xml)
        try: shelf = doc_shelfs[index]
        except: shelf = u'暂无'
        for i in range(len(sublib)):
            status[i] = True
            try:
                int(sublib[i])
                sublib[i] = u'未能获取馆藏信息'
                status[i] = False
            except:pass
        ret.append({
            'shelf':shelf,
            'sublib':sublib,
            'status':status
            })
    return ret

@login_required(login_url='/')
def wish(request):
    books = []
    try:
        user = DoubanUser.objects.get(userID=int(request.user.username))
    except:
        print '*\tYou must login fisrt!'
        return HttpResponse(json.dumps(books))

    collections = getDoubanCols(user.userID)
    for col in collections:
        if col['status'] == 'wish':
            book = {}
            book['title'] = col['book']['title']
            book['id'] = col['book']['id']
            book['author'] = col['book']['author'][0]
            book['publisher'] = col['book']['publisher']
            book['pubdate'] = col['book']['pubdate']
            book['average'] = col['book']['rating']['average']
            book['pages'] = col['book']['pages']
            book['price'] = col['book']['price']
            book['isbn'] = col['book']['isbn13']
            book['summary'] = col['book']['summary']
            book['url'] = col['book']['alt']
            book['image'] = col['book']['image']
            books.append(book)
    return HttpResponse(json.dumps(books))


@login_required(login_url='/')
def read(request):
    books = []
    try:
        user = DoubanUser.objects.get(userID=int(request.user.username))
    except:
        print '*\tYou must login fisrt!'
        return HttpResponse(json.dumps(books))

    collections = getDoubanCols(user.userID)
    for col in collections:
        if col['status'] == 'read':
            book = {}
            book['title'] = col['book']['title']
            book['id'] = col['book']['id']
            book['author'] = col['book']['author'][0]
            book['publisher'] = col['book']['publisher']
            book['pubdate'] = col['book']['pubdate']
            book['average'] = col['book']['rating']['average']
            book['pages'] = col['book']['pages']
            book['price'] = col['book']['price']
            book['isbn'] = col['book']['isbn13']
            book['summary'] = col['book']['summary']
            book['url'] = col['book']['alt']
            book['image'] = col['book']['image']
            books.append(book)
    return HttpResponse(json.dumps(books))

@login_required(login_url='/')
def reading(request):
    books = []
    try:
        user = DoubanUser.objects.get(userID=int(request.user.username))
    except:
        print '*\tYou must login fisrt!'
        return HttpResponse(json.dumps(books))

    collections = getDoubanCols(user.userID)
    for col in collections:
        if col['status'] == 'reading':
            book = {}
            book['title'] = col['book']['title']
            book['id'] = col['book']['id']
            book['author'] = col['book']['author'][0]
            book['publisher'] = col['book']['publisher']
            book['pubdate'] = col['book']['pubdate']
            book['average'] = col['book']['rating']['average']
            book['pages'] = col['book']['pages']
            book['price'] = col['book']['price']
            book['isbn'] = col['book']['isbn13']
            book['summary'] = col['book']['summary']
            book['url'] = col['book']['alt']
            book['image'] = col['book']['image']
            books.append(book)
    return HttpResponse(json.dumps(books))

@login_required(login_url='/')
def ucas(request, isbn):
    details = getUcasLib(isbn)
    if details == None:
        ret = {
            'isbn':isbn,
            'details':False
        }
    else:
        ret = {
            'isbn':isbn,
            'details':details
        }
    return HttpResponse(json.dumps(ret))