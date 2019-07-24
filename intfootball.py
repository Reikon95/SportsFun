import math

with open('Int_Football.csv') as results:
  
  match = results.readline()
  print(match)

  
  def total_matches_played():
    i = 0
    for elem in results:
      i += 1
    return 'The total number of international football matches played as of July 2019 is ' + str(i) + '. That works out to ' + str(int((i / (2019-1871)))) + ' per year on average.'

  def num_matches():
    i = 0
    for elem in results:
      i += 1
    return i

  
  print(total_matches_played())
  
  # def get_nation(country):
  #   i = 0
  #   for elem in results:
  #     elem.readline()
  #     print(elem)
  #   print('yes')
  #   return country + ' has played a total of ' + str(i) + ' international matches so far.'
  
  # print(get_nation('Scotland'))

  def split_em():
    i = 0
    home = []
    while i < 40:
      split_res = match.split(",")
      home.append(split_res[1])
      i += 1
    return home 
  print(split_em())
