
# Getting Started with Flask-form-with-ajax Project

This README provides a comprehensive guide to setting up and running Flask application.

## Prerequisites

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Git version control system**: [Download Git](https://git-scm.com/)

## 1. Clone the Repository

To download the project files from the specified Git repository to your local machine, use the following command:

```sh
git clone https://github.com/manishpg83/flask.git
```

## Creating a Virtual Environment (Recommended)

Creating a virtual environment helps isolate project dependencies from your system-wide Python installation. This prevents conflicts and ensures consistency.

**Steps:**

1. **Create a Virtual Environment:**

   ```sh
   python -m venv venv  # Create virtual environment named "venv"
   ```

2. **Activate the virtual environment:**

   Depending on your operating system, use one of these commands to activate the "venv" environment:

   - Linux/macOS:

     ```sh
     source venv/bin/activate
     ```

   - Windows:

     ```sh
     venv\Scripts\activate.bat
     ```

3. **Install Project Dependencies:**

   Activate your virtual environment (if you created one). Then, install the required dependencies listed in the `requirements.txt` file:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   Start your Flask application by executing:

   ```sh
   python app.py
   ```
