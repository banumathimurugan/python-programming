def is_isogram(string):
  if isinstance(string,str) and len(string)!=0:
    string=string.lower()
    if len(string)==len(set(string)):
      result=true
    else:
      result=false
  elif not string:
    result=false
  else:
        raise TypeError('Argument should be a string')
  return string,result
