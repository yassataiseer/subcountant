from flask import Flask, render_template,request,session
import json
import urllib.request

key = "AIzaSyDIc87kbZUwAjuqyyKtvwCHytHAS6n_FU4"


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("name.html")



@app.route('/', methods=['POST'])
def getvalue():
    youtuber= request.form['text']
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+youtuber+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    print(youtuber)
    print(data)
    print(subs)
    return render_template("count.html",youtuber=youtuber,subs=subs)  

if __name__ == '__main__':
    app.run(debug=True)

