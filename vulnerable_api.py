from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Unrestricted Resource Consumption (Schlechte Limitierung bei Ressourcenverbrauch)
@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    # Berechnet die Fakultät einer Zahl ohne Begrenzung
    if num < 0:
        return jsonify({"error": "Negative numbers are not allowed"}), 400
    result = 1
    for i in range(1, num + 1):
        result *= i
    return jsonify({"number": num, "factorial": result})

# Server-Side Request Forgery (SSRF)
@app.route('/fetch_url', methods=['POST'])
def fetch_url():
    # Akzeptiert eine beliebige URL und sendet einen Server-Request
    data = request.get_json()
    url = data.get("url")
    try:
        response = requests.get(url)
        return jsonify({"status": response.status_code, "content": response.text[:500]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Security Misconfiguration (Debug-Modus aktiviert)
@app.route('/debug', methods=['GET'])
def debug():
    # Debugging-Endpunkt, der sensible Konfigurationsdaten preisgibt
    return jsonify({
        "debug": True,
        "database_url": "postgresql://user:password@localhost/db",
        "api_key": "supersecretapikey123"
    })

# Unsafe Consumption of APIs (Ungeprüfte JSON-Daten)
@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    # Erwartet ein JSON-Objekt mit zwei Zahlen, prüft die Eingabe jedoch nicht
    data = request.get_json()
    num1 = data["num1"]
    num2 = data["num2"]
    return jsonify({"result": num1 + num2})

if __name__ == '__main__':
    # Debug-Modus aktiviert (Security Misconfiguration)
    app.run(debug=True, host='0.0.0.0', port=5000)
