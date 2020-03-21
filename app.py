#!/usr/bin/python
from flask import Flask, render_template, request, g, jsonify
import sqlite3 as sql
import json

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sql.connect('database.db')

@app.route('/')
def new_student():
    con = sql.connect('database.db')
    con.execute('CREATE TABLE IF NOT EXISTS dust_data (area TEXT, level TEXT)')
    print "init............"
    return render_template('index.html')

@app.route('/api/v1/storeData',methods=['POST', 'GET'])
def storeData():
    print "inside storedata............"
    if request.method == 'POST':
        print request
        incomingData = request.data
        print incomingData
        dataDict = json.loads(incomingData)
        print dataDict

        try:
            print"try madhe ala"
            loc = dataDict['dest']
            level = dataDict['per']
            g.db.execute("INSERT INTO dust_data (area,level) VALUES(?,?)",(loc,level))
            print"store zala"
            g.db.commit()

        except ValueError, e:
            print 'Failed Pushing Data to Database'
            return False

    return jsonify(dataDict)
	
if __name__ == '__main__':
    app.run(debug=True)