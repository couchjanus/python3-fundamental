# app.py
# Модули импортируются из других модулей с помощью команды import. 
# import the fibo module
import fibo
import foo

def main():
    
    foo.fib(100)

    result = fibo.fibonacci(1000)
    print(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
