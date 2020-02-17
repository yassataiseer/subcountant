from flask import Flask, render_template,request,session
import json
import urllib.request

import sqlite3 
  
conn = sqlite3.connect('database.db', check_same_thread=False) 
c = conn.cursor() 

key = "AIzaSyDIc87kbZUwAjuqyyKtvwCHytHAS6n_FU4"


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("name.html")

@app.route('/', methods=['POST'])
def getvalue():
    youtuber= request.form['text']
    a = youtuber.replace(" ","")
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+a+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    print(youtuber)
    print(data)
    print(subs)
    c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (youtuber, subs)) 
    conn.commit() 
    return render_template("count.html",youtuber=youtuber,subs=subs) 
    exit()

    getvalue() 
    c.close() 
    conn.close() 

    




if __name__ == '__main__':
    app.run(debug=True)

