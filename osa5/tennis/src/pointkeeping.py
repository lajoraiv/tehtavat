class PointKeeping:

    def score_text_tied(points):
        if points == 0:
                return "Love-All"
        if points == 1:
                return "Fifteen-All"
        if points == 2:
                return "Thirty-All"
        return "Deuce"
    
    def score_text_advantage(player1points, player2points):
            point_difference = player1points - player2points

            if point_difference == 1:
                return "Advantage player1"
            elif point_difference == -1:
                return "Advantage player2"
            elif point_difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
            
    def score_text(player1points, player2points):
            temp_score = str(player1points) + "-" + str(player2points)

            temp_score = temp_score.replace("0", "Love")
            temp_score = temp_score.replace("1", "Fifteen")
            temp_score = temp_score.replace("2", "Thirty")
            temp_score = temp_score.replace("3", "Forty")

            return temp_score
