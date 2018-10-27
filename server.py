from flask import Flask

app = Flask(__name__, static_url_path='C:/Users/maria/Documents/Uni/First Year/Hackathon27_10_18/BigPasta')

@app.route('/')
def hello_world():
    return app.send_static_file('index.html'), 200

app.run()
