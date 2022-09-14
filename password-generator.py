# steps for execution
# paste this code into your ide
# execute the code and print the length for the password, the you will get random generated password.
import random

if __name__ == "__main__":
    dataList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '!', '@', '#', '$', '%', '&']

    size = int(input("Enter the length for password :- "))
    password = ""
    if size > 0:
        for _ in range(size):
            password += random.choice(dataList)

        print("***************************")
        print("Generated Password = ", password)
    else:
        print('Error : "Password length can not be Zero" ')
