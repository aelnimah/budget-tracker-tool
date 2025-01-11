# Import libraries
from flask import Flask, request, jsonify # Flask used to build API
import pandas as pd # Pandas to read and process CSV files
import os # OS to handle file operations

# Set up the Flask app
app = Flask(__name__)

# Define folder to store uploaded files
UPLOAD_FOLDER = './data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# API endpoint to upload a file
@app.route('/upload', methods=['POST'])
def upload_file():
    # 400: http status code for "Bad Request"
    # 200: http status code for "OK successful"

    # Check if a file is included in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400 # Error if no file is provided
    
    # Retrieve file from request
    file = request.files['file']

    # Check if file has a name
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400 # Error if no file name
    
    # Save file and read as CSV
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath) # Save the file to the data folder
        data = pd.read_csv(filepath) # Read the file using Pandas
        return jsonify({'message': 'File uploaded sucessfully', 'data': data.to_dict(orient='records')}), 200
    
# Start app if file is run directly
if __name__ == '__main__':
    app.run(debug=True)