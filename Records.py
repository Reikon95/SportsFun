#Calculate a team's win percentage

def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
print(win_percentage(5, 5))
