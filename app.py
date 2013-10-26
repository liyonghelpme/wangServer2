#coding:utf8
from flask import Flask, g, abort, session, redirect, url_for, \
     request, render_template, _app_ctx_stack, jsonify
from flaskext import *
import json
import time
from util import *
import random
import util

app = Flask(__name__)
app.config.from_object("config")

@app.before_request
def beforeRequest():
    print("before", request.url, str(request.args), str(request.form))


@app.after_request
def afterQuest(response):
    print (request.url, str(request.args), str(request.form) )
    return response

@app.route('/login', methods=['POST'])
def login():
    print("login now", request.form, request.args)
    account = request.form.get('account', None, type=str)
    user = queryOne('select uid from User where account = %s', account)
    now = int(time.time())
    if user == None:
        uid = insertAndGetId('insert into User (account, crystal, silver, gold) values (%s, 500, 1000, 100)', (account))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 0, 200, 1500, 300, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 1, 202, 1200, 300, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 2, 0, 1700, 250, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 3, 300, 1300, 100, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 4, 224, 1550, 200, now))
    else:
        uid = user["uid"]
    builds = queryAll('select * from UserBuilding where uid = %s', (uid))
    res = queryOne('select * from User where uid = %s', (uid))
    soldiers = queryAll('select * from UserSoldier where uid = %s', (uid))
    return jsonify(dict(uid=uid, builds=builds, serverTime=now, resource=res, soldiers=soldiers))

@app.route('/finishBuild', methods=['POST'])
def finishBuild():
    uid = request.form.get("uid", None, type=int)
    kind = request.form.get("kind", None, type=int)
    px = request.form.get("px", None, type=int)
    py = request.form.get("py", None, type=int)
    bid = request.form.get("bid", None, type=int)
    objectTime = request.form.get("objectTime", None, type=int)
    update('insert into UserBuilding (uid, kind, px, py, bid, objectTime) value(%s, %s, %s, %s, %s, %s)', (uid, kind, px, py, bid, objectTime))
    return jsonify(dict(code=1))

@app.route('/harvestPlant', methods=['POST'])
def harvestPlant():
    uid = request.form.get("uid", None, type=int)
    bid = request.form.get("bid", None, type=int)
    pid = request.form.get("pid", None, type=int)
    gain = request.form.get("gain", None, type=str)
    gain = json.loads(gain)
    doGain(uid, gain)
    now = getTime()
    update('update UserBuilding set objectTime = %s, objectId = %s where uid = %s and bid = %s', (now, pid, uid, bid))
    return jsonify(dict(code=1, pid=pid))

@app.route('/levelUp', methods=['POST'])
def levelUp():
    uid = request.form.get("uid", None, type=int)
    level = request.form.get("level", None, type=int)
    exp = request.form.get("exp", None, type=int)
    update('update User set level = %s , exp = %s where uid = %s', (level, exp, uid))
    return jsonify(dict(code=1))

@app.route('/finishPlan', methods=['POST'])
def finishPlan():
    uid = request.form.get("uid", None, type=int)
    builds = request.form.get("builds", None, type=str)
    builds = json.loads(builds)
    for k in builds:
        update('update UserBuilding set px=%s, py=%s where uid = %s and bid = %s', (k[1], k[2], uid, k[0]))
    return jsonify(dict(code=1))

@app.route('/harvestMine', methods=['POST'])
def harvestMine():
    uid = request.form.get("uid", None, type=int)
    bid = request.form.get("bid", None, type=int)
    gain = json.loads(request.form.get("gain", None, type=str))
    doGain(uid, gain)
    update('update UserBuilding set objectTime = %s where uid = %s and bid = %s', (getTime(), uid, bid))
    return jsonify(dict(code=1))
    
@app.route('/initData', methods=['POST'])
def initData():
    s = queryAll('select * from strings')
    return jsonify(dict(string=s))

@app.route('/harvestSoldier', methods=['POST'])
def harvestSoldier():
    uid = request.form.get("uid", None, type=int)
    bid = request.form.get("bid", None, type=int)
    kind = request.form.get("kind", None, type=int)
    objectTime = request.form.get("time", None, type=int)
    objectList = queryOne('select objectList from UserBuilding where uid = %s and bid = %s', (uid, bid))['objectList']
    objectList = json.loads(objectList)
    objectList.pop(0)
    update('update UserBuilding set objectTime = %s, objectList = %s where uid = %s and bid = %s', (objectTime, json.dumps(objectList), uid, bid))
    update('insert into UserSoldier (uid, kind, num) values (%s, %s, %s) on duplicate key update num=num+1 ' % (uid, kind, 1))
    return jsonify(dict(code=1))

@app.route('/campAddSol', methods=['POST'])
def campAddSol():
    uid = request.form.get("uid", None, type=int)
    bid = request.form.get("bid", None, type=int)
    solId = request.form.get("solId", None, type=int)
    objectTime = request.form.get("time", None, type=int)
    cost = json.loads(request.form.get("cost", None, type=str))
    objectList = queryOne('select objectList from UserBuilding where uid = %s and bid = %s', (uid, bid))['objectList']
    objectList = json.loads(objectList)
    objectList.append(solId)
    util.doCost(uid, cost)
    update('update UserBuilding set objectTime = %s, objectList = %s where uid = %s and bid = %s', (objectTime, json.dumps(objectList), uid, bid))
    return jsonify(dict(code=1))

@app.route('/getRandomOther', methods=['POST'])
def getRandomOther():
    uid = request.form.get("uid", None, type=int)
    ret = queryOne('select max(uid) as ma, min(uid) as mi from User ')
    u = random.randint(ret["mi"], ret["ma"]) 
    print "max min", ret, u
    user = queryOne('select uid from User where uid >= %s and uid != %s limit 1', (u, uid))
    nuid = None
    if user != None:
        nuid = user["uid"]
    else:
        return jsonify(dict(code=0))

    now = int(time.time())
    builds = queryAll('select * from UserBuilding where uid = %s', (nuid))
    res = queryOne('select * from User where uid = %s', (nuid))
    soldiers = queryAll('select * from UserSoldier where uid = %s', (nuid))
    return jsonify(dict(code = 1, uid=uid, builds=builds, serverTime=now, resource=res, soldiers=soldiers))

@app.route('/synBattleRes', methods=['POST'])
def synBattleRes():
    uid = request.form.get('uid', None, type=int)
    reward = request.form.get('reward', None, type=str)
    reward = json.loads(reward)
    killedSoldier = request.form.get('killedSoldier', None, type=str)
    killedSoldier = json.loads(killedSoldier)

    util.doGain(uid, reward)
    #array [[kind, num], [kind, num]]
    for k in killedSoldier:
        update('update UserSoldier set num = num-%s where uid = %s and kind = %s', (k[1], uid, k[0]))
    return jsonify(dict(code=1))

@app.route('/rename', methods=['POST'])
def rename():
    uid = request.form.get("uid", None, type=int)
    name= request.form.get('name', None, type=str)
    update('update User set name = %s where uid = %s', (name, uid))
    return jsonify(dict(code=1))
    

if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')
