# Tos Arn Book Store

A full-stack bookstore application with a Vue 3 frontend and a FastAPI backend backed by PostgreSQL.

---

## Prerequisites

Make sure you have the following installed before you begin:

| Tool | Version |
|------|---------|
| [Node.js](https://nodejs.org/) | 18 or higher |
| [Python](https://www.python.org/) | 3.10 or higher |
| [PostgreSQL](https://www.postgresql.org/) | 14 or higher |

---

## 1. Clone the repository

```bash
git clone https://github.com/your-username/Tos-Arn-Aditi.git
cd Tos-Arn-Aditi
```

---

## 2. Database setup

Create a PostgreSQL database and user:

```sql
CREATE USER admin WITH PASSWORD 'admin123';
CREATE DATABASE mydb OWNER admin;
```

> You can use any name/password — just keep them consistent with the `.env` file in the next step.

---

## 3. Backend setup

```bash
cd Backend/FastAPI
```

### Create and activate a virtual environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file inside `Backend/FastAPI/`:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/mydb
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
```

> Replace the `DATABASE_URL` values if you used a different username, password, or database name.

### Run the backend server

```bash
uvicorn app.main:app --reload
```

The API will be available at **http://127.0.0.1:8000**.  
Interactive API docs: **http://127.0.0.1:8000/docs**

> On first startup, all database tables are created automatically and a default admin account is seeded:
> - **Username:** `admin`
> - **Password:** `admin123`
>
> Change these credentials after your first login.

---

## 4. Frontend setup

Open a new terminal tab, then:

```bash
cd Frontend
npm install
npm run dev
```

The app will be available at **http://localhost:5173**.

---

## 5. Accessing the admin panel

Navigate to **http://localhost:5173/admin/login** and sign in with the default credentials above.

Admin sessions expire after **10 minutes** for security. You will be redirected to the login page automatically when the session ends.

---

## Project structure

```
Tos-Arn-Aditi/
├── Backend/
│   └── FastAPI/
│       ├── app/
│       │   ├── models/        # SQLAlchemy models (Book, Order, Admin)
│       │   ├── schemas/       # Pydantic request/response schemas
│       │   ├── services/      # Business logic
│       │   ├── routers/       # API route handlers
│       │   ├── database.py    # DB engine and session
│       │   ├── dependencies.py
│       │   ├── config.py      # App settings (reads .env)
│       │   └── main.py        # FastAPI app entry point
│       ├── requirements.txt
│       └── .env               # Your local env vars (not committed)
└── Frontend/
    ├── src/
    │   ├── views/             # Page components
    │   ├── components/        # Reusable UI components
    │   ├── stores/            # Pinia state (books, orders, cart, auth)
    │   └── router/            # Vue Router with admin guard
    └── package.json
```

---

## API overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/admin/login` | Admin login — returns a 10-min JWT |
| `GET` | `/api/admin/users` | List admin accounts *(auth required)* |
| `POST` | `/api/admin/` | Create a new admin *(auth required)* |
| `GET` | `/api/books/` | List all books |
| `POST` | `/api/books/` | Add a book |
| `PATCH` | `/api/books/{id}` | Update a book (including stock) |
| `DELETE` | `/api/books/{id}` | Delete a book |
| `GET` | `/api/orders/` | List all orders |
| `POST` | `/api/orders/` | Place an order |
| `PATCH` | `/api/orders/{id}/status` | Update order status |
