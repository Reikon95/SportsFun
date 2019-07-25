with open('2019results.csv') as lines_doc:
  # for line in lines_doc.readlines():
    # print(line)
  
  def is_country_present(country):
    i = 0
    for line in lines_doc.readlines():
      if country in line:
        i += 1
    
    if i > 0:
      print('Yes, ' + country + ' has played ' + str(i) + ' times this year.')
      return True
    else:
      print('Nope. Either that is not a country or they have not played yet')
      return False
  
  print(is_country_present('Scotland'))
  

  def how_many_wins(country):
    if (1 + 1) == 2:
      return is_country_present(country)
    else:
      return 'something has gone horribly wrong here'
  print(how_many_wins('Scotland'))
