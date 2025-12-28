#!/usr/bin/env python3
"""
CLI Todo App - Simple task management from command line
"""

import json
import argparse
from datetime import datetime
from pathlib import Path


class TodoApp:
    def __init__(self, data_file="todos.json"):
        """
        data_file:
        - bisa relative path (CLI usage)
        - bisa absolute path (unit testing with tempfile)
        """
        self.data_file = Path(data_file)

        # Buat folder parent jika ada (aman untuk tempfile)
        if self.data_file.parent:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)

        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from JSON file safely"""
        if not self.data_file.exists():
            return []

        # File ada tapi kosong → return list kosong
        if self.data_file.stat().st_size == 0:
            return []

        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.data_file, "w") as f:
            json.dump(self.todos, f, indent=2)

    def add(self, task, priority="medium"):
        """Add a new todo"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat(),
        }
        self.todos.append(todo)
        self.save_todos()
        return todo

    def list(self, show_all=True):
        """List todos"""
        if not self.todos:
            print("No todos found.")
            return

        todos_to_show = self.todos if show_all else [
            t for t in self.todos if not t["completed"]
        ]

        if not todos_to_show:
            print("No pending todos.")
            return

        for todo in todos_to_show:
            status = "✓" if todo["completed"] else "○"
            priority_emoji = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢",
            }.get(todo["priority"], "⚪")

            task = todo["task"]
            if todo["completed"]:
                task = f"\033[9m{task}\033[0m"

            print(f"{status} [{todo['id']}] {priority_emoji} {task}")

    def complete(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                todo["completed_at"] = datetime.now().isoformat()
                self.save_todos()
                return
        # Tidak error kalau ID tidak ada (sesuai test)

    def delete(self, todo_id):
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                self.todos.pop(i)
                self.save_todos()
                return
        # Tidak error kalau ID tidak ada

    def clear_completed(self):
        """Remove all completed todos"""
        self.todos = [t for t in self.todos if not t["completed"]]
        self.save_todos()


def main():
    parser = argparse.ArgumentParser(description="CLI Todo App")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add a todo")
    add_parser.add_argument("task")
    add_parser.add_argument(
        "-p", "--priority", choices=["low", "medium", "high"], default="medium"
    )

    # list
    list_parser = subparsers.add_parser("list", help="List todos")
    list_parser.add_argument("-a", "--all", action="store_true")

    # complete
    complete_parser = subparsers.add_parser("complete", help="Complete todo")
    complete_parser.add_argument("id", type=int)

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete todo")
    delete_parser.add_argument("id", type=int)

    # clear
    subparsers.add_parser("clear", help="Clear completed todos")

    args = parser.parse_args()
    app = TodoApp(Path.home() / ".todo" / "todos.json")

    if args.command == "add":
        app.add(args.task, args.priority)
    elif args.command == "list":
        app.list(show_all=args.all)
    elif args.command == "complete":
        app.complete(args.id)
    elif args.command == "delete":
        app.delete(args.id)
    elif args.command == "clear":
        app.clear_completed()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
