__author__ = 'Dominik'
"""
Program wypisujacy slowa gdzie sa 2 takie same litery obok siebie
"""
list1=['orange', 'apple', 'banana']
list2=('carrot', 'potato', 'lettuce')
list3={'milk','sugar', 'butter', 'flour'}

list4=[]
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)

for i in list4:
    for k in range(0,len(i)-1):
        if(i[k]==i[k+1]):
            print i
