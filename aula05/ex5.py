def countDigits(str):
   count= 0
   for n in str:
      if n.isdigit() == True:
         count +=1
   return count