This is a web application that displays the top Google Trends by region. It uses the Flask web framework for the backend and the PyTrends library to fetch trending searches from Google Trends.
Installation

    Clone this repository to your local machine:

    bash

git clone <repository_url>

Change to the project directory:

bash

cd <project_directory>

Create a virtual environment (optional but recommended):

bash

python -m venv venv

Activate the virtual environment:

    Windows (Command Prompt):

    bash

venv\Scripts\activate

Windows (PowerShell):

bash

.\venv\Scripts\Activate.ps1

macOS and Linux:

bash

    source venv/bin/activate

Install the required Python packages:

bash

    pip install -r requirements.txt

Usage

    Run the Flask application:

    bash

    python app.py

    Open your web browser and go to http://localhost:5000.

    You will see a loading modal while the application fetches Google Trends data for various regions. Once the data is loaded, it will be displayed on the page.

    The top trends for different regions will be listed on the page, organized by country.

Technologies Used

    Python
    Flask
    PyTrends
    HTML/CSS
    Bootstrap
