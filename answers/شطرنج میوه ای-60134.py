def fruits(tuple_of_fruits):
  lst = list(tuple_of_fruits)
  lst2 ={}
  lst_test =[]  
  if str(type(tuple_of_fruits)) == "<class 'dict'>" :
     if (tuple_of_fruits.get("mass") > 100 and tuple_of_fruits.get("mass") < 600) and (tuple_of_fruits.get("volume") > 100 and tuple_of_fruits.get("volume") < 500 ) and (tuple_of_fruits.get("shape") == "sphere") :
        lst_test.append(tuple_of_fruits.get("name"))
        lst2[tuple_of_fruits.get("name")] = 1         
  else:  

    for i in lst[:]:
      if (i.get("mass") < 300 or i.get("mass") > 600) or (i.get("volume") < 100 or i.get("volume") > 500 ) :
        lst.remove(i)
      elif i.get("shape") == "sphere" :
        lst_test.append(i.get("name"))
        x = lst_test.count(i.get("name"))
        lst2[i.get("name")] = x 
    
  return lst2
#Erfan-Ebrahimkhani
#telegram : E-6434
# شکل آن به صورت کروی (sphere) باشد.
# جرم آن بین ۳۰۰ تا ۶۰۰ گرم باشد.
# حجم آن بین ۱۰۰ تا ۵۰۰ سانتی‌متر مکعب باشد.





