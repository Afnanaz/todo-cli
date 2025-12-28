"""
Unit tests for CLI Todo App
"""

import unittest
import json
import tempfile
from pathlib import Path
from todo import TodoApp


class TestTodoApp(unittest.TestCase):
    def setUp(self):
        """Create a temporary file for testing"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.app = TodoApp(data_file=self.temp_file.name)

    def tearDown(self):
        """Clean up temporary file"""
        Path(self.temp_file.name).unlink(missing_ok=True)

    def test_add_todo(self):
        """Test adding a todo"""
        todo = self.app.add("Test task", "high")
        self.assertEqual(todo['task'], "Test task")
        self.assertEqual(todo['priority'], "high")
        self.assertFalse(todo['completed'])
        self.assertEqual(len(self.app.todos), 1)

    def test_add_multiple_todos(self):
        """Test adding multiple todos"""
        self.app.add("Task 1", "low")
        self.app.add("Task 2", "medium")
        self.app.add("Task 3", "high")
        self.assertEqual(len(self.app.todos), 3)

    def test_complete_todo(self):
        """Test completing a todo"""
        self.app.add("Test task")
        self.app.complete(1)
        self.assertTrue(self.app.todos[0]['completed'])
        self.assertIn('completed_at', self.app.todos[0])

    def test_complete_nonexistent_todo(self):
        """Test completing a non-existent todo"""
        self.app.add("Test task")
        self.app.complete(999)  # Should not raise error
        self.assertFalse(self.app.todos[0]['completed'])

    def test_delete_todo(self):
        """Test deleting a todo"""
        self.app.add("Test task")
        self.assertEqual(len(self.app.todos), 1)
        self.app.delete(1)
        self.assertEqual(len(self.app.todos), 0)

    def test_clear_completed(self):
        """Test clearing completed todos"""
        self.app.add("Task 1")
        self.app.add("Task 2")
        self.app.add("Task 3")
        self.app.complete(1)
        self.app.complete(3)
        self.app.clear_completed()
        self.assertEqual(len(self.app.todos), 1)
        self.assertEqual(self.app.todos[0]['task'], "Task 2")

    def test_persistence(self):
        """Test that todos persist to file"""
        self.app.add("Persistent task")
        
        # Create new app instance with same file
        new_app = TodoApp(data_file=self.temp_file.name)
        self.assertEqual(len(new_app.todos), 1)
        self.assertEqual(new_app.todos[0]['task'], "Persistent task")

    def test_priority_levels(self):
        """Test different priority levels"""
        self.app.add("Low priority", "low")
        self.app.add("Medium priority", "medium")
        self.app.add("High priority", "high")
        
        self.assertEqual(self.app.todos[0]['priority'], "low")
        self.assertEqual(self.app.todos[1]['priority'], "medium")
        self.assertEqual(self.app.todos[2]['priority'], "high")

    def test_todo_ids(self):
        """Test that todo IDs are unique and sequential"""
        self.app.add("Task 1")
        self.app.add("Task 2")
        self.app.add("Task 3")
        
        self.assertEqual(self.app.todos[0]['id'], 1)
        self.assertEqual(self.app.todos[1]['id'], 2)
        self.assertEqual(self.app.todos[2]['id'], 3)


if __name__ == '__main__':
    unittest.main()