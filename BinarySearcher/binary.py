#this program does a binary search using python through a list of items
#the list should be ordered i.e it shold be sorted from smaller to bigger

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print(f"Step {steps}: {list[start:end + 1]}")

        steps += 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 9

binary_search(my_list,target)