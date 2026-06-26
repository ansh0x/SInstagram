# SInstagram — Social Media WebApp

A lightweight, full-stack social media web application inspired by Instagram, built with **Flask** and **SQLAlchemy**. Users can sign up, share photos, like posts, and manage their personal dashboard.

<p align="center">
  <img src="https://img.shields.io/badge/Flask-3.0.0-black?style=flat&logo=flask" />
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.23-red?style=flat" />
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" />
</p>

---

## ✨ Features

- **🔐 Authentication** — Secure signup & login with Werkzeug password hashing and Flask-Login session management.
- **📸 Photo Sharing** — Upload images with captions; files stored securely with timestamped filenames.
- **❤️ Interactive Likes** — Real-time like/unlike via AJAX (no page refresh) with animated heart icons.
- **🗑️ Post Management** — Delete your own posts from the personal dashboard.
- **🏠 Shuffled Feed** — Home page displays all community posts in random order.
- **🔍 Full-Screen View** — Click any post to open a focused overlay popup.
- **🎨 Responsive UI** — Custom CSS with dark sidebar, CSS variables, and smooth hover transitions.

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/ansh0x/SInstagram.git
cd SInstagram

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirement.txt

# 4. Initialize database
flask db init
flask db migrate -m "init"
flask db upgrade

# 5. Run
flask run
# Open http://127.0.0.1:5000
```
## 🗃️ Database Schema
| Table      | Key Fields                                    | Relationships                                    |
| ---------- | --------------------------------------------- | ------------------------------------------------ |
| `User`     | `id`, `username`, `email`, `name`, `password` | `posts`, `liked_posts`, `followers`, `following` |
| `Posts`    | `id`, `post_name`, `caption`, `date_created`  | `user`, `likes`, `comments`                      |
| `Comments` | `id`, `post_id`                               | `post`                                           |
| `Follower` | `id`, `follower_id`, `following_id`           | Self-referential many-to-many                    |
## 🛡️ Security Considerations

    Passwords hashed with Werkzeug (generate_password_hash)
    Upload filenames sanitized with secure_filename
    Session protected by Flask-Login
