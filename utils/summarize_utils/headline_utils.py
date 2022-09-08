def get_condition(condition):
  print('Updating condition for headline...')
  if condition:
    if 'healthy' in condition.lower():
        condition = 'healthy subjects'
        return condition
    else:  
        condition =  ' and '.join(condition.split('|'))
        return condition 
  else:
       'No condition avaialble'