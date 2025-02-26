def finite_seqeunce():
    nums = [1,2,3]
    for num in nums:
        yield num

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1