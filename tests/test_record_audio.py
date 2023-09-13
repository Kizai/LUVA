import unittest
from src.record_audio import record_audio
import os


class TestRecordAudio(unittest.TestCase):
    def test_record_audio(self):
        # Arrange
        filename = 'output.wav'

        # Act
        record_audio()

        # Assert
        self.assertTrue(os.path.exists(filename))
