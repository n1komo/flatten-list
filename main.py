
def flatten_list(test_list):
    if isinstance(test_list, list):
        if test_list == []:
            return []
        else:
            first, rest = test_list[0], test_list[1:]
            return flatten_list(first) + flatten_list(rest)
    else:
        return [test_list]


def main():
    sample_list = [1, 2, [3, 4, ["five", 6, [7, "eight"], 9], "ten"], 11, 12, ["thirteen", 14], 15]   # sample test
    flat_list = flatten_list(sample_list)
    print(flat_list) # debug purposes
    
    
    
if __name__ == '__main__':
    main()
    
    