# This is your movie database (just a list for now)
movies = [
    {"id": 1, "title": "Spider-Man", "genre": "Action"},
    {"id": 2, "title": "The Lion King", "genre": "Animation"},
    {"id": 3, "title": "Frozen", "genre": "Animation"}
]

print("🎬 Welcome to MovieMate!")
print("Here are your movies:")

for movie in movies:
    print(f"- {movie['title']} ({movie['genre']})")

print("\nYour backend is working! 🎉")
