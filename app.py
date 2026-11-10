from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This serves as our temporary database setup
EVENTS_DATABASE = [
    {
        "id": 1,
        "title": "Tech Conference 2026",
        "location": "Bengaluru, India",
        "tickets_left": 5,
        "status": "Available"
    },
    {
        "id": 2,
        "title": "AI & ML Innovation Summit",
        "location": "Virtual / Online",
        "tickets_left": 0,
        "status": "Sold Out"
    }
]

@app.route('/')
def home():
    # Sending the live Python list directly to our HTML layout
    return render_template('index.html', events=EVENTS_DATABASE)

# Action endpoint to process a ticket purchase
@app.route('/book/<int:event_id>', methods=['POST'])
def book_ticket(event_id):
    for event in EVENTS_DATABASE:
        if event["id"] == event_id:
            if event["tickets_left"] > 0:
                event["tickets_left"] -= 1
                if event["tickets_left"] == 0:
                    event["status"] = "Sold Out"
    return redirect(url_for('home'))

# Action endpoint to add a new event from the form
@app.route('/add-event', methods=['POST'])
def add_event():
    title = request.form.get('title')
    location = request.form.get('location')
    tickets = int(request.form.get('tickets', 0))
    
    new_event = {
        "id": len(EVENTS_DATABASE) + 1,
        "title": title,
        "location": location,
        "tickets_left": tickets,
        "status": "Available"
    }
    
    EVENTS_DATABASE.append(new_event)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)