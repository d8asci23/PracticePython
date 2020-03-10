PI = 3.141592
class Math:
    def circle_area(sefl, r):
        return PI * (r**2)

def sum(a, b):
    return a + b

if __name__=="__main__":
    print(PI)
    a = Math()
    print(a.circle_area(2))
    print(sum(PI, 5.5))

"""
>> python Python_Module_Practice.py
3.141592
12.566368
8.641592

>> print(Python_Module_Practice.PI)
3.141592

>> a = Python_Module_Practice.Math()
>> print(a.circle_area(2))
12.566368

>> print(Python_Module_Practice.sum(Python_Module_Practice.PI, 5.5))
8.641592
"""
