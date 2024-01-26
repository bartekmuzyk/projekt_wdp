import json
import os


class Scoreboard:
    scores: dict[str, int]

    def __init__(self, file: str = "scoreboard.json"):
        self.file = file

        if not os.path.exists(self.file):
            with open(self.file, "w") as scoreboard_file:
                scoreboard_file.write("{}")

        with open(self.file, "r") as scoreboard_file:
            self.scores = json.load(scoreboard_file)
        self._sort_scores()

    def save(self):
        self._sort_scores()
        with open(self.file, "w") as scoreboard_file:
            scoreboard_file.write(json.dumps(self.scores))

    def _sort_scores(self):
        r = [*self.scores.items()]
        for i in range(len(r) - 1):
            for j in range(i, len(r)):
                if r[j][1] < r[i][1]:
                    r[i], r[j] = r[j], r[i]
        self.scores = dict(r)
