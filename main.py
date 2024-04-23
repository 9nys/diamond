class A:
    def introduce(self):
        return "I am class A."

class B(A):
    def introduce(self):
        return "I am class B."

class C(A):
    def introduce(self):
        return "I am class C."

class D(B, C):
    pass


instance_d = D()
print(instance_d.introduce())

instance_b = B()
print(instance_b.introduce())

instance_c = C()
print(instance_c.introduce())

instance_a = A()
print(instance_a.introduce())
