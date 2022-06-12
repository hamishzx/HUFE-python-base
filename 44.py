def receive(lst):
    li=[]
    li.append(sum(lst))
    avrg = sum(lst)/len(lst)
    li.append(avrg)
    return li
lst = list(map(int,input().strip().split(" ")))
tp = tuple(receive(lst))
print(tp)