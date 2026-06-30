import random
import requests
from app.database import SessionLocal, Base, engine
from app.models.book import Book

categories = [
    "Fiction",
    "Fantasy",
    "Mystery",
    "Romance",
    "Thriller",
    "History",
    "Biography",
    "Programming",
    "Business",
    "Poetry",
    "Travel",
]

def fetch_and_seed_openlibrary(search_queries=categories, limit=10):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    total_added = 0

    for query in search_queries:
        api_url = f"https://openlibrary.org/search.json?title={query}&limit={limit}"
        print(f"Connecting to: {api_url}")

        response = requests.get(api_url)
        if response.status_code != 200:
            print(f"Failed to fetch data for '{query}'")
            continue

        data = response.json()
        docs = data.get("docs", [])

        for doc in docs:
            title = doc.get("title")
            if not title:
                continue  # skip junk entries with no title

            authors_list = doc.get("author_name", ["Unknown Author"])
            authors = ", ".join(authors_list)

            price = round(random.uniform(12.99, 39.99), 2)

            first_sentence = doc.get("first_sentence")
            if isinstance(first_sentence, list):
                first_sentence = first_sentence[0] if first_sentence else None

            if first_sentence:
                description = first_sentence
            else:
                subjects = ", ".join(doc.get("subject", [])[:5])
                if subjects:
                    description = f"A book covering topics like: {subjects}."
                else:
                    year = doc.get("first_publish_year")
                    description = f"Published in {year}." if year else "No summary available."
            description = str(description)[:500]

            # ✅ correct OpenLibrary covers URL
            cover_id = doc.get("cover_i")
            if cover_id:
                image_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            else:
                image_url = "https://placehold.co/400x600?text=No+Cover"

            genre = query.capitalize()
            stock = random.randint(5, 30)

            db_book = Book(
                title       = title,
                author      = authors,
                description = description,
                price       = price,
                image_url   = image_url,
                genre       = genre,
                stock       = stock,
            )
            db.add(db_book)
            total_added += 1

        db.commit()  # commit per query, so one bad batch doesn't lose everything

    db.close()
    print(f"Successfully populated database with {total_added} OpenLibrary books.")


if __name__ == "__main__":
    categories = [
    "Fiction",
    "Fantasy",
    "Mystery",
    "Romance",
    "Thriller",
    "History",
    "Biography",
    "Programming",
    "Business",
    "Poetry",
    "Travel",
]
    fetch_and_seed_openlibrary(search_queries=categories, limit=10)