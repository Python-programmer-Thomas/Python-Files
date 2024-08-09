print("Welcome to use any base integers or strings interconversion tool! ")
def convert_base(number, from_base, to_base):
    if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
        raise ValueError("The base must be between 2 and 36! ")

    if isinstance(number, str):
        number = int(number, from_base)
    elif not isinstance(number, int):
        raise ValueError("The input number must be an integer or a string! ")

    if number == 0:
        return "0" if to_base == 10 else "0"

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    negative = number < 0
    number = abs(number)

    while number > 0:
        remainder = number % to_base
        result = alphabet[remainder] + result
        number = number // to_base

    if negative:
        result = "-" + result

    return result

def main():
    while True:
        try:
            input_number = input("Please enter the whole number to be converted: ")
            from_base = int(input("Please enter the original base (2-36): "))
            to_base = int(input("Please enter the target base (2-36): "))

            converted_number = convert_base(input_number, from_base, to_base)
            print(f"Result: {converted_number}")
            
            choice = input("Would you like to exit the program? (Y/N): ")
            if choice == "Y":
                break
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
