# def decorator_func(func):
#     def inner_logic(*args,**kwargs):
#         print(f'inner logic consists of {func.__name__}')
#         return func(*args,**kwargs)
#     return inner_logic
# @decorator_func
# def display():
#     print('display')
# display()

def new_add(func):
    def inner_logic(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return inner_logic

@new_add
def div(a,b):
    print(a/b)

div(2,4)