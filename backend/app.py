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

        # Define categories & keywords
        categories = {
            "Food": ["groceries", "resturaunt", "cafe"],
            "Entertainment": ["netflix", "movie", "cinema"],
            "Transport": ["uber", "taxi", "bus"],
            "Utilities": ["electricity", "water", "gas"],
        }

        # Function to categorize transactions
        def categorize(description):
            description = description.lower() # Conver to lowercase
            for category, keywords in categories.items():
                if any(keyword in description for keyword in keywords):
                    return category
            return "Other" # Default category if no match is found
        
        # Apply categoization to each row    
        data["Category"] = data["Description"].apply(categorize)

        # Calculate spending summaries
        category_totals = data.groupby("Category")["Amount"].sum().to_dict() # Total by category
        overall_total = data["Amount"].sum() # Total for all transactions

        # Build summary object 
        summary = {**category_totals, "Total": overall_total}

        # Return the processed data
        return jsonify({
            'message': 'File uploaded sucessfully', 
            'data': data.to_dict(orient='records'),
            'summary': summary
            }), 200

# Start app if file is run directly
if __name__ == '__main__':
    app.run(debug=True)