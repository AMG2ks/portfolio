#!/usr/bin/env python3
"""
Portfolio Website Runner
Simple script to run the Flask application with proper configuration
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Set environment variables if not already set
    if not os.getenv('SECRET_KEY'):
        os.environ['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Check if we're in production
    is_production = os.getenv('FLASK_ENV') == 'production'
    
    if is_production:
        print("Running in production mode")
        # Use Gunicorn for production
        port = int(os.getenv('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        print("Running in development mode")
        print("Visit: http://localhost:5000")
        app.run(debug=True, host='0.0.0.0', port=5000) 