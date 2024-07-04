# EveryDay G.I.T.A Challenge

The EveryDay G.I.T.A Challenge web application allows participants to upload their images, recordings, and personal details, which are then displayed on the website grouped by chapters.

## Features

- Upload participant's image, recording (MP3, M4A, or YouTube URL), and personal details.
- Display uploaded content grouped by chapters.
- Separate routes for upload form and content display.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:

    ```sh
    git clone <repository_url>
    cd everyones-gita
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install Flask Flask-SQLAlchemy
    ```

4. **Set up the project structure**:

    Ensure your project directory looks like this:

    ```
    everyones-gita/
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   └── upload.html
    ├── static/
    │   └── uploads/
    └── uploads.db
    ```

### Running the Application

1. **Start the Flask application**:

    ```sh
    python app.py
    ```

2. **Visit the following URLs** in your web browser:
    - Upload Form: `http://127.0.0.1:5000/upload`
    - Display Uploaded Content: `http://127.0.0.1:5000/`

### Clearing the Database

To clear the database of previous uploads, you can use the `/clear_db` route. This is useful for development purposes but should be removed or protected in a production environment.

Send a POST request to this route:

```sh
curl -X POST http://127.0.0.1:5000/clear_db


