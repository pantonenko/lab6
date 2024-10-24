#decoder function (Matthew Prue)

def decode(encodedPass):
    decodedPass = ""
    
    for i in encodedPass:
        k = (int(i) - 3) % 10
        decodedPass += str(k)
        
    return decodedPass