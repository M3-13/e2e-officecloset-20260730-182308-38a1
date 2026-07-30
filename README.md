# Glamouröser Kleiderschrank-Manager

Ein glamouröser Kleiderschrank-Manager mit rot-schwarzer Hollywood-Optik. Benutzer können sich registrieren, Kleidungsstücke mit Bild und Kategorie anlegen sowie ihre Garderobe durchstöbern.

## Tech-Stack

- **Backend:** Python 3, FastAPI, SQLAlchemy (SQLite)
- **Auth:** JWT (Access-Token)
- **Frontend:** React + TypeScript (Vite), Tailwind CSS
- **Design:** Rot-Schwarzes Hollywood-Theme mit goldenen Akzenten

## Installation

### Backend

```bash
cd backend
py -m pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Starten (Entwicklung)

Starte Backend und Frontend in separaten Terminals:

```bash
# Terminal 1 – Backend (Port 8000)
cd backend
py -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Terminal 2 – Frontend (Port 5173)
cd frontend
npm run dev
```

Öffne `http://localhost:5173` im Browser.

## Umgebungsvariablen

| Variable       | Beschreibung            | Default                    |
|----------------|-------------------------|----------------------------|
| `JWT_SECRET`   | Signier-Secret für JWTs | (muss gesetzt werden)      |
| `DATABASE_URL` | SQLite-Datenbankpfad    | `sqlite:///./wardrobe.db`  |
| `CORS_ORIGIN`  | Frontend-Origin für CORS| `http://localhost:5173`    |
| `UPLOAD_DIR`   | Upload-Verzeichnis      | `uploaded_images`          |

## API-Endpunkte

| Methode | Pfad              | Beschreibung                    |
|---------|-------------------|----------------------------------|
| GET     | `/api/health`     | Health-Check                    |
| GET     | `/openapi.json`   | OpenAPI-Schema                  |

> Weitere Endpunkte folgen in Ticket #1 (Auth) und #2 (Clothing CRUD).

## Features (MVP)

- Benutzerregistrierung und Login (JWT-Auth)
- Kleidungsstücke mit Bild-Upload und Kategorie anlegen
- Garderobe filtern und durchstöbern
- Hollywood-Dunkel-Theme mit roten und goldenen Akzenten
