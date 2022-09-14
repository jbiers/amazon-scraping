import requests

webpage = requests.get('https://stackoverflow.com/questions/14604699/how-to-activate-virtualenv-in-linux')

print(webpage.content)