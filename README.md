# 🛡️ Phishing Simulation & Security Awareness Tool

> **⚠️ IMPORTANT:** This project is intended strictly for **authorized security-awareness training, education, and testing in controlled environments**. Never use it to collect real credentials or personal information.

A security-awareness demonstration tool built with **Python, Flask, Tkinter, SQLite, and Cloudflare Tunnel**. The project demonstrates how phishing simulations work while keeping testing within an authorized and controlled environment.

---


.

---

## 🚀 Features

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| 🚀 One-Click Launch | Start the local simulation environment easily                    |
| 🌐 Test URL         | Generate a URL for an authorized test environment                |
| 📊 Live Dashboard   | View simulated test submissions                                  |
| 📋 Copy URL         | Easily copy the generated testing URL                            |
| 🛑 Stop Server      | Stop the simulation safely                                       |
| 🎨 Dark Theme       | Modern dark-themed interface                                     |
| 📱 Responsive UI    | Designed for desktop and mobile screens                          |
| 🔒 Safe Testing     | Designed to use dummy/test credentials instead of real passwords |

---

## 🛠️ Technologies

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| **Python 3.8+**       | Core programming language           |
| **Flask**             | Local web application               |
| **Tkinter**           | Desktop control interface           |
| **SQLite**            | Local test-data storage             |
| **Cloudflare Tunnel** | Optional authorized remote testing  |
| **PyInstaller**       | Build standalone Windows executable |

---

## 📁 Project Structure

```text
phishing_demo/
│
├── app.py                    # Flask web application
├── phishing_controller.py   # Desktop controller
├── cloudflared.exe          # Optional Cloudflare tunnel binary
├── database.db              # Local test database
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore configuration
│
└── templates/
    ├── login.html           # Training/simulation page
    └── dashboard.html       # Test dashboard
```

---

# 📦 Installation

## Prerequisites

* Python 3.8 or newer
* Windows/Linux/macOS
* Internet connection if using an authorized remote-testing tunnel

## Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/phishing-simulation-tool.git
cd phishing-simulation-tool
```

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3 — Optional Tunnel Setup

If remote testing is required, install/configure the appropriate tunneling software according to its official documentation.

Only expose the application when you have authorization to conduct the test.

---

# 🚀 Running the Project

## Method 1 — Run from Source

```bash
python phishing_controller.py
```

## Method 2 — Build a Windows Executable

```bash
python -m PyInstaller --onefile --windowed --name "PhishingController" phishing_controller.py
```

The executable will be generated inside:

```text
dist/
```

## Method 3 — Run Flask Directly

```bash
python app.py
```

The local application can then be accessed through the configured localhost port.

---

# 🎯 How the Simulation Works

1. Start the application.
2. Launch the training/simulation environment.
3. Use only an authorized test device or test account.
4. Enter **dummy credentials** such as:

   * `test@example.com`
   * `TrainingPassword123`
5. Review the result in the local dashboard.
6. Stop the server after testing.
7. Delete temporary test data when the exercise is complete.

> **Never enter a real password, banking credential, social-media password, or other sensitive information into the simulation.**

---

# 📊 Dashboard

The dashboard should display only information necessary for the training exercise.

Recommended fields:

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| Test Username    | Dummy username used during training |
| Test Result      | Simulation outcome                  |
| Timestamp        | Time of the test                    |
| Training Session | Identifier for the exercise         |

Avoid storing real passwords or unnecessary personal information.

---

# 🔒 Security & Privacy

This project should follow these principles:

* Never collect real passwords.
* Never collect authentication tokens.
* Never collect banking information.
* Never impersonate a real service for unauthorized use.
* Use dummy accounts and test credentials.
* Obtain authorization before conducting simulations.
* Keep testing data local whenever possible.
* Delete test data after the exercise.
* Do not publish collected personal information.
* Do not share testing URLs with unauthorized people.

---

# ⚖️ Legal & Ethical Notice

Phishing simulations can have serious legal and privacy implications.

The legality of a security test depends on factors including:

* Authorization
* Ownership of the systems involved
* Scope of the test
* Type of information collected
* Applicable privacy and cybersecurity laws
* Whether users were properly informed or the exercise was approved

### 🇳🇵 Nepal

When conducting testing in Nepal, users should review applicable cybersecurity, electronic-transaction, privacy, and criminal laws and obtain appropriate authorization before testing systems or people.

### 🌍 International Testing

If a test involves systems, users, or infrastructure located in another country, additional laws and regulations may apply, including computer-misuse and data-protection legislation.

> **This README is not legal advice.** Consult a qualified legal professional or your organization's authorized security/legal team when conducting real-world security-awareness exercises.

---

# ✅ Authorized Use

| Activity                                               | Recommended |
| ------------------------------------------------------ | ----------- |
| Testing your own local environment                     | ✅           |
| Testing with explicit written authorization            | ✅           |
| Security-awareness training with approved participants | ✅           |
| Using dummy credentials                                | ✅           |
| Collecting real passwords                              | ❌           |
| Testing strangers without authorization                | ❌           |
| Impersonating services for fraud                       | ❌           |
| Credential theft                                       | ❌           |
| Selling collected information                          | ❌           |
| Extortion or blackmail                                 | ❌           |

---

# 🛡️ Responsible Testing Rules

### 1. Get Authorization

Obtain permission before conducting a security simulation against systems or users you do not personally control.

### 2. Use Test Accounts

Create dedicated accounts specifically for training.

### 3. Use Dummy Credentials

Never use real passwords or sensitive authentication information.

### 4. Minimize Data Collection

Collect only the information necessary for the training exercise.

### 5. Delete Test Data

Remove temporary testing information when the exercise is complete.

### 6. Stay Within Scope

Do not expand the test beyond the systems, users, dates, or techniques that were authorized.

---

# 📞 Contact

**Author:** Aksharatit Sapkota



For security-related issues, please report them privately rather than publishing sensitive information.

---

# 📄 License

This project is licensed under the **MIT License**.

The license does not provide permission to use the software for:

* Unauthorized access
* Credential theft
* Fraud
* Privacy violations
* Identity theft
* Harassment
* Unauthorized phishing
* Any activity prohibited by applicable law

---

# 🤝 Contributing

Contributions are welcome when they improve the educational and defensive purpose of the project.

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 🙏 Acknowledgments

* Flask community
* Python community
* Cloudflare
* Open-source contributors
* Cybersecurity education community

---

# 📌 Version History

| Version   | Date        | Changes                     |
| --------- | ----------- | --------------------------- |
| **1.0.0** | August 2026 | Initial educational release |

---

## ⚠️ Final Reminder

This project is intended for **authorized security education and awareness training**.

Use controlled test accounts, dummy credentials, and systems you are authorized to test.

**Learn cybersecurity responsibly. Stay ethical. Stay safe. 🔐**

**Made with ❤️ by Aksharatit Sapkota**
