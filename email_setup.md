# Email Configuration Guide

## Setting Up Email for Contact Form

To make the contact form fully functional, you need to configure email settings. Here's how:

### 1. Gmail Setup (Recommended)

1. Go to your Google Account settings
2. Enable 2-factor authentication
3. Generate an "App Password" for your portfolio:
   - Go to Security → App passwords
   - Select "Mail" and your device
   - Copy the generated password

### 2. Environment Variables

Create a `.env` file in your project root with these settings:

```env
# Flask Configuration
SECRET_KEY=63ce89e842968154deff9687e2fc1cb6ab50ae9a4ee6b8a92

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password-here
MAIL_DEFAULT_SENDER=your-email@gmail.com

# Production Settings
FLASK_ENV=production
PORT=5000
```

### 3. Deployment Platform Configuration

For each deployment platform, add these environment variables:

**Railway/Heroku/Render:**
- `MAIL_USERNAME` = your-email@gmail.com
- `MAIL_PASSWORD` = your-app-password
- `MAIL_DEFAULT_SENDER` = your-email@gmail.com

**Vercel:**
Add to your project settings → Environment Variables

### 4. Alternative Email Providers

**Outlook/Hotmail:**
```env
MAIL_SERVER=smtp.live.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

**Yahoo:**
```env
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
```

**SendGrid (for production):**
```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USERNAME=apikey
MAIL_PASSWORD=your-sendgrid-api-key
```

### 5. Testing

1. Install dependencies: `pip install -r requirements.txt`
2. Set up your `.env` file
3. Run the app: `python run.py`
4. Test the contact form

### 6. Fallback Behavior

If email is not configured, the contact form will:
- Still accept submissions
- Log messages to console (for development)
- Show success message to user
- You can manually check the logs for messages

### 7. Security Notes

- Never commit your `.env` file to version control
- Use app passwords, not your main email password
- Consider using SendGrid or similar services for production
- The current setup sends you a notification email and an auto-reply to the sender

### 8. Troubleshooting

**Email not sending:**
- Check your app password is correct
- Verify 2FA is enabled on your Google account
- Check firewall/network settings
- Review server logs for error messages

**Gmail "Less secure app" errors:**
- Use App Passwords instead of your main password
- This is the recommended secure approach 