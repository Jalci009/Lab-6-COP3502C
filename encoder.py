# Author: Jair Alcivar

def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        user_input = input("Please enter an option: ")

        if user_input == "1":
            encode()
        if user_input == "2":
            decode()
        if user_input == "3":
            return False


def encode():               # Takes in password and shifts/adds digit up by 3
    global og_pass
    global new_pass
    og_pass = input("Please enter your password to encode: ")
    constant = [3]
    og_pass = [int(item) for item in og_pass]
    new_pass = []
    for i in range(len(og_pass)):       # except for 7,8,9, it replaces them with appropriate number
        if og_pass[i] == 7:
            new_pass.append(0)
        elif og_pass[i] == 8:
            new_pass.append(1)
        elif og_pass[i] == 9:
            new_pass.append(2)
        else:
            new_pass.append(og_pass[i] + constant[0])
    print("Your password has been encoded and stored!\n")


def decode():              # Prints out encoded password and original password
    global new_pass
    global decode_pass
    decode_pass = ''
    new_pass_str = ''

    for i in new_pass:
      num = i - 3              #Shifts each digit down by 3 numbers. 
      if num < 0:
        num =  10 + num           #Digit cannot be negative, so digit continue to shift down from 9 after passing 0.
      decode_pass += str(num)

    for j in new_pass:          #converts an 'encoded password' list into a string. 
      new_pass_str += str(j)
    
    print(f'The encoded password is {new_pass_str}, and the original password is {decode_pass}.\n')

if __name__ == "__main__":
    main()
