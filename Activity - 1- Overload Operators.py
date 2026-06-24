# 1) Create a class named `A`.

# 2) Define the constructor `__init__(self, a)`:
#    a) Store the given value `a` in the instance variable `self.a`.

# 3) Overload the less-than operator `<` by defining `__lt__(self, other)`:
#    a) Compare `self.a` with `other.a`.
#    b) If `self.a < other.a`, return the message "ob1 is less than ob2".
#    c) Otherwise, return the message "ob2 is less than ob1".

# 4) Overload the equality operator `==` by defining `__eq__(self, other)`:
#    a) Compare `self.a` with `other.a`.
#    b) If both values are equal, return the message "Both are equal".
#    c) Otherwise, return the message "Not equal".

# 5) Create two objects:
#    a) `ob1 = A(2)`
#    b) `ob2 = A(3)`

# 6) Print the values stored inside `ob1.a` and `ob2.a`.

# 7) Use the `<` operator (`ob1 < ob2`):
#    a) This calls the overloaded method `__lt__()` and prints the returned message.

# 8) Create two more objects:
#    a) `ob3 = A(4)`
#    b) `ob4 = A(4)`

# 9) Print the values stored inside `ob3.a` and `ob4.a`.

# 10) Use the `==` operator (`ob3 == ob4`):
#     a) This calls the overloaded method `__eq__()` and prints the returned message.

class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "Ob1 is less than Ob2"
        else:
            return "Ob2 is less than Ob1"

    def __eq__(self, other):
            if (self.a == other.a):
                 return "Both are Equal"
            else:
                 return "Not Equal"

obj1 = A(7)
obj2 = A(6)
print(obj1.a, obj2.a)
print(obj1 < obj2)
obj1 = A(4)
obj2 = A(4)
print(obj1.a, obj2.a)
print(obj1 == obj2)