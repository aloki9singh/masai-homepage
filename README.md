# masai-homepage
This is a collaborative project involving four members, aimed at creating a web application with a backend in Flask and a frontend using Svelte.
## Team Members
- Kapil:- Backend
- Alok:- Fronted
- Ajaya:- Fronted
- Virendra:- Backend

## Project Overview
This project implements a web application for user registration and authentication. It utilizes Flask for the backend server, MySQL for database management, and integrates Twilio for OTP verification. The frontend is developed using Svelte.

## Installation

### Backend Setup
- Ensure you have Python and pip installed on your system.
- Create a virtual environment:
  ```bash
   python -m venv venv
  ```
- Activate the virtual environment:
  ```bash
    venv\Scripts\activate
  ```
- Install required Python packages:
  ```bash
    pip install Flask Flask-Cors Flask-MySQLdb
  ```
- Set up MySQL database:
- Create a database named flask_app.
- Configure MySQL connection details in app.py.
- Install Twilio Python library:
   ```bash
     pip install twilio
   ```
- Set up a Twilio account and obtain account_sid, auth_token, and twilio_phone_number.

- Run the Flask application:
  ```bash
  python app.py
  ```

### Frontend Setup
- Install the Svelte in your system from the official documentation
- Start the Svelte development server:
  ```bash
  npm install
  ```
  ```bash
  npm run dev
  ```
## Usage
- Follow the on-screen instructions for user registration and authentication.

## Acknowledgments
Special thanks to the entire team for their hard work and dedication to the project.
 



