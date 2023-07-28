from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/api/encode', methods=['POST'])
def convert_to_base64():
    data = request.get_json(force=True)
    input_data = data.get('input')

    if not input_data:
        return jsonify({'error': 'No input data provided'}), 400

    # Convert to bytes and encode
    encoded = base64.b64encode(input_data.encode()).decode()

    return jsonify({'encoded': encoded}), 200

@app.route('/api/decode', methods=['POST'])
def convert_from_base64():
    data = request.get_json(force=True)
    input_data = data.get('input')

    if not input_data:
        return jsonify({'error': 'No input data provided'}), 400

    # Decode from base64
    decoded = base64.b64decode(input_data).decode()

    return jsonify({'decoded': decoded}), 200

if __name__ == "__main__":
    app.run(debug=True)
