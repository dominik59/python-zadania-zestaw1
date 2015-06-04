__author__ = 'Dominik'
"""
Program wypisujacy dlugosc slow wraz ze slowami do slownika
"""
list1=['orange' , 'apple', 'banana']
list2=('carrot' , 'potato', 'lettuce')
list3={'milk' , 'sugar', 'butter', 'flour'}

list4=[]
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)

list5={}

for i in range(0,len(list4)):
    if not len(list4[i]) in list5:
        list5[len(list4[i].capitalize())]=(list4[i].capitalize(),)
    else:
        list5[len(list4[i].capitalize())]+=(list4[i].capitalize(),)

print list5