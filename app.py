"""
Modern Portfolio Website
A clean, responsive portfolio built with Flask
"""

from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import NotFound
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

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

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just return a success response
        
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Something went wrong. Please try again.'
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