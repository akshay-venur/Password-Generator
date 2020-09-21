import string 
import random

if __name__ == "__main__":

    Password_Length = int(input("Enter password length"))

    '''
    random.choices(sequence, weights=None, cum_weights=None, k=1)
    sequence : Required. A sequence like a list, a tuple, a range of numbers etc.
    weights  : Optional.  A list were you can weigh the possibility for each value. Default None
    k 	     : Optional. An integer defining the length of the returned list
    '''

    '''
    string.ascii_letters : Return ASCII letters (both lower and upper case)
    string.digits        : Return Digits from 0-9
    string.punctuation   : Return punctuation symbols
    '''
    
    Password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=Password_Length))
    print(Password)
