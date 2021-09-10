from flask import Flask, request, jsonify


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/search/text/', methods=['POST'])
async def search_text():
    data = request.json
    return jsonify(data)

app.run()
