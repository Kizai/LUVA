import unittest
from src.execute_command import execute_command


class TestExecuteCommand(unittest.TestCase):
    def test_execute_command(self):
        # Arrange
        command = 'echo hello world'
        expected_output = 'hello world'

        # Act
        actual_output = execute_command(command)

        # Assert
        self.assertEqual(actual_output, expected_output)
