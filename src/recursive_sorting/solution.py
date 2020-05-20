def print_all_unpacked(arr):
    for each in arr:
        if type(each) is list:
            print_all_unpacked(each)
        else:
            print(each)