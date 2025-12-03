from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title = "Sample API for Custom Connector",
    description="This API is for Power Automate Custom Connector demo",
    version="1.0"
    )

class Order(BaseModel):
    product: str
    quantity: int
    price: float

@app.get("/hello")
def hello():
    return {"message": "Hello from Python API!"}

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    return{
        "id": emp_id,
        "name": f"User {emp_id}",
        "department": "IT",
        "email": f"user{emp_id}@company.com"
        }

@app.post("/order")
def create_order(order: Order):
    total = order.quantity * order.price
    return {
        "product": order.product,
        "quantity": order.quantity,
        "total_price": total,
        "status": "Order created successfully"
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)