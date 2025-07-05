# Modern Portfolio Website

A beautiful, responsive portfolio website built with Flask and modern web technologies. Features a clean design, smooth animations, and mobile-first responsive layout.

## Features

- **Modern Design**: Clean, professional UI with smooth animations and transitions
- **Responsive Layout**: Mobile-first design that works on all devices
- **Interactive Elements**: Smooth scrolling, animated skill bars, and form validation
- **SEO Optimized**: Proper meta tags, semantic HTML, and structured data
- **Performance Optimized**: Lazy loading, optimized assets, and efficient code
- **Contact Form**: Functional contact form with email notifications and validation
- **Error Pages**: Custom 404 and 500 error pages

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)
- **Animations**: CSS animations and transitions

## Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main portfolio page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
└── README.md             # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```
   - Update the portfolio data in `app.py`

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open in browser**:
   Visit `http://localhost:5000`

## Customization

### Portfolio Data

Update the `PORTFOLIO_DATA` dictionary in `app.py` with your information:

```python
PORTFOLIO_DATA = {
    'name': 'Your Name',
    'title': 'Your Title',
    'bio': 'Your bio description',
    'email': 'your.email@example.com',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'location': 'Your City, Country',
    'skills': [
        {'name': 'Python', 'level': 90},
        # Add more skills
    ],
    'projects': [
        {
            'title': 'Project Name',
            'description': 'Project description',
            'technologies': ['Python', 'Flask'],
            'github_url': 'https://github.com/user/project',
            'live_url': 'https://project.com'
        },
        # Add more projects
    ],
    'experience': [
        {
            'company': 'Company Name',
            'position': 'Position',
            'period': '2020 - Present',
            'description': 'Job description',
            'achievements': ['Achievement 1', 'Achievement 2']
        },
        # Add more experience
    ]
}
```

### Styling

Customize the design by modifying CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    /* Modify colors to match your brand */
}
```

### Email Configuration

To enable the contact form to send emails:

1. **Gmail Setup** (Recommended):
   - Enable 2-factor authentication on your Google account
   - Generate an App Password: Account Settings → Security → App passwords
   - Use the app password in your `.env` file

2. **Environment Variables**:
   ```env
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

3. **Alternative Email Providers**:
   - **Outlook**: `smtp.live.com:587`
   - **Yahoo**: `smtp.mail.yahoo.com:587`
   - **SendGrid**: `smtp.sendgrid.net:587` (for production)

4. **Contact Form Features**:
   - Sends notification email to you when someone contacts you
   - Sends auto-reply confirmation to the sender
   - Includes form validation and error handling
   - Works without email configuration (logs messages for demo)

**Note**: See `email_setup.md` for detailed configuration instructions.

## Deployment

### Heroku

1. **Create Heroku app**:
   ```bash
   heroku create your-portfolio-name
   ```

2. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set FLASK_ENV=production
   ```

3. **Deploy**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

### Vercel

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

### Traditional Hosting

1. **Set up production environment**:
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

2. **Use Gunicorn**:
   ```bash
   gunicorn app:app
   ```

## Performance Optimization

- **Images**: Add optimized images to `static/images/`
- **Caching**: Implement caching for static assets
- **Compression**: Use gzip compression
- **CDN**: Consider using a CDN for static assets
- **Database**: Add database for dynamic content if needed

## Security

- Generate a strong `SECRET_KEY` for production
- Use HTTPS in production
- Implement rate limiting for contact form
- Validate and sanitize all user inputs
- Keep dependencies updated

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need help with setup, please open an issue or contact me directly.

---

**Note**: Remember to update all placeholder content with your actual information before deploying to production. 