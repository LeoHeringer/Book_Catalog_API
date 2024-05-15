# Book Catalog API

This is a book catalog API developed with Django Rest Framework, aimed at managing book information such as title, author, release year, and edition number.

## Data Models

- `Book`:
  - `id` (auto-increment): Unique identifier for the book.
  - `name` (string): The title of the book.
  - `author_name` (string): The author's name.
  - `release_year` (integer): The year the book was first released.
  - `edition_number` (integer): The edition number of the book.
  - `type` (string): The category of the book (novel, manga, comic, etc.).
  - `genre` (string): The genre of the book.
  - `publisher` (string): The publisher's name.
  - `edition_year` (integer): The year of the book's edition release.
  - `edition_number` (integer): The edition number.

## API Usage

The API functionalities include:

- Listing all books in the catalog.
- Adding a new book to the catalog.
- Retrieving details of a specific book by ID.
- Retrieving details of books by their title, author, genre, type, or publisher.
- Updating information of an existing book.
- Deleting a specific book from the catalog.

## Supported HTTP Methods

The API supports the following HTTP methods:

- `GET`: Retrieve information.
- `POST`: Add new records.
- `PUT`: Update existing records.
- `DELETE`: Delete records.

## Request Examples

Here are some examples of how to use the API:

## List all books

## Add a new book

```json
POST /books/
{
  "name": "Book Name",
  "author_name": "Author Name",
  "release_year": 2023,
  "type": "Book",
  "genre": "Book Genre",
  "publisher": "Book Publisher",
  "edition_year": 2018,
  "edition_number": 1
}
```
## Retrieve details of a specific book
```json
GET /books/
```
## Update information of an existing book
```json
PUT /books/{id}/
{
"name": "New Book Name",
"author_name": "New Author Name"
...
}
```
## Delete a specific book
```json
DELETE /books/{id}/
```

This README provides an overview of the API and examples of its usage.
