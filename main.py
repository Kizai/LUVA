from src.record_audio import record_audio
from src.audio_to_text import audio_to_text
from src.execute_command import execute_command
from src.proxy import check_connectivity, configure_proxy
from src.get_translation import get_translation

# Check connectivity
if check_connectivity():
    print(get_translation('zh_CN', 'Cannot connect to Google. Please configure a proxy.'))
    proxy_url = input(get_translation('zh_CN', 'Enter your proxy URL: '))
    configure_proxy(proxy_url)

# Record audio
print(get_translation('zh_CN', 'Recording audio...'))
record_audio()

# Convert audio to text
print(get_translation('zh_CN', 'Converting audio to text...'))
try:
    command = audio_to_text('output.wav')
except Exception as e:
    print(get_translation('zh_CN', 'Failed to convert audio to text. Please try again.'))
    raise e

# Save command to a file
with open('command.txt', 'w') as f:
    f.write(command)

# Execute command
print(get_translation('zh_CN', 'Executing command...'))
command = execute_command(command)

# Send the command to the assistant
print(get_translation('zh_CN', 'Command:'), command)
