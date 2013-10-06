#coding:utf8
from flask import Flask, g, abort, session, redirect, url_for, \
     request, render_template, _app_ctx_stack, jsonify
from flaskext import *
import json
import time
from util import *

app = Flask(__name__)
app.config.from_object("config")

@app.route('/login', methods=['POST'])
def login():
    account = request.form.get('account', None, type=str)
    user = queryOne('select uid from User where account = %s', account)
    now = int(time.time())
    if user == None:
        uid = insertAndGetId('insert into User (account) values (%s)', (account))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 0, 200, 1500, 300, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 1, 202, 1200, 300, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 2, 0, 1700, 250, now))
        update('insert into UserBuilding (uid, bid, kind, px, py, objectTime) values (%s, %s, %s, %s, %s, %s)', (uid, 3, 300, 1300, 100, now))
    else:
        uid = user["uid"]
    builds = queryAll('select * from UserBuilding where uid = %s', (uid))
    res = queryOne('select * from User where uid = %s', (uid))
    return jsonify(dict(uid=uid, builds=builds, serverTime=now, resource=res))

@app.route('/harvestPlant', methods=['POST'])
def harvestPlant():
    uid = request.form.get("uid", None, type=int)
    bid = request.form.get("bid", None, type=int)
    gain = request.form.get("gain", None, type=str)
    gain = json.loads(gain)
    doGain(uid, gain)
    now = getTime()
    update('update UserBuilding set objectTime = %s where uid = %s and bid = %s', (now, uid, bid))
    return jsonify(dict(code=1))

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
    
    


if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')
