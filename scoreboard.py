import json
import os


class Scoreboard:
    scores: dict[str, int]

    def __init__(self):
        if not os.path.exists("scoreboard.json"):
            with open("scoreboard.json", "w") as scoreboard_file:
                scoreboard_file.write("{}")

        with open("scoreboard.json", "r") as scoreboard_file:
            self.scores = json.load(scoreboard_file)
        self._sort_scores()

    def save(self):
        self._sort_scores()
        with open("scoreboard.json", "w") as scoreboard_file:
            scoreboard_file.write(json.dumps(self.scores))

    def _sort_scores(self):
        r = [*self.scores.items()]
        for i in range(len(r) - 1):
            for j in range(i, len(r)):
                if r[j][1] < r[i][1]:
                    r[i], r[j] = r[j], r[i]
        self.scores = dict(r)
