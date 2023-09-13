import unittest
from src.audio_to_text import audio_to_text


class TestAudioToText(unittest.TestCase):
    def test_audio_to_text(self):
        # Arrange
        filename = 'output.wav'
        expected_text = 'hello world'

        # Act
        actual_text = audio_to_text(filename)

        # Assert
        self.assertEqual(actual_text, expected_text)
