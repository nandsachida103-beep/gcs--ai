# app.py
from flask import Flask, request, jsonify
from data import school_data

app = Flask(__name__)

def get_response(msg):
    msg = msg.lower()

    # School basic info
    if "school name" in msg or "name of school" in msg:
        return f"Hello! I am Sinoy 🤖. The school name is {school_data['basic_details']['name']}."
    
    elif "timing" in msg or "school hours" in msg:
        general = school_data['basic_details']['school_timing']
        nursery = school_data['basic_details']['section_timing']['nursery_ukg']
        classi = school_data['basic_details']['section_timing']['class_i_xii']
        return f"School Timing: {general}. Nursery to UKG: {nursery}, Class I to XII: {classi}."

    elif "principal" in msg:
        return f"The principal is {school_data['management']['principal']}."
    
    elif "director" in msg:
        return f"The director is {school_data['management']['director']}."

    elif "fees" in msg:
        school_fee = "₹2000 per month"
        coaching_fee = "₹2000 per month"
        return f"Class 11 Fees → School Fee: {school_fee}, Coaching Fee: {coaching_fee}"

    elif "bus" in msg or "transport" in msg:
        response = "Transport Routes and Fees:\n"
        for route, fee in school_data['transport']['routes'].items():
            response += f"{route} – {'₹'+str(fee) if fee else 'Fee not specified'}\n"
        return response.strip()

    elif "science exhibition" in msg:
        se = school_data['science_exhibition']
        return f"Science Exhibition is on {se['date']}. Head: {se['head']}. Supporting Members: {', '.join(se['supporting_members'])}."

    elif "best player" in msg or "cricket" in msg or "volleyball" in msg:
        cricket = school_data['best_players']['all_time_cricket']
        volleyball = school_data['best_players']['all_time_volleyball']
        return f"Best players of all time → Cricket: {cricket}, Volleyball: {volleyball}"

    elif "address" in msg:
        return f"School Address: {school_data['address']}"

    elif "contact" in msg or "call" in msg or "phone" in msg:
        return f"Contact Numbers: {', '.join(school_data['contact_numbers'])}"

    # Fallback
    else:
        return school_data['contact_fallback']

# Home route
@app.route("/")
def home():
    return "Welcome to GCS AI 🤖 Chatbot! Use POST /chat with JSON {'message':'your question'}"

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message")
    if not msg:
        return jsonify({"response": "Please send a message."})
    
    response = get_response(msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
