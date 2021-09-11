from flask import Flask, json, request, jsonify
from marshmallow import schema, ValidationError
from .types import SearchTextInput
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/search/text/', methods=['POST'])
def search_text():
    schema = SearchTextInput()
    data = request.json

    try:
        data = schema.load(data)
        position = data["position"]

        df = pd.read_csv("csv_files/{}".format(data["file_name"]),)

        # Filtering reactangles lying in Position cordinates, sort by x0 for natural reading flow
        result = df.loc[
            (df["x0"] <= position[0]) &
            (df["y0"] <= position[1]) &
            (df["x2"] >= position[2]) &
            (df["y2"] >= position[3])
        ].sort_values(["y2", "x0"], ascending=[False, True])

        text = result["Text"].str.cat(sep=" ")

        return jsonify({"text": text})

    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    except FileNotFoundError as err:
        return jsonify({"error": "File not found"}), 405


if __name__ == "__main__":
    app.run()
