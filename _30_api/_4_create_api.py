from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/edyoda',methods=["GET","POST"])
def greet():
    data = request.args.get("naam")
    print(data)
    return jsonify({"greet":"Hello Edyoda","data":data})

app.run(debug=True)
