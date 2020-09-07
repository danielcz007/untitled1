
import sys
import yaml

print(sys.path)

list_tuidao1 = []
for i in range(4):
    list_tuidao1.append(i**2)
print(list_tuidao1)
tuidao1_reverse = list_tuidao1.reverse()
print(tuidao1_reverse)

list_tuidao2 = [i**2 for i in range(4)]
print(list_tuidao2)

list_tuidao3 = []
for i in range(4):
    if i!=0:
        list_tuidao3.append(i**2)
print(list_tuidao3)

list_tuidao4 = [i**2 for i in range(4) if i!=0]
print(list_tuidao4)



