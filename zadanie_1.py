string1 = "79-900"
string2 = "80-155"

def code_generator(a,b):
    list_1 = []
    list_2 = []
    list_3 = []
    list_1.append(a)
    list_1.append(b)

    for x in list_1:
        list_2.append(int(x.replace('-', '')))

    for y in range(list_2[0],list_2[1]):
        list_2.append(str(y))

    list_2 = list(map(str, list_2))

    for z in list_2:
        
        a = z[0:2] + "-" + z[2:5]
        list_3.append(a)

    return list_3


code_generator(string1,string2)

print(code_generator(string1,string2))
    
