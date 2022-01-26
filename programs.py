
from statistics import mode
import string


#first problem

def most_num(data):
    return mode(data)
values = [1,2,66,7,1,7,90,7]
result =most_num(values)
print(result)

#second problem

def freq_num(data):
    num1= mode(data)
    data.remove(num1)
    num2 = mode(data)
    return num1,num2
values = [1,2,66,7,1,7,90,7]
result =freq_num(values)
print(result)

#third problem

def delete(data):
    str_out = []
    for i in data:
        if type(i)==str:
            str_out.append(i)
    return str_out    

elements = [1,2,"number",55,"string","boolean",33.33,True]
output = delete(elements)
print(output)

