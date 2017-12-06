class RootAdder:
    def __init__(self, num1, num2):
        try:
            print(self.f(num1) + self.f(num2))
        except ValueError:
            print("Must be positive numbers. You gave ",str(num1)," and ",str(num2))
        except TypeError:
            print("Must be numbers. You gave ",str(num1)," and ",str(num2))
            pass
    def f(self,x):
        if x < 0: raise ValueError
        else:
            try:
                return x**(1/2)
            except TypeError:
                raise TypeError
                pass
t = RootAdder(10,-3)

