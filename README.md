# adhar-system-america
Finance Lead Manager 💼
A simple CRUD (Create, Read, Update, Delete) application for managing finance leads, built with Streamlit for the frontend and PostgreSQL for the backend.

Project Overview
This application serves as a tool for a finance lead manager to efficiently handle lead data. It demonstrates a practical implementation of a multi-tiered database architecture, separating the presentation layer (frontend), business logic (backend), and data storage (database). The app's key features include:

Lead Management: Perform all essential CRUD operations on lead records.

Data-Driven Insights: A dedicated section provides business intelligence by leveraging SQL aggregate functions.

Modular Design: The codebase is split into frontend.py and backend.py for clarity and maintainability.

Features
Create: Add new leads with details such as name, email, source, and status.

Read: Display a comprehensive list of all leads in a clean, tabular format.

Update: Modify existing lead information by selecting a lead ID.

Delete: Remove a lead record from the database.

Business Insights: Get a quick overview of lead data, including lead counts per source and overall metrics.

Technical Stack
Frontend: Streamlit

Backend: Python

Database: PostgreSQL

Database Connector: psycopg2

Setup and Installation
Follow these steps to set up the project locally.

1. Clone the Repository
Bash

git clone https://your-repository-url.git
cd your-repository-name
2. Set up the Python Environment
It's recommended to use a virtual environment.

Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate
3. Install Dependencies
Install the required Python libraries using pip.

Bash

pip install -r requirements.txt
Note: Create a requirements.txt file with the following content:

streamlit
psycopg2-binary
4. Configure the PostgreSQL Database
First, ensure you have PostgreSQL installed and running. Then, execute the following SQL command to create the necessary table and a hypothetical sales_data table for the insights section.

SQL

-- Create the main leads table
CREATE TABLE IF NOT EXISTS leads (
    lead_id SERIAL PRIMARY KEY,
    lead_name VARCHAR(255) NOT NULL,
    lead_email VARCHAR(255) UNIQUE NOT NULL,
    lead_source VARCHAR(50),
    lead_status VARCHAR(50) DEFAULT 'New'
);

-- (Optional) Create a hypothetical table for revenue insights
CREATE TABLE IF NOT EXISTS sales_data (
    sale_id SERIAL PRIMARY KEY,
    lead_id INT REFERENCES leads(lead_id),
    revenue DECIMAL(10, 2)
);

-- (Optional) Add some sample data for insights
INSERT INTO sales_data (lead_id, revenue) VALUES
(1, 150.00),
(2, 250.50),
(3, 100.25);
5. Update Database Credentials
Open the frontend.py and backend.py files and update the DB_CONFIG dictionary with your PostgreSQL credentials.

frontend.py

Python

DB_CONFIG = {
    "dbname": "finance_leads_db",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost"
}
backend.py

Python

DB_CONFIG = {
    "dbname": "finance_leads_db",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost"
}
Usage
To run the application, ensure your virtual environment is active and execute the following command in your terminal:

Bash

streamlit run frontend.py
This will open the application in your default web browser, allowing you to use the sidebar to navigate through the different CRUD operations and view business insights.
