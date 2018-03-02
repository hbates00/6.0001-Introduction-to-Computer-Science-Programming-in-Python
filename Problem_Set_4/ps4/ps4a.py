# Problem Set 4A
# Name: Haley Bates-Tarasewicz
# Collaborators: kmath
# Time Spent: 2:00
# Late Days Used: 2

def get_permutations(sequence):
    '''
    Ennumerate all permutations of a given string

    sequence (string): an arbitrary string to permute

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    permutations = []
    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations
        
    else:
        working_list = []
        for i in get_permutations(sequence[1:]):
            for space in xrange(len(i)+1):
                working_list.append(i[:space] + sequence[0] + i[space:])

        for i in working_list:
            permutations.append(i)
        
        return permutations
                
        

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print 'Input:', example_input
#    print 'Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#    print 'Actual Output:', get_permutations('abc')
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print 'TEST CASE 1'
    print '---------------'
    input1 = 'hi'
    print 'Input:', input1
    print 'Expected Output:', ['hi', 'ih']
    print 'Actual Output:', get_permutations(input1)
    print
   
    print 'TEST CASE 2'
    print '---------------'
    input2 = 'hey'
    print 'Input:', input2
    print 'Expected Output:', ['hey', 'ehy', 'eyh', 'hye', 'yhe', 'yeh',]
    print 'Actual Output', get_permutations(input2)
    print
    
    print 'TEST CASE 3'
    print '---------------'
    input3 = 'a'
    print 'Expected Output:', ['a']
    print 'Actual Output', get_permutations(input3)
    
    
    

