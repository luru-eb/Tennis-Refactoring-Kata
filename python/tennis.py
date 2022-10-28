    # -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        
    def won_point(self, playerName):
        if playerName == self.player1.name:
            self.player1.add_point()
        else:
            self.player2.add_point()
    
    def _is_draw_result(self):
        return self.player1.points == self.player2.points

    def _is_regular_result(self):
        return self.player1.points < 4 and self.player2.points < 4

    def _is_advantage_result(self):
        return abs(self.player1.points - self.player2.points) == 1

    def score(self):
        if self._is_draw_result():
            return DrawScore().score(self.player1, self.player2)
        
        if self._is_regular_result():
            return RegularScore().score(self.player1, self.player2)

        if self._is_advantage_result():
            return AdvantageScore().score(self.player1, self.player2)
            
        return WinScore().score(self.player1, self.player2)


class Referee:
    pass


class Score(ABC):
    
    @abstractmethod
    def score(self, player1, player2):
        pass


class DrawScore(Score):
    def score(self, player1, player2):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(player1.points, "Deuce")


class AdvantageScore(Score):
    def score(self, player1, player2):
        if (player1.points - player2.points == 1):
            return "Advantage " + player1.name
        return "Advantage " + player2.name


class RegularScore(Score):
    def score(self, player1, player2):
        regular_score = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }
        return f"{regular_score[player1.points]}-{regular_score[player2.points]}"


class WinScore(Score):
    def score(self, player1, player2):
        if (player1.points - player2.points >= 2):
            return "Win for " + player1.name
        return "Win for " + player2.name


class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_point(self):
        self.points+=1
