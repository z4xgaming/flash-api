from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({
        "status": "Online",
        "message": "Flash API is running successfully",
        "developer": "Commander Bhairav"
    })

@app.route('/api/player', methods=['GET'])
def get_player_data():
    player_id = request.args.get('id')
    token = request.args.get('token')
    
    if not player_id:
        return jsonify({"error": "Player ID is required"}), 400
    
    # Yahan aapka real API logic aayega jo data fetch karega
    data = {
        "status": "success",
        "account_id": player_id,
        "token_status": "Valid" if token else "Not Provided",
        "info": "Data fetching initiated..."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
