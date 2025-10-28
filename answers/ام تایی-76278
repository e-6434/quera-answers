def calculator(n, m, li):
    
    li2 = []
    ex = 0 # مخزن ذخیره نهایی
    q = 2 # زوج یا فرد بودن این عدد نشان دهنده علامت جمع یا تفریق است
    e = m
    t = 0 # برای برش حلقه
    a = n/m # a = تعداد   گروه


    if n%m != 0 :
      a+=1

    for i in range(int(a)):
      li2.append(sum(li[t:e]))
      t += m
      e += m

    for i in li2:
        if q%2 == 0:
          ex += i
        else:
          ex -= i  
        q += 1 
    return ex
   

#Erfan-Ebrahimkhani
#telegram : E-6434
# ‍‍calculator(n, m, li) 
# 
# n (تعداد اعضای لیست)
# 
# m (تعداد اعضای هر گروه) 
