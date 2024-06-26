#Seven ways to show even numbers and odd numbers
#----------
# Beispiel 1: For Loop 
numbers = list(range(0,100))
even_numbers = []
odd_numbers = []
for x in numbers:
    if x%2==0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print (even_numbers)
print('-------')
print (odd_numbers)

#---------
# Beispiel 2
even_ = list(range(0,100,2))
odd_ = list(range(1,100,2))
print (even_)
print('-------')
print (odd_)

#---------
# Beispiel 3: List Comprehension (with if condition)
numbers = list(range(0,100))
even = [x for x in numbers if x % 2 ==0]
odd = [x for x in numbers if x % 2 !=0]
print (even)
print('-------')
print (odd)

#--------
# Beispiel 4: User Input (start and end range)
start = int(input('start N: '))
end = int(input('end N: '))
numbers = list(range(start,end))
even = [x for x in numbers if x % 2 ==0]
odd = [x for x in numbers if x % 2 !=0]
print (even)
print('-------')
print (odd)

#--------
# Beispiel 5: While Loop
x = 0
even = []
odd = []
while x<12 :
    if x % 2 ==0:
        even.append(x)
    else:    
        odd.append(x)
    x +=1

print(even)
print('------')
print(odd)

# --------
# Beispiel 6: Filter (with lambda function)
numbers = list(range(0,11))
even = filter(lambda n: n % 2 ==0, numbers)
print(list(even))

odd = filter(lambda n: n % 2 !=0, numbers)
print(list(odd))

# --------
# Beispiel 7: Bitwise Operator
numbers = list(range(0,11))
even = [x for x in numbers if x & 1 ==0]
odd = [x for x in numbers if x & 1 !=0]
print ('Even: ',even)
print('-------')
print ('Odd: ',odd)
