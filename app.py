import os
import json
from flask import Flask, render_template, request, jsonify
from utils.helpers import calculate_root_number, get_zodiac_sign, calculate_destiny_number
from datetime import datetime
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

def load_crystal_data():
    data = {}
    data_files = [
        'zodiac_crystals.json',
        'numerology_crystals.json',
        'intention_crystals.json',
        'crystal_details.json'
    ]
    
    for file in data_files:
        file_path = os.path.join('data', file)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data[file.replace('.json', '')] = json.load(f)
    
    # Load personality mapping
    personality_file = os.path.join('data', 'personality_mapping.json')
    if os.path.exists(personality_file):
        with open(personality_file, 'r') as f:
            data['personality_mapping'] = json.load(f)
    
    return data

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;"
    return response

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            dob = request.form.get('dob')
            intention = request.form.get('intention')

            if not all([name, dob, intention]):
                return jsonify({'Error': 'All fields are required'}), 400

            # Validate date format
            try:
                birth_date = datetime.strptime(dob, '%Y-%m-%d')
                if birth_date > datetime.now():
                    return jsonify({'Error': 'Date of birth cannot be in the future'}), 400
            except ValueError:
                return jsonify({'Error': 'Invalid date format'}), 400

            crystal_data = load_crystal_data()
            intention_crystals = crystal_data.get('intention_crystals', {}).get(intention, [])
            if dob:
                root_number = calculate_root_number(dob)
                zodiac_sign = get_zodiac_sign(dob)
                destiny_number = calculate_destiny_number(dob)
                
                # Get crystal recommendations based on zodiac sign
                zodiac_crystals = crystal_data.get('zodiac_crystals', {}).get(zodiac_sign, [])
                
                # Get crystal recommendations based on root number
                numerology_crystals = crystal_data.get('numerology_crystals', {}).get(str(root_number), [])
                
                # Get crystal recommendations based on destiny number
                destiny_crystals = crystal_data.get('numerology_crystals', {}).get(str(destiny_number), [])
                
                # Get personality insights and crystals based on root and destiny numbers
                personality_key = f"{root_number},{destiny_number}"
                personality_data = crystal_data.get('personality_mapping', {}).get(personality_key, {})
                
                recommendations = {
                    'Name': name,
                    'Zodiac Sign': zodiac_sign,
                    'Root Number': root_number,
                    'Destiny Number': destiny_number,
                    'Intention': intention,
                    'Zodiac Crystals': zodiac_crystals,
                    'Numerology Crystals': numerology_crystals,
                    'Destiny Crystals': destiny_crystals,
                    'Intention Crystals': intention_crystals,
                    'Personality': personality_data.get('personality', 'No specific personality traits available for this combination.'),
                    'Personality Crystals': personality_data.get('crystals', [])
                }

            return render_template('index.html', recommendations=recommendations, crystal_details=crystal_data.get('crystal_details', {}))
        except Exception as e:
            app.logger.error(f"Error processing request: {str(e)}")
            return jsonify({'Error': 'An error occurred while processing your request'}), 500

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug) 