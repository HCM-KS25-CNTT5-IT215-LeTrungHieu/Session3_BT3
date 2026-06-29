from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "is_available": True,
        "year": 2022,
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "is_available": False,
        "year": 2021,
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "is_available": False,
        "year": 2020,
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "is_available": True,
        "year": 2008,
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "is_available": False,
        "year": 2019,
    },
]


@app.get("/health")
def check_health():
    return {"status": "success", "message": "Xin chao be iu"}


@app.get("/books")
def get_books():
    return {
        "status": "success",
        "message": "Lấy danh sách sách thành công",
        "data": books,
    }


@app.get("/books/available")
def get_available_books():
    available_books = [book for book in books if book["is_available"]]

    return {
        "status": "success",
        "message": "Lấy danh sách sách thành công",
        "data": available_books,
    }


@app.get("/books/borrowed")
def get_borrowed_books():
    borrowed_books = [book for book in books if not book["is_available"]]

    return {
        "status": "success",
        "message": "Lấy danh sách sách thành công",
        "data": borrowed_books,
    }


@app.get("/books/statistics")
def get_books_statistic():
    available_books = [book for book in books if book["is_available"]]
    borrowed_books = [book for book in books if not book["is_available"]]

    return {
        "status": "success",
        "message": "Lấy danh sách sách thành công",
        "data": {
            "total_books": len(books),
            "available_books": len(available_books),
            "borrowed_books": len(borrowed_books),
        },
    }


@app.get("/books/latest")
def get_latest_book():
    latest_book = max(books, key=lambda book: book["year"], default=None)

    if not latest_book:
        return {
            "status": "success",
            "message": "No books available",
        }

    return {
        "status": "success",
        "message": "Lấy danh sách sách thành công",
        "data": {"latest_book": latest_book},
    }
