# encode() method for simple python encoder (Polina Antonenko)

def encode(password):
    encoded = ""

    for i in password:
        # convert to integer & shift by 3
        num = (int(i) + 3) % 10
        encoded += str(num)

    return encoded