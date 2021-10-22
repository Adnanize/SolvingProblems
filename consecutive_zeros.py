def consecutive_zeros(binary_string): 
    """
    This function takes a binary string as a parameter, and returns
    the biggest number of consecutive zeros
    """
    #returns the biggest number of consecutive zeros
    return  "The biggest number of consecutive zeros is ", max(map(len,binary_string.split('1')))

#calling the function with the binary string
print(consecutive_zeros('1001101000110'))
