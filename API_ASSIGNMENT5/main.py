from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics"},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery"}
]

orders = []
order_counter = 1

@app.get("/products/search")
def search_products(keyword: str = Query(...)):

    results = []

    # loop through products
    for p in products:
        if keyword.lower() in p["name"].lower():
            results.append(p)

    # if no products found
    if len(results) == 0:
        return {"message": f"No products found for: {keyword}"}

    return {
        "keyword": keyword,
        "total_found": len(results),
        "products": results
    }

@app.get("/products/sort")
def sort_products(
    sort_by: str = Query("price"),
    order: str = Query("asc")
):

    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}

    reverse = False
    if order == "desc":
        reverse = True

   
    sorted_products = sorted(products, key=lambda p: p[sort_by], reverse=reverse)

    return {
        "sort_by": sort_by,
        "order": order,
        "products": sorted_products
    }

@app.get("/products/page")
def paginate_products(
    page: int = Query(1, ge=1),
    limit: int = Query(2, ge=1)
):

    total = len(products)

    start = (page - 1) * limit

    paginated = products[start:start + limit]

    total_pages = -(-total // limit)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "products": paginated
    }


@app.post("/orders")
def create_order(customer_name: str):

    global order_counter

    order = {
        "order_id": order_counter,
        "customer_name": customer_name
    }

    orders.append(order)
    order_counter += 1

    return {
        "message": "Order created successfully",
        "order": order
    }

@app.get("/orders/search")
def search_orders(customer_name: str = Query(...)):

    results = []

   
    for o in orders:
        if customer_name.lower() in o["customer_name"].lower():
            results.append(o)

    if len(results) == 0:
        return {"message": f"No orders found for: {customer_name}"}

    return {
        "customer_name": customer_name,
        "total_found": len(results),
        "orders": results
    }

@app.get("/products/sort-by-category")
def sort_by_category():

    result = sorted(products, key=lambda p: (p["category"], p["price"]))

    return {
        "products": result,
        "total": len(result)
    }


@app.get("/products/browse")
def browse_products(
    keyword: str = Query(None),
    sort_by: str = Query("price"),
    order: str = Query("asc"),
    page: int = Query(1, ge=1),
    limit: int = Query(4, ge=1, le=20)
):

    result = products

    if keyword:
        filtered = []
        for p in result:
            if keyword.lower() in p["name"].lower():
                filtered.append(p)
        result = filtered

 
    if sort_by in ["price", "name"]:
        reverse = False
        if order == "desc":
            reverse = True

        result = sorted(result, key=lambda p: p[sort_by], reverse=reverse)


    total = len(result)

    start = (page - 1) * limit
    paginated = result[start:start + limit]

    total_pages = -(-total // limit)

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total,
        "total_pages": total_pages,
        "products": paginated
    }



@app.get("/orders/page")
def paginate_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1, le=20)
):

    total = len(orders)

    start = (page - 1) * limit
    paginated = orders[start:start + limit]

    total_pages = -(-total // limit)

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "orders": paginated
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for p in products:
        if p["id"] == product_id:
            return p

    raise HTTPException(status_code=404, detail="Product not found")
