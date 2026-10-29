from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Simulated in-memory database for bookings
bookings_db = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/book', methods=['POST'])
def book_item():
    data = request.json
    booking_type = data.get('type') # 'ride' or 'stay'
    title = data.get('title')
    price = data.get('price')
    
    new_booking = {
        "id": len(bookings_db) + 1,
        "type": booking_type,
        "title": title,
        "price": price,
        "status": "Confirmed & Active"
    }
    bookings_db.append(new_booking)
    return jsonify({"success": True, "booking": new_booking})

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings_db)

if __name__ == '__main__':
    app.run(debug=True)