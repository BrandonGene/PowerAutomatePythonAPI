from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python API!"})

@app.route("/employee/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
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

