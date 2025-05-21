# 🌟 Hello World GUI App (Flask + Bootstrap)

An interactive **Hello World web app** built with Flask and styled using Bootstrap 5.  
Users can enter their name, age, and a message — and see it appear live with stylish animations and dark mode toggle.

---

## 📸 Preview

![App Screenshot](static/screenshot.png)

---

## 🚀 Features

- 🎨 Beautiful & Responsive UI (Bootstrap 5)
- 🌙 Light/Dark Mode toggle
- 🪄 Live animated greeting as you type
- ✅ Toast notifications on submit
- 📜 Recent submission history display
- 📱 Mobile-friendly design

---

## 🛠️ Tech Stack

| Layer       | Tech Used         |
|-------------|-------------------|
| Backend     | Python Flask       |
| Frontend    | HTML5, Bootstrap 5 |
| Database    | SQLite (via `sqlite3`) |
| UI Features | Bootstrap Icons, JS, CSS |

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/hello-gui-flask.git
cd hello-gui-flask

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the app
python app.py
