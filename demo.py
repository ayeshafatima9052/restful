from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/test",methods=["GET", "POST"])
def test():
   if request.method == "GET":
      return jsonify({"response": "Hello"})
   elif request.method == "POST":
      req_Json = request.json
      name = req_Json["name"]
      return jsonify({"response": "Hope You Are Doing Well "   +     name})


if __name__ =="__main__":
    app.run(debug=True)



