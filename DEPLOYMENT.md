# Portfolio Deployment Guide

This guide covers multiple deployment options for your Flask portfolio website.

## 🚀 Quick Deployment Options

### Option 1: Railway (Recommended - Easy & Free)

**Why Railway?**
- ✅ Free tier available
- ✅ Automatic deployments from GitHub
- ✅ Built-in database support
- ✅ Easy setup

**Steps:**
1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Portfolio ready for deployment"
   git push origin main
   ```

2. **Deploy to Railway**:
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your portfolio repository
   - Railway automatically detects it's a Python app
   - Your app will be live in ~2 minutes!

3. **Custom Domain** (Optional):
   - Go to your project settings
   - Add a custom domain or use the provided railway.app subdomain

---

### Option 2: Vercel (Great for Frontend)

**Steps:**
1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```
   - Follow the prompts
   - Vercel will automatically detect your Flask app

3. **Custom Domain**:
   - Add domains in Vercel dashboard

---

### Option 3: Render (Reliable & Free Tier)

**Steps:**
1. **Push to GitHub** (if not done)

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Environment**: Python 3

3. **Environment Variables**:
   - Set `FLASK_ENV=production`
   - Set `SECRET_KEY=your-production-secret-key`

---

### Option 4: Heroku (Traditional Choice)

**Steps:**
1. **Install Heroku CLI**:
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Ubuntu/Debian
   sudo snap install --classic heroku
   ```

2. **Login and Create App**:
   ```bash
   heroku login
   heroku create your-portfolio-name
   ```

3. **Set Environment Variables**:
   ```bash
   heroku config:set SECRET_KEY=your-production-secret-key
   heroku config:set FLASK_ENV=production
   ```

4. **Deploy**:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

5. **Open Your App**:
   ```bash
   heroku open
   ```

---

### Option 5: DigitalOcean App Platform (Production-Grade)

**Steps:**
1. **Push to GitHub** (if not done)

2. **Create App on DigitalOcean**:
   - Go to [cloud.digitalocean.com](https://cloud.digitalocean.com)
   - Create new "App"
   - Connect GitHub repository
   - Configure:
     - **Source Directory**: `/`
     - **Build Command**: `pip install -r requirements.txt`
     - **Run Command**: `gunicorn app:app`

3. **Environment Variables**:
   - Add `FLASK_ENV=production`
   - Add `SECRET_KEY=your-production-secret-key`

---

## 🔧 Pre-Deployment Checklist

### ✅ Required Files (Already Created)
- [x] `requirements.txt` - Python dependencies
- [x] `Procfile` - For Heroku/Railway
- [x] `vercel.json` - For Vercel
- [x] `runtime.txt` - Python version
- [x] `wsgi.py` - WSGI entry point

### ✅ Environment Variables to Set
- `SECRET_KEY` - Generate a secure secret key
- `FLASK_ENV=production` - Disable debug mode

### ✅ Generate Secret Key
```python
# Run this in Python terminal to generate a secure secret key
import secrets
print(secrets.token_hex(16))
```

---

## 🌐 Custom Domain Setup

After deployment, you can add a custom domain:

1. **Buy a domain** (Namecheap, GoDaddy, etc.)
2. **DNS Configuration**:
   - For Railway: Add CNAME record pointing to your railway app
   - For Vercel: Add CNAME record to `cname.vercel-dns.com`
   - For Heroku: Add CNAME record to your heroku app URL
3. **SSL Certificate**: Most platforms provide automatic HTTPS

---

## 📊 Performance Optimization

### For Production:
1. **Enable Gzip Compression**:
   ```python
   # Add to app.py
   from flask_compress import Compress
   Compress(app)
   ```

2. **Add Caching Headers**:
   ```python
   # Add to app.py
   @app.after_request
   def after_request(response):
       response.headers["Cache-Control"] = "public, max-age=300"
       return response
   ```

3. **Minify CSS/JS** (Optional):
   - Use build tools to minify static assets

---

## 🐛 Troubleshooting

### Common Issues:

1. **App Won't Start**:
   - Check logs: `heroku logs --tail` (for Heroku)
   - Verify all dependencies in requirements.txt

2. **Static Files Not Loading**:
   - Ensure static files are in the correct directory
   - Check if platform serves static files automatically

3. **Environment Variables**:
   - Verify SECRET_KEY is set
   - Check FLASK_ENV is set to 'production'

### Debug Commands:
```bash
# Check app status
heroku ps:scale web=1  # For Heroku

# View logs
heroku logs --tail     # For Heroku
vercel logs           # For Vercel
```

---

## 🚀 Recommended: Railway Quick Start

For the easiest deployment, I recommend **Railway**:

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app)
3. Connect GitHub and select your repo
4. Wait 2 minutes - your portfolio is live!

---

## 📧 Need Help?

If you encounter any issues during deployment:
1. Check the platform-specific documentation
2. Review application logs
3. Ensure all environment variables are set correctly

Your portfolio is now ready for the world! 🌟 