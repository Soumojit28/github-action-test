from pyfiglet import Figlet
from os import getenv, environ


message = environ["MESSAGE"]
f = Figlet(font='slant')
print(f.renderText(message))

