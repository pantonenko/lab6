# main() method for simple python encoder (Polina Antonenko)

import encode

def main():
    password = 0
    encoded = 0
    decoded = 0

    running = True

    while running:
        # main menu
        print("Menu\n-------------")
        print("1.\tEncode\n2.\tDecode\n3.\tQuit\n")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            decoded = decode(password)
            print("The encoded password is " + encoded + ", and the original password is " + decoded + ".\n")

        else:
            running = False

if __name__ == "__main__":
    main()
