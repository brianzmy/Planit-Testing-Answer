#Challenge 1
def fib(n):

    """
    xn = xn−1 + xn−2 according to this formula we could use recursion to solve
    the problen but it will cost too much time complexity thus i choose use spatial
    optimization to solve the problem.
    1,1,2,3,5,8,13,21,34
    
    Test Cases
    >>> n = 1
    >>> fib(n)
    1
    >>> n = 2
    >>> fib(n)
    1
    >>> n = 4
    >>> fib(n)
    3
    >>> n = 8
    >>> fib(n)
    21

    """

    Result = None
    if n == 0:
        Result = 0
    elif n ==1 :
        Result = 1
        
    a = 0
    b = 1
    for i in range (2,n+1):
        c = a + b           # take 8 as an example c = 1,2,3,5,8,13,21
        a = b               #take 8 as an example a = 1,2,3,5,8,13
        b = c               # take 8 as an example b = 2,3,5,8,13,21
        
    Result = b
    return Result

import math
def nearest_fib (m):
    
    """
    (5*m2 + 4) or (5*m2 – 4) according to this formula a number is fib
    if it is a perfect square. In this case we could split in to 3 conditions
    1: a number is a fib 2: a number is not a fib but it close to a fib num that
    smaller than itself 3: a number is not a fib but it close to a fib num that
    larger than itself

    Test Cases
    >>> m = 1
    >>> nearest_fib(m)
    'Yes, the index is 1 or 2'
    >>> m = 2
    >>> nearest_fib(m)
    'Yes, the index is 3'
    >>> m = 4
    >>> nearest_fib(m)
    'No, the NEAREST index is 4 and 5'
    >>> m = 22
    >>> nearest_fib(m)
    'No, the NEAREST index is 8'
    >>> m = 30
    >>> nearest_fib(m)
    'No, the NEAREST index is 9'
    """
    if m < 0:
        return 'Please try another number'
    if m == 0:
        return '0 is the seed value of Fibonacci'
    if m ==1:
        return 'Yes, the index is 1 or 2'
    ind = 1
    a = 0
    b = 1
    while b < m: 
        c = a+b
        ind +=1
        a = b
        b = c
    # if it is a perfect square the int function would not change the result.
    if (int (math.sqrt(5*m*m+4))* int (math.sqrt(5*m*m+4))== 5*m*m+4 or
        int (math.sqrt(5*m*m-4))*int (math.sqrt(5*m*m-4)) == 5*m*m-4):
        return 'Yes, the index is '+ str(ind)
    
    #a is previous fib number which is smaller than m, and b is next fib number
    #which is larger than m
    
    elif m - a < b-m:
        return 'No, the NEAREST index is ' + str(ind-1)
    elif m - a == b-m:
        return 'No, the NEAREST index is ' + str(ind - 1) + ' and ' + str(ind)
    else:
        return 'No, the NEAREST index is ' + str(ind)
    

#Challenge 2
def HOL (x):
    """
    the requiremens says this problem ignoring the case, so i lower the string
    before i do the computing. For this question we can use a nested for to calcualte the occurences of
    every letter, then append it in a list. then we find the max number in the
    occurences list, and get the index of it. Because the index is the same as
    the input so we can just use the first index number in the list to get the
    expected result

    Test Cases
    >>> x = 'Character'
    >>> HOL(x)
    'c'
    >>> x = 'banana'
    >>> HOL(x)
    'a'
    >>> x = 'APplE'
    >>> HOL(x)
    'p'
    """
    x = x.lower()
    Olist = [] #This list is used to store the occurrence number value
    for a in x:
        occurrences = 1
        for i in range(len(x)):
            if a == x[i]:
                occurrences +=1
        Olist.append(occurrences)
    HO = max(Olist)
    
    Llist = []#This list is used to store the index of the occurence number
    for j in range (len(Olist)):
        if HO == Olist[j]:
            Llist.append(j)
            
    High_OCC_Letter = x[Llist[0]]#Because we need the character that apper first,
                                 #so we just need get the first index number
    
    return  High_OCC_Letter

#Challenge 7

def list_from_file(filename):
    """
    Reads a text file into a list of strings.
    """
    file = open(filename)
    res = []
    for line in file:
        res = res + [line.strip()]
    file.close()
    return res


def table_from_file(filename):
    """
    Reads a table from a csv file.
    """
    lines = list_from_file(filename)
    cols = lines[0].split(',')
    tab = []
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        tab = tab + [row]
    return tab, cols


def lookup(heading,value):
    """
    The requirements says we need to print the row value  depends on the column(heading) value, this i write two function to
    read the table value and the column(heading)value. Then i check whether the input is in the column(heading) array,
    if yes, get the index of the heading to match the value in the table array, then print all the rows that contains that
    value. 
    Test Cases
    >>> lookup('Name','Alex')
    [['1', 'Alex', '15/03/2020', 'Australia'], ['10', 'Alex', '15/03/2020', 'Australia'], ['11', 'Alex', '15/03/2020', 'Australia']]
    >>> lookup('ID','3')
    [['3', 'Cathy', '26/04/2002', 'Fiji']]
    >>> lookup('DOB','21/06/2000')
    [['4', 'David', '21/06/2000', 'Thailand'], ['7', 'Galio', '21/06/2000', 'Greek']]
    >>> lookup('ID','23')
    'Value Not Found'
    >>> lookup('Address','1 Bourke Street')
    'Please enter a valid HEADING'

    """
    tab,cols = table_from_file('Dummy Data.csv')
    res = []
    if heading in cols:
        idx = cols.index(heading)
        for j in range(len(tab)):
            if value == tab[j][idx]:
                res.append(tab[j])
        if len(res) == 0:
            return 'Value Not Found'
        else:
            return res
    else:
        return 'Please enter a valid HEADING'
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
