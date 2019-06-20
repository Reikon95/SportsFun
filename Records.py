#Calculate a team's win percentage, can be adapted not to include draws

def win_percentage(wins, losses, draws):
  return wins / (wins + losses + draws) * 100
print(win_percentage(5, 5))

#Calculate a team's loss percentage

def loss_percentage(wins, losses, draws):
  return losses / (wins + losses + draws) * 100
print(loss_percentage(5, 5))

#Player goalscoring records
def Goals_Per_Game(player, goals, games):
  Gpg = goals/games
  print(player + " has scored at a rate of " + str(Gpg) + " goals per game.")
  
        
def save_percentage(shots, saves):
  return saves / (saves + shots) * 100

        
def shot_percentage(shots, goals):
  return shots / (shots + shots) * 100

def shots_per_goal(shots, goals):
  Spg = goals/shots
  return Spg
