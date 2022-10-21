    # -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Points = 0
        self.player2Points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Points += 1
        else:
            self.player2Points += 1
    
    def _is_draw_result(self):
        return self.player1Points == self.player2Points
        
    def _get_draw_score(self):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(self.player1Points, "Deuce")
    
    def _get_regular_score(self):
        regular_score = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }
        return f"{regular_score[self.player1Points]}-{regular_score[self.player2Points]}"

    def _is_regular_result(self):
        return self.player1Points < 4 and self.player2Points < 4

    def _is_advantage_result(self):
        return abs(self.player1Points - self.player2Points) == 1
    
    def _is_win_candidate(self):
        return abs(self.player1Points - self.player2Points) == 1
    
    def _get_advantage_score(self):
        minusResult = self.player1Points - self.player2Points
        if (minusResult == 1):
            return "Advantage " + self.player1Name
        return "Advantage " + self.player2Name

    def _get_win_score(self):
        minusResult = self.player1Points - self.player2Points

        if (minusResult >= 2):
            return "Win for " + self.player1Name
        return "Win for " + self.player2Name

    def score(self):
        if self._is_draw_result():
            return self._get_draw_score()
        
        if self._is_regular_result():
            return self._get_regular_score()

        if self._is_advantage_result():
            return self._get_advantage_score()
            
        return self._get_win_score()
        