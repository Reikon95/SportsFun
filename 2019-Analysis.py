import numpy as np
with open('2019results.csv') as results:
  results_total = results.readlines()

  def is_country_present(country):
    matches = []
    for match in results_total:
      if country in match:
        matches.append(match)
    if len(matches) > 0:
      print('Yes, ' + country + ' has played ' + str(len(matches)) + ' times this year.')
      return True
    else:
      print('Nope. Either that is not a country or they have not played yet')
      return False  
      
    
  is_country_present('Germany')
  

  def get_match_list(country):
    matches = []
    for match in results_total:
      if country in match:
        matches.append(match)
    if len(matches) > 0:
      i = 0
      for game in matches:
        print('Match ' + str(i+1) + ' ' + matches[i])
        i += 1
      return 'As of curent time, these are all the matches ' + country + ' has played this year'
    else:
      return 'It appears this country has not played a match in 2019.'
  
  get_match_list('Germany')

  matches_dic = {}

  def organise_matches():
    i = 1
    for match in results_total:
      matches_dic.update( {i : match} )
      i += 1  
  organise_matches()

  print(matches_dic[214])

  details = {}
  def split_details():
    i = 1
    for match in results_total:
      a = match.split(',')
      # details.update({i : a[0]})
      # details.update({i : a[1]})
      # details.update({i : a[2]})
      # details.update({i : a[3]})
      # details.update({i : a[4]})
      i += 1
  split_details()

  print(split_details[214])
