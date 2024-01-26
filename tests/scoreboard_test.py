import json

from scoreboard import Scoreboard


def test_sort():
    scoreboard = Scoreboard("testing_scoreboard.json")
    scoreboard.scores = {"foo": 11, "bar": 23, "baz": 0, "test": 14}
    scoreboard._sort_scores()
    assert [*scoreboard.scores.keys()] == ["baz", "foo", "test", "bar"]


def test_write():
    scoreboard = Scoreboard("testing_scoreboard.json")
    scoreboard.scores = {"foo": 11, "bar": 23, "baz": 0, "test": 14}
    scoreboard.save()
    with open("testing_scoreboard.json", "r") as scoreboard_file:
        scoreboard_data = json.load(scoreboard_file)
    assert scoreboard_data == scoreboard.scores
