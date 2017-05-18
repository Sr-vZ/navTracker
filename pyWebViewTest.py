import webview
import threading
import http.server
import socketserver
from flask import Flask, render_template
import pandas as pd

'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
def startServer():
	with socketserver.TCPServer(("", PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
		
'''
db='cleanedCSV.csv'
schemes='schemeList'
amfiCode='mfCode.csv'

def startServer():
	#app.debug=True
	app.run(host="127.0.0.1",port=8000,threaded=True)
	

app = Flask(__name__)
 
 
@app.route("/")
def hello():
	fundHouse = pd.read_csv(amfiCode)
	schemeList = pd.read_csv(schemes)
	navs = pd.read_csv(db)	
	return render_template('app.html',funds=fundHouse['FundHouse']) #"Hello World!"

if __name__ == "__main__":
	t = threading.Thread(target=startServer)
	t.daemon = True
	t.start()    
	webview.create_window("Hi!", "http://127.0.0.1:8000/")	
	sys.exit()
	
    

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