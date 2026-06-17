class CricketPlayer:
    team_size = 11
    def __init__(self,fname,lname,birth_year,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []
    def add_score(self,score):
        self.scores.append(score)

virat = CricketPlayer('virat','kohli',1988)
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
david= CricketPlayer('david','warner',1988)
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
        
        