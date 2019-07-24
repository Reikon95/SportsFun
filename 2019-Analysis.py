
with open('2019results.csv') as lines_doc:
  # for line in lines_doc.readlines():
    # print(line)
  
  def is_country_present(country):
    i = 0
    for line in lines_doc.readlines():
      if country in line:
        i += 1
        print(i)
    print(i)
    if i > 0:
      return 'Yes, ' + country + ' has played ' + str(i) + ' times this year.'
    else:
      return 'Nope. Either that is not a country or they have not played yet'
  
  print(is_country_present('Scotland'))
  

    def how_many_wins(country):
      if 'Yes' in is_counry_present(country):
        return country ' has won ' + str(x) ' out of ' str(x) + ' games.' 
      else:
        return 
    how_many_wins('scotland')
