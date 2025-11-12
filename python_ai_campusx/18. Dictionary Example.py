L1="""I don't care if it hurts
I wanna have control
I want a perfect body
I want a perfect soul
I want you to notice
When I'm not around
You're so fuckin' special
I wish I was special
"""
L=L1.split()
D={}
for i in L:
    if i in D:
        D[i] = D[i] + 1
    else:
        D[i] = 1
m=(max(D.values()))
for i in D:
    if D[i]==m:
        print(i)
    