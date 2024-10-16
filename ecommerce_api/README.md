# Django E-Commerce API

This is an e-commerce API built using Django Rest Framework. It allows managing customers, products, orders, and order items, with validations on fields such as weight and order date. The API handles multiple customers, each having multiple orders, and each order containing multiple products.

## Features
- CRUD operations for Customers, Products, Orders, and Order Items.
- Custom validation rules, including:
  - Customer and Product names must be unique.
  - Product weight must be a positive decimal value and not exceed 25kg.
  - The total weight of an order cannot exceed 150kg.
  - The order date cannot be in the past.
- Auto-generated order numbers (e.g., `ORD00001`, `ORD00002`, etc.).
- Query filters for listing orders by customer or product.

## API Endpoints

### Customers
- **List all customers**: `GET /api/customers/`
- **Create a new customer**: `POST /api/customers/`
- **Update an existing customer**: `PUT /api/customers/<id>/`
- **Delete a customer**: `DELETE /api/customers/<id>/`

### Products
- **List all products**: `GET /api/products/`
- **Create a new product**: `POST /api/products/`
- **Update an existing product**: `PUT /api/products/<id>/`
- **Delete a product**: `DELETE /api/products/<id>/`

### Orders
- **List all orders**: `GET /api/orders/`
- **Create a new order**: `POST /api/orders/`
- **Edit an order**: `PUT /api/orders/<id>/`
- **Delete an order**: `DELETE /api/orders/<id>/`
- **List orders by customer**: `GET /api/orders/?customer=CustomerName`
- **List orders by products**: `GET /api/orders/?products=Product1,Product2`

## Validations
- **Product weight**: Must be between 0 and 25kg.
- **Order total weight**: Must not exceed 150kg.
- **Order date**: Cannot be set in the past.

## Project Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-ecommerce-api.git
    cd django-ecommerce-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

## Testing

You can test the API using tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).

### Example Order Creation Payload

```json
{
    "customer": "f8367d6a-7d63-4d0e-86a5-2c892b80f151",
    "order_date": "2023-12-31",
    "address": "1234 Test Address",
    "order_item": [
        {
            "product": "442273df-f37f-4497-b188-32b0408d98b0",
            "quantity": 2
        },
        {
            "product": "0b315ca7-cdec-47bc-849a-b4d1ccde77e4",
            "quantity": 1
        }
    ]
}
