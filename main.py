from pyfiglet import Figlet
from os import getenv, environ


# In GitHub Actions, environment variables from `action.yml` inputs are accessed via `os.environ`
# and inputs are automatically exported as env vars. You should use `getenv` for safety.
message = getenv('MESSAGE', 'Hello, World!')
f = Figlet(font='slant')
print(f.renderText(message))

