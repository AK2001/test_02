

'''

~~~ΆΣΚΗΣΗ 3 ΣΤΟ ΜΑΘΗΜΑ FUNCTIONS~~~

def add_lists(list_a , list_b):
    combined_list = []
    for i in range(len(list_a)):
        combined_list.append(list_a[i]+list_b[i])
    return combined_list

list_1=[ ]
list_2=[ ]
length=int(input("How long are your lists? :"))
for _ in range(length):
    Ls1_values = int(input("please enter you numbers for the first list :"))
    list_1.append(Ls1_values)

for _ in range(length):
    Ls2_values=int(input("please enter you numbers for the second list :"))
    list_2.append(Ls2_values)

print(add_lists(list_1,list_2))
'''

'''

~~~ΑΣΚΗΣΗ 4 ΣΤΟ ΜΑΘΗΜΑ FUNCTIONS~~~

def add_lists(list_a , list_b,fraction="add"):
    combined_list = []
    if fraction=="subtract":
        for i in range(len(list_a)):
            combined_list.append(list_a[i] - list_b[i])
        return combined_list
    elif fraction=="multiply":
        for i in range(len(list_a)):
            combined_list.append(list_a[i] * list_b[i])
        return combined_list
    elif fraction=="divide":
        for i in range(len(list_a)):
            combined_list.append(list_a[i] / list_b[i])
        return combined_list
    else:
        for i in range(len(list_a)):
            combined_list.append(list_a[i] + list_b[i])
        return combined_list

list_1=[1,2,3,4]
list_2=[4,3,2,1]
fraction_=input("what fraction do you want to do:\nadd,subtruct,multiply or divide?")
print(add_lists(list_1,list_2,fraction_))


'''















