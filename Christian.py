def Sequence(N):
    list = [0]
    i = 1
    while(i<N+1):
        a = list[i - 1] -i
        if a  > 0 and a not in list: 
           list.append(list[i - 1] -i)
        else:
            list.append(list[i - 1] +i)
        i = i +1     # n += 1
    return list
