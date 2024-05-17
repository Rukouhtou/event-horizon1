sol1 = lambda x: True if x%2==0 else False

ex1 = 40
sol2 = lambda x=0: 'done' if sol1(ex1) else 'denied'
print(sol2())
