class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string.")
        self.title = title
    
    @property
    def title(self):
        return self.title

    def results(self):
        return [result for result in Result.all() if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores) if scores else 0

class Player:
    def __init__(self, username):
        if not isinstance(username, str) or len(username) == 0:
            raise Exception("Username must be a non-empty string.")
        self.username = username
        
    @property
    def username(self):
        return self.username
    

    def results(self):
        return [result for result in Result.all() if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results()if result.game == game])
    @classmethod
    def highest_scored(cls, game):
        players = game.players()
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))

class Result:
    _all_results = []
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise Exception("Player must be a valid Player instance")
        
        if not isinstance(game, Game):
            raise Exception("Game must be a valid Game instance")
    
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise Exception("Score must be an integer between 1 and 5000")
        self.player = player
        self.game = game
        self.score = score
        
    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score

    @classmethod
    def all(cls):
        return cls._all_results