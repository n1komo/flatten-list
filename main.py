READY_LIST = []

def flatten_list(nested_list):      # this func flattens the list
    for item in nested_list:
        if isinstance(item, list):  # this checks if the item in list is type of a list.
            flatten_list(item)
        else:
            READY_LIST.append(item)


def main():
    sample_list = [1, 2, [3, 4, [5, 6, [7, 8], 9], 10], 11, 12, [13, 14], 15]   # sample test
    flatten_list(sample_list)
    print(READY_LIST) # debug purposes
    
    
    
    
if __name__ == '__main__':
    main()
    
    