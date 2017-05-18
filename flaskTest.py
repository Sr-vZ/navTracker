import webview
import threading
import http.server
import socketserver
from flask import Flask, render_template,request,url_for, jsonify
import pandas as pd
import os,json

'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
def startServer():
	with socketserver.TCPServer(("", PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
		
'''
db='cleanedCSV.csv'
schemes='fundDB.csv'
amfiCode='mfCode.csv'
schemeDB='./static/test.json'

def startServer():
	#app.debug=True
	app.run(host="127.0.0.1",port=8000,threaded=True)
	

app = Flask(__name__)
 
 
@app.route("/")
def hello():
	fundHouse = pd.read_csv(amfiCode)
	schemeList = pd.read_csv(schemes)
	navs = pd.read_csv(db)
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT)
	#schemedata=""#pd.read_json(schemeDB)
	#data = json.load(open(json_url))
	return render_template('app.html',fundHouse=fundHouse) #"Hello World!"

@app.route("/json",methods=['GET'])
def json():
	#df=pd.read_json('test.json')
	return open('./static/test.json').read()

@app.route('/_get_schemes')
def add_numbers():
	df = pd.read_csv(schemes)
	fund = request.args.get('f', 0, type=str)
	#b = request.args.get('b', 0, type=int)
	x=df[df['fundHouse']==fund]	
	return jsonify(result=x['fundName'].to_json(orient='records'))

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('fundHouse')
    return(str(select)) # just to see what select is


if __name__ == "__main__":
	app.debug=True
	app.run(host="127.0.0.1",port=8000)
	
    

'''
if __name__ == '__main__':
    """  https://github.com/r0x0r/pywebview/blob/master/examples/http_server.py
    """
	
    t = threading.Thread(target=startServer)
    t.daemon = True
    t.start()
 
    webview.create_window("Hi!", "http://127.0.0.1:8000/app.html")
 
    sys.exit()

	'''