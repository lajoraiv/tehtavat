from pointkeeping import PointKeeping

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1  

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = PointKeeping.score_text_tied(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = PointKeeping.score_text_advantage(self.m_score1, self.m_score2)
        else:
            score = PointKeeping.score_text(self.m_score1, self.m_score2)

        return score
    
