# budget-tracker-tool

The **Budget Tracker Tool** is a Python-based API that processes CSV files containing financial transactions. It categorizes transactions, calculates spending summaries by category, and returns the data in JSON format. This tool is designed to simplify financial analysis and tracking.

---

## **Features**
- Accepts CSV files containing transactions.
- Automatically categorizes transactions based on descriptions (e.g., Groceries, Netflix).
- Provides spending summaries for each category and the overall total.
- Easy-to-use API for integration with other tools.
- Includes an API testing script for quick validation.

---

## **Folder Structure**
budget-tracker-tool/
│
├── backend/                # Flask API code
│   ├── app.py              # Main application file
│
├── testscripts/            # Testing utilities
│   ├── apitest.py          # Script to test the API
│
├── data/                   # Sample CSV files for testing
│   ├── sample.csv          # Example test file
│
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
├── README.md               # Project documentation

---

## **Set-up**

1) Clone Repository
    - git clone https://github.com/aelnimah/budget-tracker-tool.git
    - cd budget-tracker-tool

2) Set-up Virtual Environment
    - python -m venv venv
    - venv\Scripts\activate

3) Install Dependencies
    - pip install -r requirements

---

## **Using the API**

1) Start the Flask API
    - Navigate to the 'backend' directory: cd backend
    - Run the API: python app.py
    - The API will be accessible at: http://127.0.0.1:5000

---

## **Testing the API**

1) Run the test script
    - python testscripts/apitest.py

2) Provide Path to a CSV file
    - A sample CSV is provided in the data folder, feel free to edit it or use your own
    - To use the existing sample provide the path: data/sample.csv

3) Observe output
    - The script will send the file to the API and display the response, including transaction categories and spending summaries.

--- 

## **Future Development***
    * Deploy the API to AWS Elastic Beanstalk for global access.
    * Build a web app for visualizing transaction data.
    * Implement AI/ML for dynamic transaction categorization.
    * Enable linking to bank accounts.

---

## **Contact**
If you have any questions or feedback, feel free to reach out:
    - Email: elnimaha@gmail.com
    - GitHub: aelnimah