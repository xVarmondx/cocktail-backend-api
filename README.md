# 🍹 Koktajlownik API

<div align="center">

**Your ultimate cocktail recipe management API — built with Django**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST-3.14+-red?logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.x-4169E1?logo=postgresql)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-black?logo=jsonwebtokens)](https://jwt.io/)
[![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-85EA2D?logo=swagger)](https://swagger.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

---

## About the Project

**Koktajlownik** is a fully functional, secure REST API for managing cocktail recipes and an ingredient database. Built on top of Django REST Framework and PostgreSQL, it serves as a solid backend foundation for modern frontend and mobile applications.

### ✨ Key Features

| | Feature | Description |
|---|---|---|
| 🍸 | **Cocktail Management** | Full CRUD for recipes — ingredients handled in a single request |
| 🧂 | **Ingredient Database** | Manage ingredients split into alcoholic and non-alcoholic |
| 🔐 | **JWT Authorization** | Only the author or an Admin can edit/delete a cocktail |
| 🔍 | **Filtering & Pagination** | Search by category and name; built-in result pagination |
| ✅ | **Data Validation** | Strict validation — DRF built-ins + custom validators |

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations and create a superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 3. Start the server
python manage.py runserver
```

> 📖 Interactive Swagger docs (OpenAPI 3.0) available at: **http://127.0.0.1:8000/api/docs/**

![Swagger API Documentation](swagger.png)

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-unique-django-secret-key
DEBUG=True

DB_NAME=koktajlownik
DB_USER=postgres
DB_PASSWORD=your-password
```

---

## 🗄️ Database Schema

```mermaid
erDiagram
    User ||--o{ Cocktail : "creates (author)"
    Cocktail ||--o{ CocktailIngredient : "contains"
    Ingredient ||--o{ CocktailIngredient : "is part of"

    User {
        int id PK
        string username
        string password
    }
    Cocktail {
        int id PK "Auto-increment ID"
        string name "Cocktail name"
        string category "Category (e.g. Drink)"
        text instructions "Preparation instructions"
        int author_id FK "Link to author"
    }
    Ingredient {
        int id PK "Auto-increment ID"
        string name UK "Unique name"
        text description "Description"
        boolean is_alcoholic "Contains alcohol"
        string image_url "Optional image"
    }
    CocktailIngredient {
        int id PK
        int cocktail_id FK
        int ingredient_id FK
        string amount "Exact quantity/ratio"
    }
```

---

## 📡 API Endpoints

### 🍹 Cocktails — `/api/cocktails/`

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|:----:|
| `GET` | `/api/cocktails/` | List cocktails *(pagination & filters)* | — |
| `GET` | `/api/cocktails/:id` | Cocktail details | — |
| `POST` | `/api/cocktails/` | Create a new cocktail | 🔐 |
| `PATCH` | `/api/cocktails/:id` | Update a cocktail *(author/admin only)* | 🔐 |
| `DELETE` | `/api/cocktails/:id` | Delete a cocktail *(author/admin only)* | 🔐 |

**Query params:** `?search=` · `?category=` · `?ordering=`

### 🧂 Ingredients — `/api/ingredients/`

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|:----:|
| `GET` | `/api/ingredients/` | List ingredients | — |
| `GET` | `/api/ingredients/:id` | Ingredient details | — |
| `POST` | `/api/ingredients/` | Add an ingredient | 🔐 |
| `PATCH` | `/api/ingredients/:id` | Update an ingredient | 🔐 |
| `DELETE` | `/api/ingredients/:id` | Delete an ingredient | 🔐 |

### 🔑 Authorization

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/token/` | Obtain Access + Refresh Token |
| `POST` | `/api/token/refresh/` | Refresh an expired Access Token |
