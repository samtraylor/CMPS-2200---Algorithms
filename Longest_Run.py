class Result:
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size             # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def longest_run_recursive(mylist, key):
    if mylist[0] == key:
        return Result(1,1,1,True)
    elif (key in mylist) == False and len(mylist) == 1:
        return Result(0,0,0,False)
    else:
        left = longest_run_recursive(mylist[:len(mylist)//2],key)
        #print(left.__repr__())
        right = longest_run_recursive(mylist[len(mylist)//2:],key)
        #print(right.__repr__())
        if mylist[len(mylist)//2 - 1] == mylist[len(mylist)//2]:
            longest = left.longest_size + right.longest_size
        else:
            longest = max(left.longest_size,right.longest_size)
        return Result(left,right,longest,False)
        
def test_longest_run():
    print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12).__repr__())
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3

test_longest_run()
