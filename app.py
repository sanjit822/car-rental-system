from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

# Route for the Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for the Booking page
@app.route('/booking')
def booking():
    return render_template('booking.html')

# Route for the Repairs page
@app.route('/repair')
def repair():
    return render_template('repair.html')

# Route for the Maintenance page
@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Route for the Admin page (for admin functionalities)
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Route for Service Request Modal (Handle POST request for the modal)
@app.route('/request_service', methods=['POST'])
def request_service():
    # Get data from the modal form
    name = request.form.get('name')
    email = request.form.get('email')
    service_details = request.form.get('service_details')

    if name and email and service_details:
        # Logic to store the service request (could be a database or just an email)
        flash(f"Thank you {name}, your request for the service has been submitted.", "success")
        return redirect(url_for('services'))
    else:
        flash("Please fill in all fields.", "error")
        return redirect(url_for('services'))

# Route for the Dashboard page (Optional, for admin or user dashboard)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for Payment page
@app.route('/payment')
def payment():
    return render_template('payment.html')

# Route for the Rent page
@app.route('/rent')
def rent():
    return render_template('rent.html')

if __name__ == '__main__':
    app.run(debug=True)
