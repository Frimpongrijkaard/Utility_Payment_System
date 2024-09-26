# Utility_Payment_System
Final research and project approval app which is softpayout

This project aims to develop an automated utility payment system that allows customers to pay theirutility bills (such as electrricty, water, and gas) throughh an online application.
The application serves as digital platform for a utility company, enabling customers to manage their utility accounts, make payments, and view payment history without the need to visit the company office.

Live Demo: not yet Deployed Site Link

Project Blog: https://lnkd.in/dsZNHX7G

## Project Goals:
1. Ease of Access: allow customers to pay their utility bilss online anytime, anywhere.

2. Payment History:Provides customers with a detailed history of all payment made to utility services

3. Account Management: Enable customers to manage their utility account, view outstanding balances, and receive notifcation about due payments.

4. Security: Ensure that customer data and transactions are secure, with proper authentication and encryption.

## Features

User Registration & Login: Secure registration and login using hashed passwords.

Profile Management: Users can update their personal and account information.

Utility Management: View utility providers, outstanding bills, and make payments.

Responsive Design: Mobile-first design for seamless usage on all devices.

Admin Dashboard: Admins can view all users and utility payment information.


## Installation
    To run this project locally, follow these steps:

## Prerequisites
    Ensure you have the following installed:


Python 3.x

Flask

SQLAlchemy

MySQL or SQLite

Virtualenv

### Step-by-step Installation

    Clone the Repository:

        git clone https://github.com/yourusername/utility-payment-system.git

    Navigate to the Project Directory:

        cd utility-payment-system

    Create a Virtual Environment:

        python3 -m venv venv
        source venv/bin/activate  # For Linux/MacOS
        venv\Scripts\activate
    


    Install Dependencies:

        pip install -r requirements.txt


    Set Up the Database:

        Open config.py and configure your database settings.
        Run the migrations or create the database:

        python manage.py db upgrade
    

    Run the Application:
        flask run


## Usage
    
    User Registration
        Navigate to the registration page and fill out the form with your full name, email, password, phone number, and address.
        After successful registration, you can log in with your credentials.

    Login
        Enter your email and password on the login page.
        Once authenticated, you'll be redirected to your dashboard, where you can manage your utilities and make payments.

    Profile Management
        In your dashboard, navigate to the profile section.
        Here, you can update your email, password, phone number, and address.

    Admin Usage
        Admins can access the admin panel to view all users, manage utility providers, and see payment histories.



## Contributing
        We welcome contributions to enhance the Utility Payment System. Here’s how you can help:

    Fork the repository: Click the "Fork" button at the top right of this page.

    Clone your fork:

        
        git clone https://github.com/yourusername/utility-payment-system.git
    
    Create a new branch:


        git checkout -b feature-branch
    
    Make changes: Add your code.

    Commit changes:


        git commit -m "Your commit message"

    Push to the branch:


        git push origin feature-branch
    
    Submit a Pull Request: From your forked repository, click the "Pull Request" button.

We will review your request, provide feedback, and merge it into the main project if everything looks good.

## Related Projects
    Here are some projects related to the Utility Payment System that might interest you:

    Payment Gateway API
    Utility Management System


## Licensing
    This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
        For further inquiries or collaboration requests, feel free to reach out to the authors:

    Author 1  https://www.linkedin.com/in/frimpong-rijkaard-06045a216/
    Author 2 http://www.linkedin.com/in/nyo-tek-93703532b

