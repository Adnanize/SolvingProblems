#defining a function to ask the user to input a temperature in fahrenheit
askUser = float(input("What is the temperature you would like to choose (in Fahrenheit) to convert to celsius? "))

def convertTemp(askUser):
    """
    This function takes the input from the user and converts the temperature from fahrenheit to celsius
    """

    #This is the equation to convert Fahrenheit to celsius, and returns it
    return (askUser - 32) * (5/9) 

#Calling the function with the gives the temperature from Fahrenheit to celsius
print(convertTemp(askUser))