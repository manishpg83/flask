# flask
Getting Started with Flask Project

This README provides a comprehensive guide to setting up and running your Flask application.

Prerequisites:

Python 3.x (https://www.python.org/downloads/)
Git version control system (https://git-scm.com/)

1. Clone the Repository:
git clone https://github.com/manishpg83/flask.git
This command will download the project files from the specified Git repository to your local machine.


2. Create a Virtual Environment (Recommended):
Creating a virtual environment helps isolate project dependencies from your system-wide Python installation. This can prevent conflicts and ensure consistency. Here's an example using venv:

python -m venv venv
cd venv
source bin/activate  # Windows: venv\Scripts\activate.bat
->This will create a new virtual environment named "venv" and activate it.

3. Install Project Dependencies:
Activate your virtual environment (if you created one). Then, install the required dependencies listed in the requirements.txt file:

pip install -r requirements.txt

4. Run the Application:
Start your Flask application by executing:

python app.py