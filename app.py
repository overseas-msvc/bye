from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bye", methods=["GET"])
def bye():
	data = request.json
	return jsonify(f"reply from endpoint bye, data = {data}")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)