import math

with open('Int_Football.csv') as results:
  
  def total_matches_played():
    i = 0
    for elem in results:
      i += 1
    return 'The total number of international football matches played as of July 2019 is ' + str(i)

  
  print(total_matches_played())
  
  def get_nation(country):
    i = 0
    for elem in results:
      if elem == country:
        i += 1
    
    return country + ' has played a total of '+ str(i) + ' international matches so far.'
  print(get_nation('Gabon'))
