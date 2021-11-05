# assignment-03

# no other imports needed
from collections import defaultdict
import math
#

### PART 1: SEARCHING UNSORTED LISTS

# search an unordered list L for a key x using iterate
# return True or False
def isearch(L, x):
    def isKey(leftVal,index):
        if index == x and leftVal == 0:
            return leftVal + x
        elif leftVal != 0:
            return leftVal
        else:
            return 0
    return (iterate(isKey,0,L) == x)

def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])


def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])


# search an unordered list L for a key x using reduce
# return True or False
def rsearch(L, x):
    def isKey(leftVal, rest):
        if (leftVal == x) or (rest == x):
            return x
        else:
            return 0
    return (reduce(isKey,0,L) == x)

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(reduce(f, id_, a[:len(a)//3]),
                 reduce(f, id_, a[len(a)//3:]))


### PART 2: DOCUMENT INDEXING

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """    
    The main map reduce logic.
    
    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    # 1. call map_f on each element of docs and flatten the results
    # e.g., [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1), ('sam', 1), ('is', 1), ('ham', 1)]
    pairs = flatten(list(map(map_f, docs)))
    # 2. group all pairs by by their key
    # e.g., [('am', [1, 1]), ('ham', [1]), ('i', [1, 1]), ('is', [1]), ('sam', [1, 1])]
    groups = collect(pairs)
    # 3. reduce each group to the final answer
    # e.g., [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    return [reduce_f(g) for g in groups]


def doc_index_map(doc_tuple):
    """
    Params:
      doc_tuple....a tuple (docstring, docid)
    Returns:
      a list of tuples of form (word, docid), where token is a whitespace delimited element of this string.
    Note that the returned list can contain duplicates.
    E.g.
    >>> doc_index_map('document one is cool is it', 0)
    [('document', 0), ('one', 0), ('is', 0), ('cool', 0), ('is', 0), ('it', 1)]    
    """
    ### done. do not change me.
    doc, docid = doc_tuple[0], doc_tuple[1]
    return [(token, docid) for token in doc.split()]

def dedup(a, b):
    """
    Return a concatenation of two lists without any duplicates.
    Assume that input lists a and b already sorted and deduplicated.
    This should be done in _constant_ time (ignoring any time to create or concatenate lists).
    e.g.
    >>> dedup([1,2,3], [3,4,5])
    [1,2,3,4,5]
    """
    lists = flatten([a,b])
    without = list(lists)
    for x in lists:
        without.remove(x)
        if x in without:
            lists.remove(x)
    return lists
    
def doc_index_reduce(group):
    """
    Fix this function to instead call the reduce and dedup functions
    to return the _unique_ list of document ids that this word appears in.
    
    Params:
      group...a tuple of the form (word, list_of_docids), indicating the docids containing this word, with duplicates.
    Returns:
      tuple of form (word, list_of_docids), where duplicate docids have been removed.
      
    >>> doc_index_reduce(['is', [0,0,1,2]])
    ('is', [0,1,2])
    """
    return (group[0], dedup(group[1], []))
    
def test_dedup():
    assert dedup([1,2,3], [3,4,5]) == [1,2,3,4,5]
    
def test_doc_index_reduce():
    assert doc_index_reduce(['is', [0,0,1,2]]) == ('is', [0,1,2])

def test_index():
    res = run_map_reduce(doc_index_map, doc_index_reduce,
               [('document one is cool is it', 0),
                ('document two is also cool', 1),
                ('document three is kinda neat', 2)
               ])    
    assert res == [('also', [1]),
                   ('cool', [0, 1]),
                   ('document', [0, 1, 2]),
                   ('is', [0, 1, 2]),
                   ('it', [0]),
                   ('kinda', [2]),
                   ('neat', [2]),
                   ('one', [0]),
                   ('three', [2]),
                   ('two', [1])]
    

def collect(pairs):
    """
    Implements the collect function (see text Vol II Ch2)
    >>> collect([('i', 1), ('am', 1), ('sam', 1), ('i', 1)])
    [('am', [1]), ('i', [1, 1]), ('sam', [1])]    
    """
    ### done
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done. do not change me.
    return x + y
    
def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)


### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    return (iterate(parens_update,0,mylist) == 0)

def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    #current_output = open - close
    if next_input == "(":
        current_output += 1
    if next_input == ")":
        current_output -= 1
    return current_output


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    pairs = []
    reduced = []
    
    for res in list(map(paren_map, mylist)):
        pairs.append((res,1))
    groups = collect(pairs)

    def reduce_group(group):
        r = reduce(plus, 0, group[1])
        return [group[0], r]
    
    groups = ([reduce_group(g) for g in groups])
    
    for x in groups:
        reduced.append(x[0] * x[1])
    return (scan(plus,0,reduced)[1] == 0)

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    def evenout(r,l):
        while r >= 1 and l >= 1:
            r -= 1
            l -= 1
        return (r,l)
    if len(mylist) == 1:
        l,r = 0,0
        if mylist[0] == '(':
            l += 1
        elif mylist[0] == ')':
            r += 1
        return (l,r)
    else:
        lcounts, rcounts = (parens_match_dc_helper(mylist[:len(mylist)//2]), parens_match_dc_helper(mylist[len(mylist)//2:]))
        return (evenout(lcounts[0] + rcounts[0], lcounts[1] + rcounts[1]))
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False

test_dedup()
test_isearch()
test_rsearch()
test_doc_index_reduce()
test_index()
test_parens_match_iterative()
test_parens_match_scan()
test_parens_match_dc()
