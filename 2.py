
data = input()

for i in range(len(data)):
    if (data[i].isdigit()):
        lastIndex = i
        break
        
elements = list(data[:i])
number = list(data[i:])

result = ''
while elements or number:
    if len(elements) > 1:
        element = elements.pop(0)
        if element.isupper() and elements[0].islower():
            result += (element + elements.pop(0))
        elif element.isupper() and elements[0].isupper():
            result += element
        else:
            break
    elif len(elements) == 1:
        element = elements.pop(0)
        if element.isupper():
            result += element
        else:
            break
    else:
        break

    if len(number) <=0:
        break
    if len(number) > 1 and number[0] == '1' and number[1] == '0':
        result += number.pop(0)
        result += number.pop(0)
    elif number[0] == '1':
        number.pop(0)
    else:
        result += number.pop(0)

    
if len(elements) > 0 or len(number) > 0:
    print('error')
else:
    print(result)
     