from flask import Flask
import socket

app = Flask(__name__)

def get_Host_name_IP():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_ip

		
#Default dashboard
@app.route('/')
def index():
	IP = get_Host_name_IP()
	print IP
	return IP
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
