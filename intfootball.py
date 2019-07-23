import math

with open('Int_Football.csv') as results:
  
  match = results.readline()
  print(match)

  
  def total_matches_played():
    i = 0
    for elem in results:
      i += 1
    return 'The total number of international football matches played as of July 2019 is ' + str(i)

  
  print(total_matches_played())
  
  # def get_nation(country):
  #   i = 0
  #   for elem in results:
  #     elem.readline()
  #     print(elem)
  #   print('yes')
  #   return country + ' has played a total of ' + str(i) + ' international matches so far.'
  
  # print(get_nation('Scotland'))

  # def nation ():
  #   i = 0
  #   for line in results.readlines():
  #     if '1883-03-10,England,Scotland,2,3,Friendly,Sheffield,England,FALSE' in line:
  #       i += 1
  #     else:
  #       continue 
  #   return i
  # print(nation())

