# 🎬 Movies & Shows Management System (Python)

This is a beginner-friendly yet feature-rich Python project designed to manage movies and TV shows.  
It allows users to add movies, add shows, view everything, search, delete, and mark items as watched — all in a simple menu-driven interface.

All data is saved automatically in a JSON file, so your collection stays safe even after closing the program.

---

## 🚀 Features

### 🎥 **Movie Management**
- Add a new movie  
- Store:
  - Title  
  - Release year  
  - Duration (e.g., *2h 15m* or *130 min*)  
  - Genre  
  - Watch status  

### 📺 **Show Management**
- Add a TV show  
- Store:
  - Title  
  - Release year  
  - Number of seasons  
  - Number of episodes  
  - Duration per episode  
  - Watch status  

### 🔍 **General Features**
- View all movies & shows  
- Search by title keyword  
- Mark items as watched  
- Delete movies or shows  
- Persistent storage in `movies_shows.json`  
- Clean and clear menu-driven CLI  

---

## 📂 Project Structure
project-folder/ │ ├── movies_system.py          # Main Python script ├── movies_shows.json         # Auto-created database file └── README.md                 # Documentation
---

## ▶️ How to Run

### 🖥️ Windows (PowerShell or CMD)

1. Open PowerShell in your project folder:

cd "C:\Users\serum\OneDrive\Documents\python project"

2. Run the program:

python movies_system.py

---

### 💻 VS Code

1. Open VS Code  
2. Open the folder containing `movies_system.py`  
3. Open the file and press **Run ▶**  

---

### 📱 Android – Pydroid 3

1. Install **Pydroid 3**  
2. Create a new file  
3. Paste the full code  
4. Save as `movies_system.py`  
5. Press **Run ▶**

---

## 🧠 Program Flow

When you run the program, you will see this menu:

=== Movies & Shows Management ===

1. Add Movie


2. Add Show


3. View All


4. Mark as Watched


5. Delete Movie/Show


6. Search


7. Exit
### 🔸 Add Movie  
Enter title, year, duration, and genre.

### 🔸 Add Show  
Enter title, year, seasons, episodes, duration per episode.

### 🔸 View All  
Displays all stored movies & shows with watch status.

### 🔸 Mark as Watched  
Turns "Pending ❗" into "Watched ✔".

### 🔸 Delete Item  
Remove movies or shows by number.

### 🔸 Search  
Search items by title keyword.

---

## 📌 Example Data Stored in JSON

```json
[
    {
        "type": "Movie",
        "title": "Avengers Endgame",
        "year": "2019",
        "duration": "3h 1m",
        "genre": "Action",
        "watched": true
    },
    {
        "type": "Show",
        "title": "Money Heist",
        "year": "2017",
        "seasons": "5",
        "episodes": "48",
        "duration": "45 min",
        "watched": false
    }
]



👤 Author

gunta karthick reddy

26MIM10020