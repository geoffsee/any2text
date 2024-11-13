from flask import Flask, request, jsonify
from extractous import Extractor
import os

app = Flask(__name__)
extractor = Extractor()


@app.route("/extract", methods=["POST"])
def extract_text():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Save the file temporarily
        temp_path = os.path.join("/tmp", file.filename)
        file.save(temp_path)

        # Extract text from the file
        result = extractor.extract_file_to_string(temp_path)

        # Clean up the temp file
        os.remove(temp_path)

        return jsonify({"text": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False, port=5006, host="0.0.0.0")
