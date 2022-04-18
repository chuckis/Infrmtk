# coding: utf-8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y
        
(23 + 35)/(94 - 92)
a, b = 3, 4
(a +b)*(a - b)
a, b = b, a
(a+b)*(a-b)
pow(2, 5)
pow(2, 10)
import math
math.sqrt(1024)
pow(2, pow(3, 2))
help(pow)

pow("string", 2)
"string" * 10
p = Point(2, 3)
q = Point(1, 2)
    
def find_distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx**2 + dy**2)
    
find_distance(p, q)


