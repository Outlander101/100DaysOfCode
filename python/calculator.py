import os

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    '+': "add",
    '-': "subtract",
    '*': "multiply",
    "/": "divide"
}

def operations_case(first_number, second_number, operation):
    match operation:
            case '+':
                return add(first_number, second_number)
            case '-':
                return sub(first_number, second_number)
            case '*':
                return mul(first_number, second_number)
            case '/':
                return div(first_number, second_number)
            case _:
                print("Invalid operation")
                return

def main():
    continues = True
    output = 0
    while continues:
        first_number = float(input("Enter the first number:  "))
        continue_prev = True
        while continue_prev:
            second_number = float(input("Enter the next number: "))
            # if not second_number.isnumeric():
            #     print(f"Invalid number: {second_number}")
            #     exit()
            operation = input(f"Choose the operation: {operations} '+,-,*,/': ")
            output = operations_case(first_number, second_number, operation)
            print(f"{first_number} {operation} {second_number} = {output}")
            output_continue = input(f"Do you want to continue with {output} (Y/N): ").lower()
            if output_continue == 'y':
                first_number = output
                continue
            else:
                continue_prev = False
                continuation = input("Want to continue with calculations (Y/N): ").lower()
                if continuation == 'y':
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue
                else:
                    continues = False
                    print("End of calculation")
                    continue

if __name__ == '__main__':
    main()


            
