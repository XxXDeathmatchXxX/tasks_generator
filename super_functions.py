import random
from tasks import stack_of_functions



def SuperFunction():
    a = random.choice(stack_of_functions)
    return a


a, b = SuperFunction()

print(b)
print("Ответ: ", a)