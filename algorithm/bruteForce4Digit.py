
codeToCrack = '2508'

def bruteForce(code):
    code = [int(x) for x in code]
    bruteForceAttempt = [0, 0, 0, 0]
    # while bruteForceAttempt != code:
    for i in range(len(code)):
        for j in range(10):
            bruteForceAttempt[i] += j
            print(bruteForceAttempt)
            bruteForceAttempt = [0, 0, 0, 0]
    
    return bruteForceAttempt

# bruteForce(codeToCrack)

def tryCode(code):
    myCode = ""
    attempt = 0
    def fillCode(code, digit):
        myCode = ""
        for i in range(digit-len(str(code))):
            myCode += "0"
        myCode += str(code)
        return myCode
        
    for i in range(10**len(code)):
        myCode = fillCode(i, len(code))
        print(myCode)
        if myCode == code:
            break
        attempt += 1
    return attempt

print(tryCode('009011'))