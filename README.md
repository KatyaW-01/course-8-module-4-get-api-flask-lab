# Simple Products API

This is a basic Flask API that serves product data with filtering capabilities.

## Features

- Returns a welcome message at the root endpoint.
- Lists all products or filters products by category.
- Retrieves a product by its ID.

## Endpoints

### `GET /`

- Returns a simple welcome message.
- **Response Example**:
```json
{
  "message": "welcome"
}
```
### `GET /products/<id>`
- Returns a list of all products
- Optional query parameter: `category` - filters products by category
- **Example Request**:
```bash
GET /products?category=electronics
```
- **response example**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 899.99,
    "category": "electronics"
  }
]
```
### `GET /products/<id>`
- returns the product with the specified `id`
- **Example Request**:
```bash
GET /products/1
```
- **Response Example**:
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 899.99,
  "category": "electronics"
}
```
- returns `404 Not Found` if the product does not exist.

## How to Run
1. Make sure you have Python and Flask installed
2. Run the app:
  ```bash
    python app.py
  ```
3. Visit http://127.0.0.1:5000 in your browser or use an API client like Postman to test endpoints
