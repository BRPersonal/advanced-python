import bisect

"""
Maintain a high-score leaderboard that stays sorted
in descending orde of score
"""
class LeaderBoard:
    def __init__(self):
        self.scores = []
        self.players = []

    def add_score(self, player, score):
        # Insert maintaining descending order
        pos = bisect.bisect_left([-s for s in self.scores], -score)
        self.scores.insert(pos, score)
        self.players.insert(pos, player)

    def top_players(self, n=5):
        return list(zip(self.players[:n], self.scores[:n]))