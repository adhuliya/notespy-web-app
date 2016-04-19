#!/usr/bin/env python3

import sqlite_driver as sqd
import bottle as bt
import alibrary as alib


dbfile = "notes.sqlite3.db"
sq = None    #stores the sqlite cursor after initialize() is called
queries = None    #stores the queries read from queries.sql.py
sessions = dict()

@bt.route("/", method="get")
def index():
    print ("value =", bt.request.query.absc)
    failed = bt.request.query.failed or False
    
    return bt.template('login',failed=failed)


@bt.route("/login", method="post")
def login2():
    session = alib.getsession(bt.request, sessions)

    if session: bt.redirect('/homepage')

    uid = bt.request.forms.get("uid")
    pwd = bt.request.forms.get("pwd")

    #formdata = getformdata('uid','pwd')

    #logininfo = getlogininfo(uid=formdata['uid'], pwd=formdata['pwd'])
    loginid = sq.execute('query0003s', (uid, pwd))


    print(loginid)
    if loginid:
        uniqueid = alib.randomstring()
        while uniqueid in sessions:
            uniqueid = alib.randomstring()
        sessions[uniqueid] = {'id':loginid[0][0], 'name':loginid[0][1]}

        bt.response.set_cookie('sessionid', uniqueid)
        bt.redirect("/homepage")
    else:
        bt.redirect("/?failed=true")

@bt.route("/homepage")
def homepage():
    session = alib.getsession(bt.request, sessions)
    if session: 
        return bt.template("Welcome {{name}}!", name=session['name'])

    bt.redirect("/")

@bt.route("/logout")
def logout():
    sessionid = bt.request.get_cookie('sessionid', None)
    if sessionid and sessionid in sessions: 
        name = sessions[sessionid]['name']
        del sessions[sessionid]
        bt.response.delete_cookie('sessionid')
        return bt.template("Bye {{name}}!", name=name)

    bt.redirect("/")

def initialize():
    global sq, dbfile
    sq = sqd.Sqlite3(dbfile=dbfile)


if __name__ == "__main__":
    initialize()
    bt.run(host="0.0.0.0", port=8000, debug=True)


