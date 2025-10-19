"""
Modern Portfolio Website
A clean, responsive portfolio built with Flask
"""

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from werkzeug.exceptions import NotFound
import os
import re
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

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

# Add current year to template context
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

# Portfolio data
PORTFOLIO_DATA = {
    'name': 'Aziz Guebsi',
    'title': 'Software Engineer & Full Stack Developer',
    'bio': 'Passionate software engineer specializing in microservices architecture, digital security solutions, and modern web technologies. Experienced in building scalable applications with Django, Angular, and cloud-native technologies.',
    'email': 'gabsiaziz37@gmail.com',
    'github': 'https://github.com/AMG2ks',
    'linkedin': 'https://www.linkedin.com/in/aziz-guebsi/',
    'location': 'Tunis, Tunisia',
    'skills': [
        {'name': 'Python', 'level': 90},
        {'name': 'Django', 'level': 90},
        {'name': 'Angular', 'level': 85},
        {'name': 'JavaScript', 'level': 85},
        {'name': 'TypeScript', 'level': 80},
        {'name': 'React JS', 'level': 80},
        {'name': 'Streamlit', 'level': 85},
        {'name': 'PostgreSQL', 'level': 85},
        {'name': 'Docker', 'level': 80},
        {'name': 'RabbitMQ', 'level': 75},
        {'name': 'HTML/CSS', 'level': 90},
        {'name': 'Git', 'level': 85},
        {'name': 'Three JS', 'level': 70},
        {'name': 'Tailwind CSS', 'level': 75}
    ],
    'projects': [
        {
            'id': 1,
            'title': 'IoT Device Monitoring Dashboard',
            'description': 'Web-based platform for monitoring IoT devices with real-time data visualization and analytics, providing comprehensive insights into device performance and status.',
            'technologies': ['Django', 'Angular', 'ChartJS', 'PostgreSQL'],
            'github_url': 'https://github.com/DigiSmartSolutions',
            'live_url': '#',
            'image': 'iot-dashboard.jpg'
        },
        {
            'id': 2,
            'title': 'BerrySign Digital Signature Platform',
            'description': 'BerrySign is a secure digital signature platform that allows users to sign documents electronically, streamlining the document signing process and reducing paper waste with microservice architecture.',
            'technologies': ['Django', 'Angular', 'RabbitMQ', 'Docker'],
            'github_url': 'https://github.com/',
            'live_url': '#',
            'image': 'berrysign.jpg'
        },
        {
            'id': 3,
            'title': 'Smart Budget Manager',
            'description': 'A comprehensive financial management application with intelligent budget tracking, expense monitoring, and savings goals. Features multi-user support, automated backups, and supports 21 international currencies with beautiful dashboard analytics.',
            'technologies': ['Python', 'Streamlit', 'SQLite', 'PostgreSQL'],
            'github_url': 'https://github.com/AMG2ks/budget_manager',
            'live_url': 'https://budgetmanager.streamlit.app',
            'image': 'budget-manager.png'
        },
        {
            'id': 4,
            'title': 'Skrow - Freelance Marketplace',
            'description': 'Skrow is a modern, full-featured freelance marketplace platform designed specifically for the Tunisian market, connecting local freelancers with clients both domestically and internationally. The platform bridges the gap between skilled Tunisian professionals and businesses seeking quality services, while supporting the local economy and digital transformation.',
            'technologies': ['Django', 'React', 'PostgreSQL', 'Docker', 'Azure', 'Celery', 'Redis', 'WebSocket'],
            'live_url': 'https://skrow.switzerlandnorth.cloudapp.azure.com',
            'image': 'skrow1.png'
        },
    ],
    'experience': [
        {
            'company': 'Digitalberry',
            'position': 'Software Engineer',
            'period': 'July 2023 - Present',
            'description': 'Developing and securing microservices with advanced authentication systems and certificate management.',
            'achievements': [
                'Developing and Securing Microservices – Design, implement, and optimize secure microservices architectures, ensuring seamless integration with authentication systems like Keycloak',
                'Certificate and Token Management – Work on BerryCert and the new token management platform, handling TLS credentials, YubiKey, and SafeNet integrations',
                'Performance Optimization & Automation – Enhance system performance by optimizing API calls, implementing multi-threading, and automating key workflows for improved efficiency'
            ]
        },
        {
            'company': 'Digitalberry',
            'position': 'Full Stack Developer - Intern',
            'period': 'February 2023 - May 2023',
            'description': 'Built comprehensive digital signature platform with microservice architecture.',
            'achievements': [
                'Building a Digital-Signature platform using Django, Angular, and RabbitMQ',
                'Collaborating with cross-functional teams including designers, product managers, and other developers to create high-quality products',
                'Implementing a microservice architecture using Docker',
                'Implementing a real-time notification system using RabbitMQ'
            ]
        },
        {
            'company': 'Digi Smart Solutions',
            'position': 'Django Angular Developer - Intern',
            'period': 'June 2022 - September 2022',
            'description': 'Developed and maintained web applications using Django and Angular technologies.',
            'achievements': [
                'Developing and maintaining web applications using Django and other related technologies',
                'Building user interfaces using Angular and other front-end technologies',
                'Building RESTful APIs and integrating third-party services',
                'Creating and maintaining documentation for projects'
            ]
        }
    ]
}

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html', data=PORTFOLIO_DATA)

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_contact_email(name, email, message):
    """Send contact form email"""
    try:
        # Email to yourself (notification)
        notification_msg = Message(
            subject=f'New Portfolio Contact: {name}',
            recipients=[PORTFOLIO_DATA['email']],
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
{PORTFOLIO_DATA['name']}

---
This is an automated response from {PORTFOLIO_DATA['name']}'s portfolio website.
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