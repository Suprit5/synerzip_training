# def div(a,b):
#     print(a/b)
# def ext_div(func):
#     def inside_logic(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inside_logic

# divs=ext_div(div)
# divs(2,4)

# '''passing a function as an argument'''
# def cube(x):
#     return x*x*x
# def ans(func,arg_list):
#     result=[]
#     for i in arg_list:
#         result.append(func(i)) #here we are calling cube which has an alias func
#     return result

# #here we are calling a func ans while passing two args 
# #1. cube (which finds cube of an number)
# #2. [] (and a list of numbers of which cube to be found)
# cube=ans(cube,[1,5,7,8,9])
# print(cube)

# def html_tag(tag):
#     def message(msg):
#         print(f'<{tag}>{msg}</{tag}>')
#     return message
# print_tag=html_tag('h1')
# print(print_tag) #this variable print_tag is equal to the message function which is inside the tag function
# print_tag('Hello World!')
# print_tag('Namaste World')

'''closures'''
def outer_func(message):
    msg=message
    def inner_func():
        print(msg)
    return inner_func
my_func=outer_func('Hello')
print(my_func())