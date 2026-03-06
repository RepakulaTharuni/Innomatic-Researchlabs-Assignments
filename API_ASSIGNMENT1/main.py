from fastapi import FastAPI

app = FastAPI()

# Products List
products = [
    {"id": 1, "name": "Notebook", "price": 50, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Pen", "price": 10, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Headphones", "price": 1500, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Mouse", "price": 700, "category": "Electronics", "in_stock": False},

    # Q1 → Added products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]


# Root
@app.get("/")
def home():
    return {"message": "FastAPI Store API Running"}


# Show all products
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}


# Q2 → Category filter
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):

    result = [p for p in products if p["category"] == category_name]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }


# Q3 → In-stock products
@app.get("/products/instock")
def get_instock():

    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }


# Q4 → Store info
@app.get("/store/info")
def store_info():

    return {
        "store_name": "Tech & Stationery Store",
        "owner": "Tharuni",
        "total_products": len(products),
        "categories": ["Electronics", "Stationery"]
    }


# Q5 → Bonus (product by id)
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for p in products:
        if p["id"] == product_id:
            return p

    return {"error": "Product not found"}

    
