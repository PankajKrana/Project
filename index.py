def factrial(n):
    print("factorial called with " + str(n))
    if n<2:
        print("returning 1")
        return 1

    result = n * factrial(n-1)
    print("returning" + str(result)+ "for factorial of " + str(n))
    return result


