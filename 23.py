for n in range(199,100,-2):
    for i in range(3,int(n**(1/2))+1,2):
        if n % i == 0:
            break
    else:
        print(f'200以内最大素数是{n}')
        break