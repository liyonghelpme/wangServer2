#coding:utf8
import urllib2
import urllib
import json
import random
name = u'中环英雄豪杰真夺目自然亮丽花哨疯狂英俊浪漫爱恨热血轻易动听花朵醉酒'
for i in xrange(100, 200):
    data = {"account":'liyong%d'%(i)}
    req = 'http://localhost:9000/login'
    r = urllib2.urlopen(req, urllib.urlencode(data))
    rp = json.loads(r.read())
    uid = rp['uid']

    req = 'http://localhost:9000/rename'
    v1 = random.randint(0, len(name)-1)
    v2 = random.randint(0, len(name)-1)
    data = {'uid':uid, 'name':(name[v1]+name[v2]).encode('utf8')}
    print data
    r = urllib2.urlopen(req, urllib.urlencode(data))
    rp = json.loads(r.read())
#print rp
