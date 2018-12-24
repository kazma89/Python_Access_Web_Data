import re
count = 0
file = open('regex_sum_161409.txt')
for line in file :
    num = re.findall('[0-9]+',line)
    for number in num:
        count = count + int(number)
        #print(number)
print(count)
