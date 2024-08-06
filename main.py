from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from chatbot.bot import Chatbot
from config import OPENAI_API_KEY, SECRET_KEY
from database.db_manager import DatabaseManager
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
app.secret_key = SECRET_KEY  # Set secret key for sessions

# Initialize chatbot and database manager
bot = Chatbot(OPENAI_API_KEY)
db = DatabaseManager()

UPLOAD_FOLDER = 'uploads'  # Define upload folder
ALLOWED_EXTENSIONS = {'pdf'}  # Allowed file extensions for upload

# Configure Flask app to use the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file is allowed based on its extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    if 'username' in session:  # Check if user is logged in
        return redirect(url_for('chatbot'))
    return render_template('index.html')  # Render the home page

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # If form is submitted
        username = request.form['username']
        password = request.form['password']
        if db.register_user(username, password):  # Attempt to register user
            return redirect(url_for('login'))
        return "Usuario ya existe"  # Inform user if username already exists
    return render_template('register.html')  # Render registration page

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # If form is submitted
        username = request.form['username']
        password = request.form['password']
        if db.verify_user(username, password):  # Verify user credentials
            session['username'] = username  # Store username in session
            return redirect(url_for('chatbot'))
        return "Credenciales inválidas"  # Inform user if credentials are invalid
    return render_template('login.html')  # Render login page

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('home'))  # Redirect to home page

# Route for chatbot page
@app.route('/chatbot')
def chatbot():
    if 'username' not in session:  # Check if user is not logged in
        return redirect(url_for('login'))
    return render_template('chatbot.html')  # Render chatbot page

# Route for chatting with the bot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Get JSON data from the request
    user_input = data.get('message')  # Extract message from the data
    context = data.get('context')  # Extract context from the data

    if not user_input:  # Check if message is provided
        return jsonify({"error": "No se proporcionó mensaje"}), 400

    try:
        response = bot.process_input(user_input, context)  # Process user input with the bot
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error if exception occurs

# Route for uploading PDFs
@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:  # Check if file is not part of the request
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']  # Get the file from the request
    if file.filename == '':  # Check if file is selected
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):  # Check if file is allowed
        filename = secure_filename(file.filename)  # Secure the filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Create file path
        file.save(file_path)  # Save the file
        try:
            content = bot.process_pdf(file_path)  # Process the PDF with the bot
            return jsonify({"message": content, "filename": filename})
        except Exception as e:
            return jsonify({"error": f"Error processing PDF: {str(e)}"}), 500  # Return error if exception occurs
    else:
        return jsonify({"error": "Archivo no válido"}), 400

# Main entry point
if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create upload folder if it doesn’t exist
    app.run(host='0.0.0.0', port=8080)  # Run the Flask app on port 8080