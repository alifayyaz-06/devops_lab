
import unittest
import tempfile
from pathlib import Path

from main import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_file = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.storage_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Complete assignment")

        self.assertEqual(task["title"], "Complete assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(task["id"], 1)

    def test_complete_task(self):
        task = self.manager.add_task("Study Python")

        completed = self.manager.complete_task(task["id"])

        self.assertTrue(completed["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Submit project")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.list_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
