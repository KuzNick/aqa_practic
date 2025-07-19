from random import randint
import time

class Loops:
    def __init__(self):
        pass
    
    def loop_of_numbers(self, start:int, end:int):
        numbers:list = [x for x in range(start, end)]
        
        for i in numbers:
            if i == 5:
                break
            
            print(f"Число - {i}")
            
            
    def loop_of_strings(self, number:int):
        words:list = [f"str{i}" for i in range(number)]
        
        for i in words:
            print(f"Строка - {i}")
            
    def rostics_load_immitation(self, number:int):
        for _ in range(number):
            load:int = randint(0, 100)
            
            if load > 85:
                print(f"Крылышки в опасности! Нагрузка — {load}%")
                
            time.sleep(0.2)
            
            

obj_loop = Loops()

obj_loop.loop_of_numbers(1, 8)
obj_loop.loop_of_strings(10)
obj_loop.rostics_load_immitation(10)

