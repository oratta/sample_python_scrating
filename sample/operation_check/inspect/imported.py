import inspect

stack = inspect.stack()
print(stack)
for s in stack[1:]:
    m = inspect.getmodule(s[0])
    if m:
        print(m.__file__)
        break