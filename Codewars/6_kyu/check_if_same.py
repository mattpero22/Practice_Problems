'''
Problem: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

Instructions:
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

'''

def comp(array1, array2):
    if array1 is not None and array2 is not None:
        if len(array1) == 0 or len(array2) == 0 or len(array1) != len(array2):
            return False
        else:
            array1.sort()
            array2.sort()
        for idx,ele in enumerate(array1):
            if array1[idx] == array2[idx]**(1/2):
                continue
            else:
                return False
            
        return True
    return False



if __name__ == '__main__':
    a = [121, 144, 19, 161, 19, 144, 19, 11]  
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(a,b))

'''
Notes:
    # had to work with the .sort() array method. Forgot that it does actually modify the variable, and not return a sorted instance of the array.
    # had to add an extra error wrapper condition for the None type on one of our required parameters to get it to pass all tests

Result:
    COMPLETED: 7 minutes
'''