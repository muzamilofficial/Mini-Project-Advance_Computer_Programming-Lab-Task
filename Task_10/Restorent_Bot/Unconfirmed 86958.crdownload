from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["hello", "hi", "hey", "greet"]):
        return " Welcome to Bella Vista Restaurant! You can ask me about our <b>menu</b>, <b>timings</b>, <b>reservation</b>, <b>location</b>, <b>delivery</b>, or <b>specials</b>."

    elif any(word in user_input for word in ["menu", "food", "dish", "eat", "items"]):
        return " Our menu includes:<br>• <b>Starters:</b> Bruschetta, Soup of the Day<br>• <b>Mains:</b> Grilled Salmon, Pasta Alfredo, BBQ Ribs<br>• <b>Desserts:</b> Tiramisu, Cheesecake<br>• <b>Drinks:</b> Fresh Juices, Coffee, Mocktails"

    elif any(word in user_input for word in ["timing", "time", "open", "close", "hours"]):
        return " We are open:<br>• <b>Mon – Thu:</b> 12:00 PM – 10:00 PM<br>• <b>Fri – Sat:</b> 12:00 PM – 11:30 PM<br>• <b>Sunday:</b> 1:00 PM – 9:00 PM"

    elif any(word in user_input for word in ["reservation", "book", "table", "reserve", "booking"]):
        return " To make a reservation, call us at <b>+92-300-1234567</b> or visit our website. We recommend booking at least <b>2 hours in advance</b> for weekends."

    elif any(word in user_input for word in ["location", "address", "where", "find"]):
        return " We are located at <b>12 Gulberg III, Main Boulevard, Lahore</b>. Easily accessible via ride-share apps. Free parking available!"

    elif any(word in user_input for word in ["delivery", "order", "online", "home"]):
        return " We offer home delivery within a <b>10 km radius</b>. Order via our app or call <b>+92-311-9876543</b>. Minimum order: <b>Rs. 800</b>. Delivery time: <b>30–45 mins</b>."

    elif any(word in user_input for word in ["special", "offer", "deal", "discount", "today"]):
        return " Today's Specials:<br>• <b>Lunch Deal (12–3 PM):</b> Main + Drink for Rs. 999<br>• <b>Family Combo:</b> 4 Mains + 2 Desserts for Rs. 3,500<br>• <b>Happy Hour (5–7 PM):</b> 20% off on all beverages!"

    elif any(word in user_input for word in ["price", "cost", "fee", "rate", "cheap", "expensive"]):
        return " Our price range:<br>• Starters: Rs. 300 – 600<br>• Main Course: Rs. 700 – 1,800<br>• Desserts: Rs. 250 – 500<br>• Drinks: Rs. 150 – 400"

    elif any(word in user_input for word in ["wifi", "internet", "connect"]):
        return " Yes! We offer <b>free high-speed WiFi</b> to all our dine-in guests. Ask the staff for the password upon seating."

    elif any(word in user_input for word in ["bye", "goodbye", "thanks", "thank"]):
        return " Thank you for visiting Bella Vista! We hope to serve you soon. Have a wonderful day!"

    else:
        return " I'm not sure about that. You can ask me about our <b>menu</b>, <b>timings</b>, <b>reservation</b>, <b>location</b>, <b>delivery</b>, <b>specials</b>, or <b>prices</b>."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_response():
    user_message = request.form["msg"]
    reply = chatbot_reply(user_message)
    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(debug=True)
