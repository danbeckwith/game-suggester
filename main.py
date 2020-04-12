from constants import GAME_PROJECT_ID, CONSOLES, KNOWN_TAGS
from todoist.api import TodoistAPI
from secrets import API_TOKEN

def buildGameObject(game):
    return { "id": game["id"], "labels": [labels.get(label_id) for label_id in game["labels"]] }

def getGameId(game):
    return game["content"]

def getLabelNameFromId(id):
    return labels.get("id")

def getLabels():
    return dict((label["id"], label["name"]) for label in api.state["labels"])

def getGames():
    return dict((getGameId(game), buildGameObject(game)) for game in games_from_api["items"])
    
api = TodoistAPI(API_TOKEN)
api.sync()
games_from_api = api.projects.get_data(GAME_PROJECT_ID)

labels = getLabels()




games = getGames()

print(games);