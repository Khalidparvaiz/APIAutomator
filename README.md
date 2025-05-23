# JSONPlaceholder CLI Client

A command-line Python application that interacts with the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake REST API.  
You can fetch, view, update, delete posts, and manage comments through simple terminal commands.

## 🚀 Features

- View all posts
- Show a specific post and its comments
- Add a comment to a post
- Update a post
- Delete a post via confirmation
- Interactive CLI with user-friendly prompts

## 🧰 Requirements

- Python 3.7 or higher
- `requests` library

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/jsonplaceholder-cli.git
cd jsonplaceholder-cli
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python api.py
```

You will see the list of posts and get a prompt like:

```
Available commands: SHOW, LIST, UPDATE, DELETE, QUIT
Enter a command:
```

Follow the instructions to manage posts.

## 📝 Example Commands

- `LIST` — show all posts again
- `SHOW` — view a specific post and its comments
- `UPDATE` — change title/body of a post
- `DELETE` — delete a post after confirmation
- `QUIT` — exit the app

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
