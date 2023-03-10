def find_max(numbers):
    max = 0
    for number in numbers:
        #number +=1
        if number > max:
            max = number
    return max        

def find_position(numbers, target): #找數字遊戲,找出數字並打印出他們的位置,如果無法找出請打印-1
    pos = 0 
    for number in numbers:
        if target == number : #第一個就找到&找到
            return pos
        else : #不是tartget繼續找
            pos +=1
    return -1

print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1