from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Flask API is running!"})
    
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python API!"})

@app.route("/employee", methods=["GET"])
def get_employee():
    emp_id = request.args.get("emp_id", type=int)
    
    return jsonify({
        "id": emp_id,
        "name": f"User {emp_id}",
        "department": "IT",
        "email": f"user{emp_id}@company.com"
    })

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()

    product = data.get("product")
    quantity = data.get("quantity")
    price = data.get("price")

    total = quantity * price

    return jsonify({
        "product": product,
        "quantity": quantity,
        "total_price": total,
        "status": "Order created successfully"
    })


if __name__ == "__main__":
    # 這段只在你本機 python main.py 時會跑
    app.run(host="0.0.0.0", port=8000, debug=True)




