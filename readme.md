# NetGrab

NetGrab is a Django-based web scraper designed to fetch all hyperlinks (`<a>` tags) from a given website and display them in a clean, responsive table. This tool uses BeautifulSoup for web scraping and Tailwind CSS for styling, offering a seamless and efficient user experience.

## Features

- Fetches and stores all links from any provided website.
- Displays links with their names and URLs in a tabular format.
- Allows users to delete all stored links with a single click.
- Simple, responsive design with Tailwind CSS.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Web Scraping:** BeautifulSoup
- **Database:** Django's default SQLite (can be replaced with other DB engines)
- **HTTP Requests:** `requests` library


## Installation

Follow these steps to run NetGrab locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/chriswilder3/netgrab.git
   cd netgrab
    ```
2. Set up a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

6. Open the app in your browser:
    http://127.0.0.1:8000