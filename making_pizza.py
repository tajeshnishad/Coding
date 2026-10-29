# using modules
import pizza

pizza.make_pizza(16,'peproni')
pizza.make_pizza(12,'mushrooms','green peeper','xtra cheese')

from pizza import make_pizza
make_pizza(16,'butter chicken')

# using as to give a function an alias(Nick name)
from pizza import make_pizza as mp
mp(15,'butter paneer')

# using as to give a modul an alias(Nick name)
import pizza as p 
p.make_pizza(12,'extra cheese')

# importing all function in a module 
from pizza import *
make_pizza(20,'double cheese pizza')

from pizza import make_pizza
make_pizza(10,'blur cheery')