# Error Handling
def divide(num1,num2):
    try:
        result= num1/num2
    except ZeroDivisionError:
        return "ERROR : DIVISION BY ZERO IS NOT ALLOWED"
    except TypeError:
        return "ERROR : BOTH INPUTS SHOULD BE A NUMBER"
    else:
        return result
    finally:
        print("EXECUTING FINALLY BLOCK")

# Example usage
print(divide(10, 2))  
print(divide(10, 0)) 
print(divide(10, 'a'))  
