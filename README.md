# Book Management System

A robust, production-ready Django application for managing a library of books. This project provides a full CRUD (Create, Read, Update, Delete) interface with search functionality, designed for efficient book archiving and retrieval.

## Description

The Book Management System is a streamlined web application built with Django that allows users to catalogue books with detailed metadata including author, journal, publisher, and publication date. It features a centralized dashboard with powerful search capabilities to filter through large collections effortlessly.

## Features

- **Full CRUD Operations**: Create, view, update, and delete book entries.
- **Advanced Search**: Filter books by name, author, journal, or publisher using the integrated search bar.
- **Detailed Metadata**: Track specific details such as `Description`, `Published Date`, and `Publisher`.
- **Responsive UI**: Clean and intuitive interface built with Django Templates.
- **Robust Backend**: Powered by Django 5.0 and Class-Based Views for scalability and maintainability.

## Tech Stack

- **Backend**: Python 3.x, Django 5.0
- **Database**: SQLite3 (Development)
- **Frontend**: Django Template Engine (HTML/CSS)
- **Environment Management**: Virtualenv

## Installation Guide

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SharifulIslamRony790/Book-Management.git
   cd "Book Management"
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - **Windows**:
     ```powershell
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:8000/list/`

## Usage Instructions

- **Viewing Books**: The home page displays all registered books.
- **Searching**: Use the search input on the list page to filter books by title, author, or publisher.
- **Adding a Book**: Navigate to `/create/` to add a new record.
- **Updating/Deleting**: Click on a book's detail view to access edit and delete options.

## Project Structure

```text
├── book/                  # Application-specific logic
│   ├── forms.py           # Book data validation and forms
│   ├── models.py          # Database schema (Book model)
│   ├── urls.py            # App-level routing
│   └── views.py           # CRUD logic (ListView, DetailView, etc.)
├── Config/                # Project configuration (settings, asgi, wsgi)
├── templates/             # HTML templates for the UI
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/list/` | GET | List all books with search support |
| `/create/` | GET/POST | Form to add a new book |
| `/details/<id>/` | GET | Detailed view of a specific book |
| `/update/<id>/` | GET/POST | Form to edit an existing book |
| `/delete/<id>/` | POST | Confirm and delete a book |

## Screenshots

![Dashboard Placeholder](https://via.placeholder.com/800x400?text=Book+Management+Dashboard)
*Note: Replace with actual screenshots of your running application.*

## Environment Variables

This project uses standard Django settings. For production deployment, ensure you configure:
- `DEBUG`: Set to `False`
- `SECRET_KEY`: Use a secure, random string
- `ALLOWED_HOSTS`: List of authorized domains

## Deployment on Render (with SQLite)

Follow these steps to deploy the project on Render using SQLite database:

1. **Push Code to GitHub**
   - Create a new repository on GitHub.
   - Run the following commands in your project directory:
     ```bash
     git init
     git add .
     git commit -m "Prepare for deployment"
     git remote add origin https://github.com/your-username/your-repo.git
     git push -u origin main
     ```

2. **Create Render Account**
   - Go to [render.com](https://render.com) and sign up for a free account.

3. **Create Web Service**
   - In the Render dashboard, click "New" > "Web Service".
   - Connect your GitHub repository.
   - Set the following:
     - **Runtime**: Python 3
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn Config.wsgi:application --bind 0.0.0.0:$PORT`

4. **Set Environment Variables**
   - In the web service settings, go to "Environment".
   - Add the following variables:
     - `DEBUG`: False
     - `SECRET_KEY`: A random string (e.g., `your-secure-secret-key`)
     - `ALLOWED_HOSTS`: your-app-name.onrender.com

5. **Deploy**
   - Click "Create Web Service" or "Manual Deploy" > "Deploy latest commit".
   - Wait for the build to complete.
   - Access your app at the provided URL (e.g., https://your-app-name.onrender.com/list/).

Note: SQLite data may not persist across deploys. For production, consider using PostgreSQL.

## Contributing Guidelines

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Author Information

**Shariful Islam Rony**
- GitHub: [SharifulIslamRony790](https://github.com/SharifulIslamRony790)
