# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Циклический сдвиг

n = [6, 4, 7, 9, 8, 1, 3]
st = len(n) - 5


# for i in range(1, len(n)):
#     print(str(n[i]), '', end='')
#
# for i in range(st):
#     print(str(n[i]), '', end='')


for i in range(1, len(n)):
    print(str(n[i]), '', end='')

for i in n:
    print(str(n[i]), '', end='')