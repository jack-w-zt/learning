def function_a():
    print("a before")
    function_b()
    print("a after")
def function_b():
    print("b befote")
    function_c()
    print("b after")
def function_c():
    print("c end")
print(function_a())