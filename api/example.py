from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'field1': 'value1',
        'field2': True
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
