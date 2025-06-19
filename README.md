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

---

## AI Usage Notes (ChatGPT 4.1)

### What AI helped with
- Designing the structure of Django models and their relationships
- Styling profile cards responsibly using Bootstrap
- Integrating and configuring Select2 for tag selection
- Writing and debugging template logic for profile card display
- Building pagination and customizing its appearance

### What AI didn't help with
- Handling edge cases in form validation
- Select2 behavior quirks (required additional manual tweaking)
- Fine-tuning responsiveness for long bios and field overflows

### Example prompts that I used
- “How do I make a ManyToMany field in Django show as multi-select checkboxes with tags?”
- “How can I make Bootstrap cards clickable links without wrapping the entire card in an <a> tag?”
- “Write a custom Django form that saves user info and a related profile model with image upload.”

