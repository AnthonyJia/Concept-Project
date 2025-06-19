# 🎨 Concept Creative Portfolio & Search App

A mini full-stack web app that allows users to explore creative profiles, search by name or field, and view rich creator cards.

Built with **Django**, **Bootstrap**, and **SQLite**, and enhanced with **Select2** and custom CSS for a clean user interface.

## 🚀 Features

- Add new creative profiles with:
  - Name
  - Bio
  - Profile picture
  - Creative fields (multi-select)
  - Up to 3 portfolio links
- View creator profiles in a card layout
- Search creators by name
- Filter creators by creative field
- Detail view for each profile

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AnthonyJia/Concept-Project.git
cd Concept-Project
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

### 6. Visit http://127.0.0.1:8000 in your browser
