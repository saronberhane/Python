def minMax(num):
    if len(num) == 1 :
        return [num[0],num[0]]
    else:
        return [(min(num[0],minMax(num[1:])[0])) , (max(num[0],minMax(num[1:])[1]))]

print(minMax([1,7,-1,5,3]))

