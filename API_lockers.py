from flask import Flask

app = Flask(__name__)

data = {111111 : {"lockers": [1,2]},
        222222 : {"lockers": [2,3]}}

@app.route("/")
def home():
    return "Smart Lock Project", 200

@app.route("/<int:id>/<int:locker>", methods=['GET'])
def authorise_check(id, locker):
    if (id not in data):
        return "<h1>404</h1><p>Student not found.</p>", 404
    elif(locker not in data[id]["lockers"]):
        return "<h1>400</h1><p>Student not authorized.</p>", 400
    else:
        return "<h1>200</h1><p>Student authorized</p>", 200

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(debug=True)