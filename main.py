READY_LIST = []

def flatten_list(nested_list):      # this func flattens the list
    for item in nested_list:
        if isinstance(item, list):  # this checks if the item in list is type of a list.
            flatten_list(item)
        else:
            READY_LIST.append(item)


def main():
    sample_list = [1, 2, [3, 4, ["five", 6, [7, "eight"], 9], "ten"], 11, 12, ["thirteen", 14], 15]   # sample test
    flatten_list(sample_list)
    print(READY_LIST) # debug purposes
    
    
    
    D
if __name__ == '__main__':
    main()
    
    