"""
WSGI Entry Point for Production Deployment
"""

from app import app

if __name__ == "__main__":
    app.run() 