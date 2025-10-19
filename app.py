"""
Modern Portfolio Website
A clean, responsive portfolio built with Flask
"""

from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message
from werkzeug.exceptions import NotFound
import os
import re
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch',
    'ar': 'العربية'
}

# Load translations
TRANSLATIONS = {}
for lang_code in LANGUAGES.keys():
    try:
        with open(f'translations/{lang_code}.json', 'r', encoding='utf-8') as f:
            TRANSLATIONS[lang_code] = json.load(f)
    except FileNotFoundError:
        print(f"Warning: Translation file for {lang_code} not found")
    except json.JSONDecodeError as e:
        print(f"Error loading translation file for {lang_code}: {e}")

def get_locale():
    """Get the current locale from session or default to English"""
    return session.get('lang', 'en')

def get_translation(key_path, default=''):
    """
    Get translation for a given key path (e.g., 'nav.home')
    Returns the translation in the current language or the default value
    """
    lang = get_locale()
    if lang not in TRANSLATIONS:
        lang = 'en'
    
    keys = key_path.split('.')
    value = TRANSLATIONS.get(lang, {})
    
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key, default)
        else:
            return default
    
    return value if value else default

# Make translation function available in templates
@app.context_processor
def inject_i18n():
    """Inject translation functions and language info into templates"""
    return {
        'get_locale': get_locale,
        't': get_translation,
        'languages': LANGUAGES,
        'current_year': datetime.now().year
    }

# Mail configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', os.getenv('MAIL_USERNAME'))

# Initialize Flask-Mail
mail = Mail(app)

# Portfolio data
def get_portfolio_data():
    """Get portfolio data with translations"""
    lang = get_locale()
    translations = TRANSLATIONS.get(lang, TRANSLATIONS.get('en', {}))
    profile = translations.get('profile', {})
    
    portfolio_data = {
        'name': profile.get('name', 'Aziz Guebsi'),
        'title': profile.get('title', 'Software Engineer & Full Stack Developer'),
        'bio': profile.get('bio', 'Passionate software engineer specializing in microservices architecture, digital security solutions, and modern web technologies.'),
        'email': 'gabsiaziz37@gmail.com',
        'github': 'https://github.com/AMG2ks',
        'linkedin': 'https://www.linkedin.com/in/aziz-guebsi/',
        'location': profile.get('location', 'Tunis, Tunisia'),
        'skills': [
        'Python',
        'Django',
        'Angular',
        'JavaScript',
        'TypeScript',
        'React',
        'Streamlit',
        'PostgreSQL',
        'Docker',
        'RabbitMQ',
        'HTML/CSS',
        'Git',
        'Three.js',
        'Tailwind CSS',
        'Flask',
        'Redis',
        'Celery',
        'Azure',
        'WebSocket',
        'Keycloak'
        ],
        'projects': [
            {
                'id': 4,
                'title': translations.get('projects_data', [{}])[0].get('title', 'Skrow - Freelance Marketplace'),
                'description': translations.get('projects_data', [{}])[0].get('description', ''),
                'technologies': ['Django', 'React', 'PostgreSQL', 'Docker', 'Azure', 'Celery', 'Redis', 'WebSocket'],
                'live_url': 'https://skrow.switzerlandnorth.cloudapp.azure.com',
                'image': 'skrow1.png'
            },
            {
                'id': 1,
                'title': translations.get('projects_data', [{}, {}])[1].get('title', 'IoT Device Monitoring Dashboard') if len(translations.get('projects_data', [])) > 1 else 'IoT Device Monitoring Dashboard',
                'description': translations.get('projects_data', [{}, {}])[1].get('description', '') if len(translations.get('projects_data', [])) > 1 else '',
                'technologies': ['Django', 'Angular', 'ChartJS', 'PostgreSQL'],
                'github_url': 'https://github.com/DigiSmartSolutions',
                'live_url': '#',
                'image': 'iot.jpg'
            },
            {
                'id': 2,
                'title': translations.get('projects_data', [{}, {}, {}])[2].get('title', 'BerrySign Digital Signature Platform') if len(translations.get('projects_data', [])) > 2 else 'BerrySign Digital Signature Platform',
                'description': translations.get('projects_data', [{}, {}, {}])[2].get('description', '') if len(translations.get('projects_data', [])) > 2 else '',
                'technologies': ['Django', 'Angular', 'RabbitMQ', 'Docker'],
                'github_url': 'https://github.com/',
                'live_url': '#',
                'image': 'requests.png'
            },
            {
                'id': 3,
                'title': translations.get('projects_data', [{}, {}, {}, {}])[3].get('title', 'Smart Budget Manager') if len(translations.get('projects_data', [])) > 3 else 'Smart Budget Manager',
                'description': translations.get('projects_data', [{}, {}, {}, {}])[3].get('description', '') if len(translations.get('projects_data', [])) > 3 else '',
                'technologies': ['Python', 'Streamlit', 'SQLite', 'PostgreSQL'],
                'github_url': 'https://github.com/AMG2ks/budget_manager',
                'live_url': 'https://budgetmanager.streamlit.app',
                'image': 'budget_manager.png'
            },
        ],
        'experience': []
    }
    
    # Add translated experience data
    exp_data = translations.get('experience_data', [])
    for i, exp in enumerate(exp_data):
        portfolio_data['experience'].append({
            'company': exp.get('company', ''),
            'position': exp.get('position', ''),
            'period': exp.get('period', ''),
            'description': exp.get('description', ''),
            'achievements': exp.get('achievements', [])
        })
    
    return portfolio_data

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html', data=get_portfolio_data())

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    """Set the language preference"""
    if lang_code in LANGUAGES:
        session['lang'] = lang_code
    return jsonify({'status': 'success', 'language': lang_code})

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_contact_email(name, email, message):
    """Send contact form email"""
    try:
        portfolio_data = get_portfolio_data()
        # Email to yourself (notification)
        notification_msg = Message(
            subject=f'New Portfolio Contact: {name}',
            recipients=[portfolio_data['email']],
            body=f"""
You have received a new message from your portfolio website:

Name: {name}
Email: {email}

Message:
{message}

---
Sent from your portfolio contact form
            """.strip()
        )
        
        # Auto-reply to the sender
        auto_reply_msg = Message(
            subject='Thanks for contacting me!',
            recipients=[email],
            body=f"""
Hi {name},

Thank you for reaching out! I've received your message and will get back to you as soon as possible.

Here's a copy of your message:
"{message}"

Best regards,
{portfolio_data['name']}

---
This is an automated response from {portfolio_data['name']}'s portfolio website.
            """.strip()
        )
        
        # Send both emails
        mail.send(notification_msg)
        mail.send(auto_reply_msg)
        
        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No data received.'
            }), 400
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Validate required fields
        if not name:
            return jsonify({
                'status': 'error',
                'message': 'Name is required.'
            }), 400
            
        if not email:
            return jsonify({
                'status': 'error',
                'message': 'Email is required.'
            }), 400
            
        if not message:
            return jsonify({
                'status': 'error',
                'message': 'Message is required.'
            }), 400
        
        # Validate email format
        if not validate_email(email):
            return jsonify({
                'status': 'error',
                'message': 'Please enter a valid email address.'
            }), 400
        
        # Validate message length
        if len(message) < 10:
            return jsonify({
                'status': 'error',
                'message': 'Message must be at least 10 characters long.'
            }), 400
            
        if len(message) > 1000:
            return jsonify({
                'status': 'error',
                'message': 'Message must be less than 1000 characters.'
            }), 400
        
        # Check if email is configured
        if not app.config.get('MAIL_USERNAME'):
            # Fallback: just log the message (for development/demo)
            print(f"Contact form submission from {name} ({email}): {message}")
            return jsonify({
                'status': 'success',
                'message': 'Thank you for your message! I\'ll get back to you soon. (Email not configured - message logged for demo purposes)'
            })
        
        # Try to send email
        if send_contact_email(name, email, message):
            return jsonify({
                'status': 'success',
                'message': 'Thank you for your message! I\'ve received it and will get back to you soon. Check your email for a confirmation.'
            })
        else:
            # Fallback if email fails
            print(f"Email failed, logging message from {name} ({email}): {message}")
            return jsonify({
                'status': 'success',
                'message': 'Thank you for your message! I\'ve received it and will get back to you soon.'
            })
            
    except Exception as e:
        print(f"Contact form error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Something went wrong. Please try again or contact me directly.'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('FLASK_ENV', 'production') == 'development'
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port) 