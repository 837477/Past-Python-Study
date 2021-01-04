def binary_search(List, item):
    low = 0
    high = len(List) - 1

    #low와 high는 리스트 중에서 어디를 탐색하는지 나타낸다. (탐색범위, 구간)

    while low <= high: #low가 high보다 커지면 값을 찾지 못했으므로, 종료.
        mid = int( (low + high) / 2 ) #low와 high의 중간값을 정해준다.
        guess = List[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        # -1, +1을 해주는 이유는, 이미 탐색한 값이 중복되지 않기 위해.
    return None

TEST = [1, 3, 5, 7, 9]

print(binary_search(TEST, 3))
