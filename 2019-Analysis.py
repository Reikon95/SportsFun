with open('2019results.csv') as results:

  def is_country_present(country):
    matches = []
    for match in results.readlines():
      if country in match:
        matches.append(match)
    if len(matches) > 0:
      print('Yes, ' + country + ' has played ' + str(len(matches)) + ' times this year.')
      return True
    else:
      print('Nope. Either that is not a country or they have not played yet')
      return False  
      
    
  print(is_country_present('Scotland'))
  

  def get_match_list(country):
    matches = []
    for match in results.readlines():
      if country in match:
        matches.append(match)
    if len(matches) > 0:
      return matches
    else:
      return 'It appears this country has not played a match in 2019.'
  
  print(get_match_list('Scotland'))
