from flask import Flask,jsonify,render_template,request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

speed = 0

@app.route("/get_speed")
def get_speed():
    data = {"speed":speed}
    return jsonify(data)

# @Dayton
@app.route("/set_speed", methods=['GET', 'POST'])
def set_speed():
    current_speed = request.form['speed']
    global speed
    speed = int(current_speed)
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True,
            port=80,
            host='0.0.0.0',
            threaded=True
    ) 
