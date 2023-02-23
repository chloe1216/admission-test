def count(input):
    str_key = []
    str_value = []
    for str in input:
        if str not in str_key : #如果沒有出現在str_key裡就把他放入
            str_key.append(str)
            str_value.append(1)
        else: #已經有在str_key,就把str_value++
            str_value[str_key.index(str)] +=1
    ans = dict(zip(str_key,str_value))
    return ans

        
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):
    tmp_list_of_key = []
    tmp_list_of_value = []
    for key in input: #轉為兩個list
        tmp_list_of_key.extend(list(key.get('key')))
        tmp_list_of_value.extend(list(str(key.get('value'))))
    tmp_list_of_value = list(map(int,tmp_list_of_value)) #str轉int
    keys = []
    values = []
    key_index = 0
    dup_index = 0
    for key in tmp_list_of_key:
        if key not in keys: #沒有出現過的key,value分別記下
            keys.append(key) 
            values.append(tmp_list_of_value[key_index])
        else: #遇到重複的key把value取出加總
            for dup in keys:
                if dup == key:
                    values[dup_index] += tmp_list_of_value[key_index]
                    dup_index = 0
                    break
                else :
                    dup_index+=1        

        key_index+=1

    ans = dict(zip(keys,values))
    return ans

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}

]

print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}