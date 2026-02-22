# To-Do App (Flask)

A simple To-Do list web application built with **Flask**, letting you add, view, update, and remove tasks through a clean interface. It’s a beginner-friendly project to practice Flask routing, templates, and database integration.

---

## 💡 Features

- Add a task with a description  
- View all tasks  
- Mark tasks as complete or delete them  
- Uses Python + Flask + database (SQLAlchemy)  
- Modular structure with `app` package  

---

## 🧠 Technologies Used

- Flask — lightweight Python web framework  
- SQLAlchemy — ORM for database operations  
- HTML / CSS / Bootstrap — UI templates  
- Python virtual environment — dependency isolation  

---

## 🚀 Getting Started

### 📌 Prerequisites

Make sure you have:

- Python 3.7 or higher
- pip installed

---

### 📥 Clone Repository

```bash
git clone https://github.com/ashu-s1ngh/To-Do-App-Flask.git
cd To-Do-App-Flask
```

---

### 🐍 Create Virtual Environment

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python run.py
```

App will start at:

```
http://127.0.0.1:5000/
```

Open it in your browser to use the To-Do app.

---

## 🧩 Project Structure

```
To-Do-App-Flask/
│
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── templates/
│   │   └── __init__.py
│   │
│   └── models.py
│
│
├── run.py
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

Manual testing steps:

1. Open homepage  
2. Add a task  
3. Mark complete or delete  

---

## 📜 License

This project is open-source and free to use.

---

⭐ *Feel free to fork, modify, and expand it with features like login, due dates, or APIs.*

