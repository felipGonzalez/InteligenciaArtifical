def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    


if __name__ == '__main__':
   num = int(input(" escribe el numero"))
   print(factorial(num))
    