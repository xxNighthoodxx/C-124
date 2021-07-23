from flask import Flask, request, jsonify

app = Flask(__name__)

contact = {
	'id': 1,
	'Name': request.json['Name'],
	'Contact': request.json.get('Contact', ""),
	'done':False
}