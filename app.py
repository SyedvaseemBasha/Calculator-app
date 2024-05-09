from cal_func import do_addition,do_Subtraction
from area import cal_rec
from multi import do_Multi


def main():
    print('welcome to the calculator App')
    print("""
          \nSelect the function from the given options
          1. Add
          2. Subtract
          3. Multiplication
          4. Area
          """)
    user_input = input('Select the Function')

    a = int(input('value of A '))
    b = int(input('value of B '))
    
    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_Subtraction(a,b)
    elif user_input == '3':
        result = do_Multi(a,b)    
    elif user_input == '4':
        result = cal_rec(a,b)     

    print(result)    

if __name__ == "__main__" :
  main()  



    