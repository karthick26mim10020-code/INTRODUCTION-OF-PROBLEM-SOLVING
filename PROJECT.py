import json
import os

FILENAME = "movies_shows.json"

# Load existing data
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


# Save data to file
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- ADD MOVIE ----------------
def add_movie(data):
    print("\n--- Add Movie ---")
    title = input("Movie title: ")
    year = input("Release year: ")
    duration = input("Duration (e.g. 2h 15m or 130 min): ")
    genre = input("Genre (Action, Drama, Sci-Fi, etc): ")

    movie = {
        "type": "Movie",
        "title": title,
        "year": year,
        "duration": duration,
        "genre": genre,
        "watched": False
    }

    data.append(movie)
    save_data(data)
    print("Movie added successfully!\n")


# ---------------- ADD SHOW ----------------
def add_show(data):
    print("\n--- Add Show ---")
    title = input("Show title: ")
    year = input("Release year: ")
    seasons = input("Number of seasons: ")
    episodes = input("Total episodes: ")
    duration = input("Duration per episode (e.g. 45 min): ")

    show = {
        "type": "Show",
        "title": title,
        "year": year,
        "seasons": seasons,
        "episodes": episodes,
        "duration": duration,
        "watched": False
    }

    data.append(show)
    save_data(data)
    print("Show added successfully!\n")


# ---------------- VIEW ALL ----------------
def list_items(data):
    if not data:
        print("No movies or shows found.\n")
        return

    print("\n----- ALL MOVIES & SHOWS -----")
    for i, item in enumerate(data, start=1):
        status = "Watched ✔" if item["watched"] else "Pending ❗"

        if item["type"] == "Movie":
            print(f"{i}. [MOVIE] {item['title']} ({item['year']}) - {item['duration']} - {item['genre']} - {status}")

        elif item["type"] == "Show":
            print(f"{i}. [SHOW] {item['title']} ({item['year']}) - {item['seasons']} Seasons, "
                  f"{item['episodes']} Episodes - {item['duration']} - {status}")
    print()


# ---------------- MARK AS WATCHED ----------------
def mark_watched(data):
    list_items(data)
    if data:
        num = int(input("Enter item number to mark as watched: ")) - 1
        if 0 <= num < len(data):
            data[num]["watched"] = True
            save_data(data)
            print("Item marked as watched!\n")
        else:
            print("Invalid selection.\n")


# ---------------- DELETE ITEM ----------------
def delete_item(data):
    list_items(data)
    if data:
        num = int(input("Enter item number to delete: ")) - 1
        if 0 <= num < len(data):
            removed = data.pop(num)
            save_data(data)
            print(f"Deleted: {removed['title']}\n")
        else:
            print("Invalid selection.\n")


# ---------------- SEARCH ----------------
def search_item(data):
    keyword = input("Enter keyword to search: ").lower()
    results = [item for item in data if keyword in item["title"].lower()]

    if not results:
        print("No matching items found.\n")
        return

    print("\n----- SEARCH RESULTS -----")
    for i, item in enumerate(results, start=1):
        status = "Watched ✔" if item["watched"] else "Pending ❗"

        if item["type"] == "Movie":
            print(f"{i}. [MOVIE] {item['title']} ({item['year']}) - {item['duration']} - {item['genre']} - {status}")

        else:
            print(f"{i}. [SHOW] {item['title']} ({item['year']}) - "
                  f"{item['seasons']} Seasons - {item['episodes']} Episodes - {item['duration']} - {status}")
    print()


# ---------------- MAIN MENU ----------------
def main():
    data = load_data()

    while True:
        print("\n=== Movies & Shows Management ===")
        print("1. Add Movie")
        print("2. Add Show")
        print("3. View All")
        print("4. Mark as Watched")
        print("5. Delete Movie/Show")
        print("6. Search")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_movie(data)
        elif choice == "2":
            add_show(data)
        elif choice == "3":
            list_items(data)
        elif choice == "4":
            mark_watched(data)
        elif choice == "5":
            delete_item(data)
        elif choice == "6":
            search_item(data)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()