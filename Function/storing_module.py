'''
# importing an entire module
# description:This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program
import module_1
module_1.make_pizza(16,'pepproni')

module_1.make_pizza(12,'mushrooms','green pepper','extra cheese')

# imprting a specific functions
#synatx:from module_name import function_name

#we can import as many as function by sperating it with (,)
from module_1 import make_pizza
make_pizza(16,'pepronni')
make_pizza(12,'mushroom','gren pepper','extra cheese')

#3 giving a function an alias
#to avoid conflict in names bing called
from module_1 import make_pizza as mp
mp(34,'gobbi')
mp(14,'hari mirch','simla mirch','demak')

#4 we can also give alias to module name
import module_1 as m1
m1.make_pizza(12,'abc')
m1.make_pizza(45,'abc','bca','usd')

#5 we can also import all functin from module
#by using *

from module_1 import *
make_pizza(12,'abc')
make_pizza(15,'dhd','sds','ssd')
'''
#styling function

