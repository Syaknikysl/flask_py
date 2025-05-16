from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample book database
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
]


# 1. Welcome message
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Book Library API!"})


# 2. Get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)


# 3. Get book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


# 4. Add new book
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if "title" not in data or "author" not in data or "year" not in data:
        return jsonify({"error": "Invalid request"}), 400

    new_id = max(b["id"] for b in books) + 1
    new_book = {"id": new_id, "title": data["title"], "author": data["author"], "year": data["year"]}
    books.append(new_book)

    return jsonify(new_book), 201


# 5. Render book list using Jinja2
@app.route('/books')
def render_books():
    return render_template('books.html', books=books)


if __name__ == "__main__":
    app.run(debug=True)
