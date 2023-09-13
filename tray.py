from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from src.record_audio import record_audio
from src.audio_to_text import audio_to_text
from src.execute_command import execute_command
from src.get_translation import get_translation
import interpreter
import os
import sys

# Create a Qt application
app = QApplication(sys.argv)

# Prevent the application from quitting when the last window is closed
app.setQuitOnLastWindowClosed(False)

# Create a tray icon
icon = QSystemTrayIcon(QIcon('icon.png'))

# Create a menu for the tray icon
menu = QMenu()

# Create an action for the menu
action = QAction(get_translation('zh_CN','Record'))


# Start recording when the action is triggered
def on_triggered():
    print(get_translation('zh_CN','Recording audio...'))
    record_audio()
    print(get_translation('zh_CN','Converting audio to text...'))
    try:
        command = audio_to_text('output.wav')
    except Exception as e:
        QMessageBox.critical(None, 'Error', get_translation('zh_CN','Failed to convert audio to text. Please try again.'))
        return
    print(get_translation('zh_CN','Executing command...'))
    command = execute_command(command)
    print('Command:', command)
    interpreter.chat(command)


# Set the action's triggered event
action.triggered.connect(on_triggered)

# Add the action to the menu
menu.addAction(action)

# Set the tray icon's menu
icon.setContextMenu(menu)

# Show the tray icon
icon.show()

# Run the Qt application
app.exec_()
