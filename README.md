# CLI Todo App 📝
## Features ✨

- ✅ Add, complete, and delete todos
- 🎯 Priority levels (low, medium, high)
- 💾 Persistent storage (JSON)
- 🎨 Beautiful CLI output with emojis
- ⚡ Fast and lightweight
- 🧪 Fully tested with pytest

## Installation 🚀

### From source

```bash
# Clone the repository
git clone https://github.com/yourusername/cli-todo-app.git
cd cli-todo-app

# Install dependencies
pip install -r requirements.txt

# Install the app
pip install -e .
```

### Using pip (once published)

```bash
pip install cli-todo-app
```

## Usage 📖

### Add a new todo

```bash
todo add "Buy groceries"
todo add "Finish project" -p high
todo add "Call mom" -p low
```

### List todos

```bash
# Show pending todos
todo list

# Show all todos (including completed)
todo list --all
```

### Complete a todo

```bash
todo complete 1
```

### Delete a todo

```bash
todo delete 2
```

### Clear completed todos

```bash
todo clear
```

## Development 🛠️

### Run tests

```bash
pytest test_todo.py -v
```

### Run tests with coverage

```bash
pytest test_todo.py --cov=todo --cov-report=html
```

### Check code quality

```bash
# Format code
black todo.py test_todo.py

# Lint code
flake8 todo.py test_todo.py

# Type checking
mypy todo.py
```

## CI/CD Pipeline 🔄

This project uses three GitHub Actions workflows:

### 1. Tests (`test.yml`)
- Runs on multiple OS (Ubuntu, Windows, macOS)
- Tests against Python 3.8, 3.9, 3.10, 3.11
- Generates coverage reports
- Uploads results to Codecov

### 2. Code Quality (`lint.yml`)
- Runs Flake8 for linting
- Checks formatting with Black
- Performs type checking with MyPy

### 3. Build and Release (`build.yml`)
- Builds distribution packages
- Creates GitHub releases on tags
- Publishes to PyPI (optional)

## Project Structure 📁

```
cli-todo-app/
├── .github/
│   └── workflows/
│       ├── test.yml       # CI Build 1: Tests
│       ├── lint.yml       # CI Build 2: Code Quality
│       └── build.yml      # CI Build 3: Build & Release
├── todo.py                # Main application
├── test_todo.py           # Unit tests
├── requirements.txt       # Dependencies
├── setup.py              # Package configuration
└── README.md             # This file
```

## Storage 💾

Todos are stored in `~/.todo/todos.json` by default.

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

All PRs must pass the CI checks:
- ✅ All tests passing
- ✅ Code quality checks passing
- ✅ Builds successfully

## License 📄

MIT License - feel free to use this project however you'd like!

## Author ✍️

Your Name - [@yourusername](https://github.com/yourusername)

---

Made with ❤️ and Python