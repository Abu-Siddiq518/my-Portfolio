# 🔐 Abubakkar Siddiq - Cybersecurity Portfolio

A dynamic, cybersecurity-themed portfolio built with Python Flask featuring:
- Matrix rain background animation
- Glitch text effects & cursor trails
- Admin panel to manage all content
- Fully responsive design

---

## 🚀 QUICK SETUP

### 1. Install Python (if not installed)
Download from: https://www.python.org/downloads/

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the portfolio
```bash
python app.py
```

### 4. Open in browser
- **Portfolio:** http://localhost:5000
- **Admin Panel:** http://localhost:5000/admin/login

---

## 🔑 ADMIN ACCESS
- **URL:** http://localhost:5000/admin/login
- **Password:** `Siddiq`

---

## 📁 PROJECT STRUCTURE
```
portfolio/
├── app.py                 # Main Flask application
├── data.json              # Auto-generated data file
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html         # Main portfolio page
│   ├── admin_login.html   # Admin login
│   ├── admin_dashboard.html
│   ├── admin_profile.html
│   ├── admin_achievements.html
│   ├── admin_projects.html
│   ├── admin_certifications.html
│   └── admin_stats.html
└── static/
    ├── css/style.css      # All styles
    ├── js/main.js         # All JavaScript
    └── images/            # ← ADD YOUR IMAGES HERE
```

---

## 🖼️ ADDING YOUR IMAGES

Place the following images in `static/images/`:

| Filename       | Description                     |
|----------------|---------------------------------|
| `profile.jpg`  | Your professional headshot      |
| `cert1.jpg`    | AWS Cloud Practitioner cert     |
| `cert2.jpg`    | HackupTechnology VAPT cert      |
| `cert3.jpg`    | UI/UX Design certificate        |
| `cert4.jpg`    | Web Dev certificate             |
| `ach1.jpg`     | Cybersecurity Hackathon photo   |
| `ach2.jpg`     | Programming Quiz award photo    |
| `ach3.jpg`     | Technical Quiz award photo      |
| `ach4.jpg`     | Intra-College Hackathon photo   |
| `project1.jpg` | AI Cybersecurity project screenshot |
| `project2.jpg` | AI Farmers Platform screenshot  |
| `project3.jpg` | SQLi Simulation screenshot      |

---

## ✅ PERFECT PORTFOLIO CHECKLIST

### Must Have (Upload these first!)
- [ ] `profile.jpg` — Professional photo with good lighting
- [ ] All certificate images — Scan or screenshot your certs
- [ ] Achievement photos — Photos from hackathon wins

### Should Have
- [ ] GitHub profile with security-related repos
- [ ] TryHackMe profile link
- [ ] PortSwigger Web Security Academy profile
- [ ] Resume PDF link

### Nice to Have
- [ ] LinkedIn recommendations
- [ ] CTF writeups (blog posts)
- [ ] GitHub contribution graph screenshot
- [ ] Video demo of your projects

---

## 🛠️ ADMIN PANEL FEATURES

| Feature | What You Can Do |
|---------|----------------|
| **Profile** | Edit name, title, bio, contact info, social links |
| **Projects** | Add/delete projects with images, tags, descriptions |
| **Achievements** | Add/delete hackathon wins with photos & icons |
| **Certifications** | Add/delete certs with validation IDs |
| **Stats** | Update counter numbers shown in the hero section |

---

## 🌐 DEPLOYING ONLINE (Free Options)

### Option 1: PythonAnywhere (Easiest)
1. Sign up at pythonanywhere.com
2. Upload files
3. Create a WSGI configuration
4. Your site goes live!

### Option 2: Railway.app
1. Connect GitHub repo
2. Deploy with one click
3. Free tier available

### Option 3: Render.com
1. Upload to GitHub
2. Connect to Render
3. Auto-deploy on push

---

## 🔒 SECURITY NOTE
Change the `app.secret_key` in `app.py` before deploying to production!

---

**Built for:** Abubakkar Siddiq A | Cybersecurity Professional
**Tech Stack:** Python Flask | HTML5 | CSS3 | Vanilla JS
