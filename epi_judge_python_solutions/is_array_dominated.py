import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0, team1):
        players_0 = []
        players_1 = []
        for player in team0._players:
            players_0.append(player.height)
        for player in team1._players:
            players_1.append(player.height)
        sorted0 = sorted(players_0)
        sorted1 = sorted(players_1)
        for i in range(len(sorted0)):
            if sorted0[i] - sorted1[i] >= 0:
                return False
        return True

@enable_executor_hook
def valid_placement_exists_wrapper(executor, team0, team1, expected_01,
                                   expected_10):
    t0, t1 = Team(team0), Team(team1)

    result_01 = executor.run(
        functools.partial(Team.valid_placement_exists, t0, t1))
    result_10 = executor.run(
        functools.partial(Team.valid_placement_exists, t1, t0))
    if result_01 != expected_01 or result_10 != expected_10:
        raise TestFailure("")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_array_dominated.py",
                                       'is_array_dominated.tsv',
                                       valid_placement_exists_wrapper))
