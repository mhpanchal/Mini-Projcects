# 456 = [6, 5, 4]
# 246 = [6, 4, 2]
# 456 + 246 = 702 --> output = [2, 0, 7]

def sum_list(l1, l2):
    carry = 0
    lst = []

    for i in range(len(lst1)) :

        if l1[i] + l2[i] > 9 :
            ele = (l1[i] + l2[i]) % 10
            if carry == 0 :
                lst.append(ele)
            else :
                lst.append(ele + 1)

            carry = 1

        if l1[i] + l2[i] == 9 :
            if carry == 0 :
                lst.append(9)
            else :
                lst.append(0)

            carry = l1[i] // l2[i]
                
        elif l1[i] + l2[i] < 9 :
            if carry == 0 :
                lst.append(l1[i] + l2[i])
            else :
                lst.append(l1[i] + l2[i] + 1)

    return lst

lst1 = [int(i) for i in input("Enter the elements of List 1 : ").split()]
lst2 = [int(i) for i in input("Enter the elements of List 2 : ").split()]

if len(lst1) < len(lst2) :
    lst1, lst2 = lst2, lst1

if len(lst1) > len(lst2) :
    lst2.reverse()

    for i in range(len(lst1) - len(lst2)):
        lst2.append(0)

    lst2.reverse()

print("\nList 1 - ", lst1)
print("List 2 - ", lst2)
print("Sum of Lists - ", sum_list(lst1, lst2))
