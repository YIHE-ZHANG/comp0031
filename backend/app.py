from flask import Flask, request, jsonify
from parser31 import parse_to_latex  # Import your parse_to_latex function

app = Flask(__name__)

@app.route('/generate_latex', methods=['POST'])
def generate_latex():
    data = request.json
    B = data['B']
    premises = data['premises']
    gamma = data['gamma']
    latex_string = parse_to_latex(B, premises, gamma)
    return jsonify({'latex': latex_string})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
