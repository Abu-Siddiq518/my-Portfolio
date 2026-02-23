from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import json, os, hashlib, uuid
from datetime import datetime
from functools import wraps
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'cyber_portfolio_secret_key_2024'

ADMIN_PASSWORD_HASH = hashlib.sha256('Siddiq+++@123'.encode()).hexdigest()
DATA_FILE     = 'data.json'
MESSAGES_FILE = 'messages.json'
UPLOAD_FOLDER = os.path.join('static', 'images')
ALLOWED_EXT   = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

# ─── Helpers ────────────────────────────────────────────────
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def save_uploaded_image(file_field_name):
    """
    Handle an uploaded image from a form field.
    Returns saved filename, or '' if no file uploaded.
    """
    if file_field_name not in request.files:
        return ''
    f = request.files[file_field_name]
    if f.filename == '':
        return ''
    if f and allowed_file(f.filename):
        ext      = f.filename.rsplit('.', 1)[1].lower()
        filename = secure_filename(f.filename)
        # avoid collisions: prefix with short uuid if file already exists
        dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(dest):
            filename = uuid.uuid4().hex[:8] + '_' + filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename
    return ''

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as fh:
            return json.load(fh)
    return get_default_data()

def save_data(data):
    with open(DATA_FILE, 'w') as fh:
        json.dump(data, fh, indent=2)

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as fh:
            return json.load(fh)
    return []

def save_messages(msgs):
    with open(MESSAGES_FILE, 'w') as fh:
        json.dump(msgs, fh, indent=2)

def get_default_data():
    return {
        "profile": {
            "name": "Abubakkar Siddiq A",
            "title": "Cybersecurity Professional | Penetration Tester",
            "tagline": "Securing the Digital World, One Vulnerability at a Time",
            "about": "Cybersecurity Professional with hands-on penetration testing experience at Vimix Technologies and HackupTechnology. Skilled in identifying and mitigating OWASP Top 10 vulnerabilities using Burp Suite, OWASP ZAP, Nmap, and SQLMap. Proven track record of conducting real-world VAPT on web applications and cloud environments, with strong expertise in exploit development, CTF challenges, and secure coding practices.",
            "email": "abubakkarsiddiq123as@gmail.com",
            "phone": "+91-8489843737",
            "location": "Coimbatore, Tamil Nadu, India",
            "linkedin": "https://www.linkedin.com/in/abubakkar-siddiq-a-78583b309/",
            "github": "https://github.com/abubakkarsiddiq",
            "profile_image": "profile.jpg",
            "resume_url": "#"
        },
        "education": [
            {"degree": "B.Tech - Information Technology", "institution": "Kongunadu College of Engineering and Technology", "period": "2022 – 2026", "score": "CGPA: 8.58", "location": "Thottiyam, Trichy"},
            {"degree": "Higher Secondary Certificate (HSC)", "institution": "Lions Matriculation Higher Secondary School", "period": "2021 – 2022", "score": "82%", "location": "Ponnamaravathy, Pudukkottai"}
        ],
        "experience": [
            {"role": "Security Tester", "company": "Vimix Technologies LLP", "type": "Internship", "period": "Jan 2026 – Present", "location": "Coimbatore, Tamil Nadu, India",
             "points": ["Performing real-world application security testing to identify OWASP Top 10 vulnerabilities", "Conducting penetration testing to assess security risks and explore cloud environments", "Identified and documented 10 real-world security vulnerabilities in a live Django-based web application", "Skills: Burp Suite, Cloud Computing, Penetration Testing, OWASP Top 10"]},
            {"role": "Vulnerability Assessment & Penetration Testing", "company": "HackupTechnology", "type": "Internship", "period": "Feb 2025 – Aug 2025", "location": "Coimbatore, Tamil Nadu, India",
             "points": ["Trained in Web Application VAPT by validating vulnerabilities in demo labs using Burp Suite and OWASP ZAP", "Transitioned to real-world application testing, identifying issues such as IDOR, authentication flaws, and misconfigurations", "Securing applications through effective remediation measures and security best practices", "Skills: Web Application Security, Ethical Hacking, Burp Suite, OWASP ZAP, Vulnerability Assessment"]}
        ],
        "skills": {
            "Penetration Testing": ["Web App Security (WAPT)", "Network Security Testing", "Ethical Hacking"],
            "Security Tools": ["Burp Suite", "OWASP ZAP", "Nmap", "SQLMap", "Wfuzz", "Nuclei", "Metasploit", "Beef Framework"],
            "Vulnerability Assessment": ["OWASP Top 10", "SQLi", "XSS", "CSRF", "Broken Authentication", "Dorking"],
            "SOC Tools": ["Virus Total", "Thunderbird", "Nessus", "Splunk", "WireShark"],
            "Digital Forensics": ["Autopsy", "FTK", "Volatility"],
            "Operating Systems": ["Linux (Kali, Ubuntu)", "Windows"],
            "Programming": ["Python", "HTML", "CSS", "JavaScript"],
            "Soft Skills": ["Critical Thinking", "Problem-Solving", "Team Collaboration", "Project Ownership"]
        },
        "projects": [
            {"title": "AI-Powered Cybersecurity Incident Management System", "description": "Developed a cybersecurity-focused, AI-powered incident management system using machine learning models and NLP. Implemented threat intelligence to analyze reported attacks with secure reporting and real-time evidence analysis.", "highlights": ["Machine Learning & NLP Integration", "Real-time threat intelligence", "Secure reporting system", "IEEE Conference Publication"], "tags": ["Python", "ML", "NLP", "Cybersecurity", "IEEE"], "image": "project1.jpg", "link": "#"},
            {"title": "AI-Powered Platform for Farmers", "description": "Developed a CNN-based plant disease detection system integrated with marketplace functionality. Ensured data security and safe API communication throughout the platform.", "highlights": ["CNN-based disease detection", "Secure API communication", "Marketplace integration", "IEEE Conference Publication"], "tags": ["Python", "CNN", "AI", "Security", "IEEE"], "image": "project2.jpg", "link": "#"},
            {"title": "SQL Injection Attack Simulation", "description": "Simulated SQL Injection attacks on web applications to understand attack vectors. Implemented input sanitization, parameterized queries, and secure coding practices.", "highlights": ["Attack vector simulation", "Input sanitization", "Parameterized queries", "Security documentation"], "tags": ["SQLi", "Web Security", "Python", "OWASP"], "image": "project3.jpg", "link": "#"}
        ],
        "certifications": [
            {"title": "AWS Cloud Practitioner", "issuer": "Amazon Web Services", "validation": "d3ad77640b924c73b8356e182070bf8a", "image": "cert1.jpg", "date": "2024"},
            {"title": "VAPT Internship Certificate", "issuer": "HackupTechnology", "validation": "HackupTech-VAPT-2025", "image": "cert2.jpg", "date": "2025"},
            {"title": "UI/UX Design Professional Certification", "issuer": "Professional Body", "validation": "UIUX-CERT-2024", "image": "cert3.jpg", "date": "2024"},
            {"title": "Web & Full Stack Development Certification", "issuer": "Professional Body", "validation": "WEBDEV-CERT-2024", "image": "cert4.jpg", "date": "2024"}
        ],
        "achievements": [
            {"title": "1st Prize – Cybersecurity Hackathon", "event": "MAM College, Trichy", "description": "College-level cybersecurity competition – First Place", "image": "ach1.jpg", "year": "2024", "icon": "🏆"},
            {"title": "1st Prize – Technical Programming Quiz", "event": "IT Department", "description": "Demonstrated programming excellence", "image": "ach2.jpg", "year": "2024", "icon": "🥇"},
            {"title": "1st Place – Technical Quiz", "event": "JJ College of Engineering", "description": "Won college-level technical quiz competition", "image": "ach3.jpg", "year": "2023", "icon": "🎯"},
            {"title": "2nd Prize – Intra-College Hackathon", "event": "EEE Department", "description": "Showcased innovative solutions", "image": "ach4.jpg", "year": "2023", "icon": "🥈"}
        ],
        "ctf_research": [
            "Discovered and disclosed SQL Injection and XSS vulnerabilities in test environments",
            "Enhanced web application security awareness through responsible disclosure",
            "Solved real-world labs on TryHackMe and PortSwigger",
            "Performed exploitation, privilege escalation, and post-exploitation",
            "Participated in CTF competitions to sharpen penetration testing skills",
            "Completed hands-on WAPT labs focusing on security testing methodologies"
        ],
        "stats": {"vulnerabilities_found": 10, "ctf_solved": 50, "certifications": 4, "projects": 3}
    }

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

# ─── Public ─────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html', data=load_data())

@app.route('/contact', methods=['POST'])
def contact():
    name    = request.form.get('name', '').strip()
    email   = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()
    if name and email and message:
        msgs = load_messages()
        msgs.insert(0, {
            "id":        datetime.now().strftime('%Y%m%d%H%M%S%f'),
            "name":      name,
            "email":     email,
            "subject":   subject or '(no subject)',
            "message":   message,
            "timestamp": datetime.now().strftime('%d %b %Y, %I:%M %p'),
            "read":      False
        })
        save_messages(msgs)
        return jsonify({"status": "ok",    "msg": "Message received! I'll get back to you soon."})
    return jsonify({"status": "error", "msg": "Please fill all required fields."})

# ─── Auth ────────────────────────────────────────────────────
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        pw = request.form.get('password')
        if hashlib.sha256(pw.encode()).hexdigest() == ADMIN_PASSWORD_HASH:
            session['admin_logged_in'] = True
            flash('Welcome back, Siddiq! Access granted.', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('ACCESS DENIED: Invalid credentials', 'error')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

# ─── Dashboard ───────────────────────────────────────────────
@app.route('/admin')
@login_required
def admin_dashboard():
    data   = load_data()
    msgs   = load_messages()
    unread = sum(1 for m in msgs if not m.get('read'))
    return render_template('admin_dashboard.html', data=data, msgs=msgs, unread=unread)

# ─── Messages ────────────────────────────────────────────────
@app.route('/admin/messages')
@login_required
def admin_messages():
    msgs = load_messages()
    for m in msgs:
        m['read'] = True
    save_messages(msgs)
    return render_template('admin_messages.html', msgs=msgs)

@app.route('/admin/messages/delete/<msg_id>', methods=['POST'])
@login_required
def delete_message(msg_id):
    msgs = [m for m in load_messages() if m['id'] != msg_id]
    save_messages(msgs)
    flash('Message deleted.', 'success')
    return redirect(url_for('admin_messages'))

@app.route('/admin/messages/delete_all', methods=['POST'])
@login_required
def delete_all_messages():
    save_messages([])
    flash('All messages cleared.', 'success')
    return redirect(url_for('admin_messages'))

# ─── Profile ─────────────────────────────────────────────────
@app.route('/admin/profile', methods=['GET', 'POST'])
@login_required
def admin_profile():
    data = load_data()
    if request.method == 'POST':
        for field in ['name','title','tagline','about','email','phone','location','linkedin','github']:
            data['profile'][field] = request.form.get(field, data['profile'].get(field, ''))
        # Remove image flag
        if request.form.get('remove_profile_image') == '1':
            data['profile']['profile_image'] = ''
        # Profile image upload (new file takes priority)
        img = save_uploaded_image('profile_image')
        if img:
            data['profile']['profile_image'] = img
        # Frame shape
        shape = request.form.get('profile_shape', 'circle')
        if shape in ('circle', 'rounded', 'square'):
            data['profile']['profile_shape'] = shape
        # Brightness & contrast
        try:
            data['profile']['profile_brightness'] = max(50, min(150, int(request.form.get('profile_brightness', 100))))
            data['profile']['profile_contrast']   = max(50, min(150, int(request.form.get('profile_contrast',   100))))
        except (ValueError, TypeError):
            pass
        save_data(data)
        flash('Profile updated!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_profile.html', data=data)

# ─── Projects ────────────────────────────────────────────────
@app.route('/admin/projects', methods=['GET', 'POST'])
@login_required
def admin_projects():
    data = load_data()
    if request.method == 'POST':
        action = request.form.get('action')
        uploaded_img = save_uploaded_image('image_file')

        if action == 'add':
            highlights = [h.strip() for h in request.form.get('highlights','').split('\n') if h.strip()]
            tags       = [t.strip() for t in request.form.get('tags','').split(',') if t.strip()]
            image      = uploaded_img or request.form.get('image','')
            data['projects'].append({"title": request.form.get('title',''), "description": request.form.get('description',''), "highlights": highlights, "tags": tags, "image": image, "link": request.form.get('link','#')})
            save_data(data)
            flash('Project added!', 'success')

        elif action == 'edit':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['projects']):
                highlights = [h.strip() for h in request.form.get('highlights','').split('\n') if h.strip()]
                tags       = [t.strip() for t in request.form.get('tags','').split(',') if t.strip()]
                image      = uploaded_img or request.form.get('image', data['projects'][idx].get('image',''))
                data['projects'][idx] = {"title": request.form.get('title',''), "description": request.form.get('description',''), "highlights": highlights, "tags": tags, "image": image, "link": request.form.get('link','#')}
                save_data(data)
                flash('Project updated!', 'success')

        elif action == 'delete':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['projects']):
                data['projects'].pop(idx)
                save_data(data)
                flash('Project deleted!', 'success')

    return render_template('admin_projects.html', data=data)

# ─── Achievements ────────────────────────────────────────────
@app.route('/admin/achievements', methods=['GET', 'POST'])
@login_required
def admin_achievements():
    data = load_data()
    if request.method == 'POST':
        action       = request.form.get('action')
        uploaded_img = save_uploaded_image('image_file')

        if action == 'add':
            image = uploaded_img or request.form.get('image','')
            data['achievements'].append({"title": request.form.get('title'), "event": request.form.get('event'), "description": request.form.get('description'), "year": request.form.get('year'), "icon": request.form.get('icon','🏆'), "image": image})
            save_data(data)
            flash('Achievement added!', 'success')

        elif action == 'edit':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['achievements']):
                image = uploaded_img or request.form.get('image', data['achievements'][idx].get('image',''))
                data['achievements'][idx] = {"title": request.form.get('title'), "event": request.form.get('event'), "description": request.form.get('description'), "year": request.form.get('year'), "icon": request.form.get('icon','🏆'), "image": image}
                save_data(data)
                flash('Achievement updated!', 'success')

        elif action == 'delete':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['achievements']):
                data['achievements'].pop(idx)
                save_data(data)
                flash('Achievement deleted!', 'success')

    return render_template('admin_achievements.html', data=data)

# ─── Certifications ──────────────────────────────────────────
@app.route('/admin/certifications', methods=['GET', 'POST'])
@login_required
def admin_certifications():
    data = load_data()
    if request.method == 'POST':
        action       = request.form.get('action')
        uploaded_img = save_uploaded_image('image_file')

        if action == 'add':
            image = uploaded_img or request.form.get('image','')
            data['certifications'].append({"title": request.form.get('title'), "issuer": request.form.get('issuer'), "validation": request.form.get('validation'), "date": request.form.get('date'), "image": image})
            save_data(data)
            flash('Certification added!', 'success')

        elif action == 'edit':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['certifications']):
                image = uploaded_img or request.form.get('image', data['certifications'][idx].get('image',''))
                data['certifications'][idx] = {"title": request.form.get('title'), "issuer": request.form.get('issuer'), "validation": request.form.get('validation'), "date": request.form.get('date'), "image": image}
                save_data(data)
                flash('Certification updated!', 'success')

        elif action == 'delete':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['certifications']):
                data['certifications'].pop(idx)
                save_data(data)
                flash('Certification deleted!', 'success')

    return render_template('admin_certifications.html', data=data)

# ─── Skills ──────────────────────────────────────────────────
@app.route('/admin/skills', methods=['GET', 'POST'])
@login_required
def admin_skills():
    data = load_data()
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add_category':
            cat_name = request.form.get('category_name', '').strip()
            if cat_name and cat_name not in data['skills']:
                skills_raw = request.form.get('skills_list', '')
                items = [s.strip() for s in skills_raw.split(',') if s.strip()]
                data['skills'][cat_name] = items
                save_data(data)
                flash(f'Skill category "{cat_name}" added!', 'success')
            elif cat_name in data['skills']:
                flash('Category name already exists.', 'error')

        elif action == 'edit_category':
            old_name = request.form.get('old_name', '')
            new_name = request.form.get('category_name', '').strip()
            skills_raw = request.form.get('skills_list', '')
            items = [s.strip() for s in skills_raw.split(',') if s.strip()]
            if old_name in data['skills']:
                # Rebuild dict preserving order with updated key/values
                new_skills = {}
                for k, v in data['skills'].items():
                    if k == old_name:
                        new_skills[new_name] = items
                    else:
                        new_skills[k] = v
                data['skills'] = new_skills
                save_data(data)
                flash('Skill category updated!', 'success')

        elif action == 'delete_category':
            cat_name = request.form.get('category_name', '')
            if cat_name in data['skills']:
                del data['skills'][cat_name]
                save_data(data)
                flash(f'Category "{cat_name}" deleted!', 'success')

    return render_template('admin_skills.html', data=data)

# ─── Experience ──────────────────────────────────────────────
@app.route('/admin/experience', methods=['GET', 'POST'])
@login_required
def admin_experience():
    data = load_data()
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            points_raw = request.form.get('points', '')
            points = [p.strip() for p in points_raw.split('\n') if p.strip()]
            data['experience'].append({
                "role":     request.form.get('role', ''),
                "company":  request.form.get('company', ''),
                "type":     request.form.get('type', 'Internship'),
                "period":   request.form.get('period', ''),
                "location": request.form.get('location', ''),
                "points":   points
            })
            save_data(data)
            flash('Experience added!', 'success')

        elif action == 'edit':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['experience']):
                points_raw = request.form.get('points', '')
                points = [p.strip() for p in points_raw.split('\n') if p.strip()]
                data['experience'][idx] = {
                    "role":     request.form.get('role', ''),
                    "company":  request.form.get('company', ''),
                    "type":     request.form.get('type', 'Internship'),
                    "period":   request.form.get('period', ''),
                    "location": request.form.get('location', ''),
                    "points":   points
                }
                save_data(data)
                flash('Experience updated!', 'success')

        elif action == 'delete':
            idx = int(request.form.get('index'))
            if 0 <= idx < len(data['experience']):
                data['experience'].pop(idx)
                save_data(data)
                flash('Experience deleted!', 'success')

    return render_template('admin_experience.html', data=data)

# ─── Stats ───────────────────────────────────────────────────
@app.route('/admin/stats', methods=['GET', 'POST'])
@login_required
def admin_stats():
    data = load_data()
    if request.method == 'POST':
        data['stats']['vulnerabilities_found'] = int(request.form.get('vulnerabilities_found', 0))
        data['stats']['ctf_solved']            = int(request.form.get('ctf_solved', 0))
        data['stats']['certifications']        = int(request.form.get('certifications', 0))
        data['stats']['projects']              = int(request.form.get('projects', 0))
        save_data(data)
        flash('Stats updated!', 'success')
    return render_template('admin_stats.html', data=data)

@app.route('/api/data')
def api_data():
    return jsonify(load_data())

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        save_data(get_default_data())
    if not os.path.exists(MESSAGES_FILE):
        save_messages([])
    app.run(debug=False, host="0.0.0.0",port=5000)

