from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [{
	id: 1,
	"title": "Buy Groceries",
	"description": "ABC",
	"done": False
},
{
	id: 2,
	"title": "Do Homework",
	"description": "DEF",
	"done": True
}]

@app.route("/add-data", methods=["POST"])
def add_data():
	if not request.json:
		return jsonify({
			"status": "ERROR",
			"msg": "Pls provide the data"
			}, 400)
	else:
		contact = {
		id: tasks[-1]["id"]+1,
		"Name": request.json["Name"],
		"contact": request.json.get("contact", ""),
		"done": False
		}
	tasks.append(contact)
	return jsonify({
			"status": "SUCCESS",
			"msg": "Task added successfully"
			}, 200)

@app.route("/get-data")
def get_tasks():
	return jsonify({
		"data": tasks
		})


if __name__ == "__main__":
	app.run()