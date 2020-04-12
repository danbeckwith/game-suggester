from constants import CONSOLES, KNOWN_TAGS
from secrets import API_TOKEN
from client import TodoistWrapper

api = TodoistWrapper(API_TOKEN)

games = api.getGames()

print(games)