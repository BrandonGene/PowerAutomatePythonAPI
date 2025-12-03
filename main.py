from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------
# 全域錯誤處理
# -------------------------
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request", "message": str(e)}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found", "message": "The requested resource was not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500


# -------------------------
# API Routes
# -------------------------
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Flask API is running!"})

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python API!"})


# -------------------------
# GET /employee (Query: emp_id=)
# -------------------------
@app.route("/employee", methods=["GET"])
def get_employee():
    emp_id = request.args.get("emp_id", type=int)

    # ❗ 錯誤處理：emp_id 缺失或格式錯誤
    if emp_id is None:
        return jsonify({
            "error": "Missing or invalid parameter",
            "message": "emp_id (int) is required"
        }), 400

    # ❗ 這裡可加入查資料邏輯，如果找不到可回 404
    if emp_id <= 0:
        return jsonify({
            "error": "Employee Not Found",
            "message": f"No employee found with emp_id={emp_id}"
        }), 404

    return jsonify({
        "id": emp_id,
        "name": f"User {emp_id}",
        "department": "IT",
        "email": f"user{emp_id}@company.com"
    })


# -------------------------
# POST /order
# -------------------------
@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json(silent=True)

    # ❗ 錯誤處理：Body 不是 JSON
    if data is None:
        return jsonify({
            "error": "Invalid JSON",
            "message": "Request body must be valid JSON"
        }), 400

    product = data.get("product")
    quantity = data.get("quantity")
    price = data.get("price")

    # ❗ 錯誤處理：缺少欄位
    if not product or quantity is None or price is None:
        return jsonify({
            "error": "Missing required fields",
            "message": "Fields 'product', 'quantity', and 'price' are required"
        }), 400

    # ❗ 錯誤處理：型別錯誤
    try:
        quantity = float(quantity)
        price = float(price)
    except ValueError:
        return jsonify({
            "error": "Invalid Data Type",
            "message": "quantity and price must be numeric"
        }), 400

    # ❗ 錯誤處理：數值不能為負
    if quantity < 0 or price < 0:
        return jsonify({
            "error": "Invalid Value",
            "message": "quantity and price must be non-negative"
        }), 400

    total = quantity * price

    return jsonify({
        "product": product,
        "quantity": quantity,
        "total_price": total,
        "status": "Order created successfully"
    })


# -------------------------
# 主程式
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
