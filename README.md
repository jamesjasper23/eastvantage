Address Book API
A FastAPI application that allows users to create, update, delete, and search addresses based on geographic distance.

Features
    • Create address
    • Update address
    • Delete address
    • Retrieve all addresses
    • Find addresses within a given distance
    • SQLite database
    • Logging support
    • Docker support

Tech Stack
    • Python
    • FastAPI
    • SQLAlchemy
    • SQLite
    • Docker
    • Uvicorn

Project Structure
app/
 ├ api/
 ├ core/
 ├ db/
 ├ schemas/
 ├ services/
 └ main.py

Dockerfile
docker-compose.yml
requirements.txt
.env

Running the Project
Option 1 — Run with Docker (Recommended)
Build and start the application:
docker compose up --build
The API will be available at:
http://localhost:3001/docshttps://github.com/jamesjasper23/eastvantage/pull/2/conflict?name=README.md&ancestor_oid=0b0c0da2bfa0f15b2a8cc5d9d4798df97ef54911&base_oid=9197b261fa95b4a404323a23dda5b8c1c0575f66&head_oid=26b3abeb9ed45f87a9d9f18d3016c6d8eed9d5e3

Option 2 — Run without Docker
Create virtual environment:
python -m venv venv
Activate environment:
Linux / Mac:
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run the application:
uvicorn app.main:app --reload --port 3001
Open:
http://localhost:3001/docs

Environment Variables
Create a .env file in the project root:
DATABASE_URL=sqlite:///./addresses.db

API Endpoints
Method	Endpoint	Description
POST	/addresses	Create address
GET	/addresses	Get all addresses
PUT	/addresses/{id}	Update address
DELETE	/addresses/{id}	Delete address
GET	/addresses/near	Find nearby addresses

Example Request
GET /addresses/near?lat=12.9716&lon=77.5946&distance=5
This returns all addresses within 5 km of the given coordinates.

Logging
Application logs are stored in:
logs/app.log

