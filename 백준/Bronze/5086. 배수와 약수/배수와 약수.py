while True:
    try:
        n,m=map(int,input().split())
        if n==0 and m==0:
            exit()
        if n < m:
            if m%n==0: print("factor")
            else:
                print("neither")
        else:
            if n%m==0:
                print("multiple")
            else:
                print("neither")

    except:
        exit()