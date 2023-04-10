from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/search/<user>")
def search(user):
    server_ip = socket.gethostbyname(socket.gethostname())

    message = {
        "user": user,
        "ip": server_ip
    }

    with open('results/output.txt', 'a') as f:
        log = f"{user},{server_ip} \n"
        f.write(log)
        f.close()

    return message
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

#docker-compose up --scale load-balancer-app=4  -d