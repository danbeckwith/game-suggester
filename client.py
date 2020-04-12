from todoist.api import TodoistAPI
from constants import GAME_PROJECT_ID


class TodoistWrapper:
    def __init__(self, token):
        self.api = TodoistAPI(token)
        self.labels = dict((label["id"], label["name"]) for label in self.api.state["labels"])

    def buildGameObject(self, game):
        return {"id": game["id"], "labels": [self.labels.get(label_id) for label_id in game["labels"]]}

    def getGameId(self, game):
        return game["content"]

    def getLabelNameFromId(self, id):
        return self.labels.get("id")

    def getGames(self):
        games_from_api = self.api.projects.get_data(GAME_PROJECT_ID)
        return dict((self.getGameId(game), self.buildGameObject(game)) for game in games_from_api["items"])
