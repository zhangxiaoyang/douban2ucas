from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib  
import urllib2  
import json
from models import DoubanUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def post(code):
    # auth
    url = 'https://www.douban.com/service/auth2/token'
    data = {
        'client_id':'0d9a0fb718d8510628ce2f254a88f312',
        'client_secret':'782789e87c58c83c',
        'redirect_uri':'http://douban2ucas.sinaapp.com/auth/',
        'grant_type':'authorization_code',
        'code':code
        }

    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  

    auth_data = response.read()
    auth_data = json.loads(auth_data)

    # auto info
    access_token = auth_data['access_token']
    expires_in = auth_data['expires_in']
    refresh_token = auth_data['refresh_token']
    douban_user_id = auth_data['douban_user_id']
    douban_user_name = auth_data['douban_user_name']
    
    # user info
    req = urllib2.Request('https://api.douban.com/v2/user/'+str(douban_user_id))
    response = opener.open(req)  
    user_data = response.read()
    user_data = json.loads(user_data)
    douban_user_avatar = user_data['avatar']
	
    return douban_user_id, douban_user_name, douban_user_avatar

def index(request):
    try:
        user = DoubanUser.objects.get(userID=int(request.user.username))
        userID = user.userID
        userName = user.userName
        userAvatar = user.userAvatar
    except:
        userID = None
        userName = None
        userAvatar = None
    return render(request, 'index.html', locals())

@login_required(login_url='/')
def bye(request):
    logout(request)
    return render(request, 'index.html', locals())

def sorry(request):
    return render(request, 'sorry.html', locals())

def auth(request):
    code = request.GET['code']
    try:
        userID, userName, userAvatar = post(code)
    except:
        print '*\tLogin with douban account error!'
        return render(request, 'sorry.html', locals())

    try:
        DoubanUser(
            userID=int(userID),
            userName=userName,
            userAvatar=userAvatar
            ).save()
        User.objects.create_user(str(userID))
    except:
        print '*\tUser', userID, 'already exists...'
    user =  authenticate(username=str(userID))
    login(request, user)
    return render(request, 'index.html', locals())