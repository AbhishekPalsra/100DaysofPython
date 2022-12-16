import random   #python module
import my_module
a=1
b=90
randon_integer=random.randint(a,b)
print(randon_integer)
print(my_module.pi)
random_float=random.uniform(a,b)
print(random_float)
randon_float=random.random(); # float b [0,1)
print(5*randon_float); # bw [0,5)
love_score=random.randint(1,100)
print(f"your love score is {love_score}")