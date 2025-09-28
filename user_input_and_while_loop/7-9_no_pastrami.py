sandwich_orders=['aalo sandwich','pastrami','panner sandwich','pastrami','gobi sndwich','chicken sandwich','pastrami']
print("deli has ran rout of pastrami")
finished_orders=[]

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
for item in sandwich_orders:
    finished_orders.append(item)