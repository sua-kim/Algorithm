'''
2020-2 자료구조 과제 3: 정렬 프로그램

1870021 휴먼기계바이오공학부 김수아
'''

import pandas as pd
import time
import random

# 선택정렬
def selection_sort(arr):
    for i in range(len(arr)):
        lowestNumberIndex = i
        # 가장 작은 원소의 인덱스 찾기
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowestNumberIndex]:
                lowestNumberIndex = j
        # 가장 작은 원소와 정렬안된 부분의 가장 작은 위치의 원소를 교환
        if lowestNumberIndex != i:
            temp = arr[i]
            arr[i] = arr[lowestNumberIndex]
            arr[lowestNumberIndex] = temp
    return arr

# 버블정렬
def bubble_sort(arr):
    # 어떤 인덱스까지 아직 정렬이 되지 않았는지 기록
    unsorted_until_index = len(arr) - 1

    # 배열의 정렬 여부를 기록
    sorted = False

    # 배열이 완전히 정렬됐음을 알 때까지 while 루프 실행
    while not sorted:
        sorted = True
        # for 루프는 배열의 첫 인덱스부터 아직 정렬되지 않은 인덱스까지 수행
        for i in range(unsorted_until_index):
          # 모든 인접값 쌍을 비교하고 순서가 뒤바뀌어있으면 교환
          if arr[i] > arr[i+1]:
            sorted = False
            arr[i], arr[i+1] = arr[i+1], arr[i]

        # unsorted_until_index 값을 1 감소
        unsorted_until_index = unsorted_until_index - 1
    return arr

# 삽입정렬
def insertion_sort(arr):
    for index in range(1, len(arr)):
        # index: 각 패스스루의 시작 위치
        # position: temp_value를 저장할 위치, 비교를 통해 삽입할 위치까지 이동
        position = index
        # temp_vlaue: 각 패스스루에서 위치를 찾아가는 원소의 값을 임시로 저장
        temp_value = arr[index]
        # 배열의 끝을 만나면 정지 or position - 1 위치의 값이 temp_value보다 작으면 정지
        while position > 0 and arr[position-1] > temp_value:
            # temp_value보다 큰 값을 뒤로 이동
            arr[position] = arr[position-1]
            position = position - 1
            # 정렬되는 정확한 위치에 temp_value값 저장
            arr[position] = temp_value
    return arr
            
# 쉘 정렬
def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                # 삽입 정렬을 위해 한칸 씩 미뤄줌
                arr[j + h] = arr[j]
                j -= h
            # 조건문을 빠져나온 j는 이미 j-h연산이 끝났으므로 다시 +h
            arr[j + h] = temp
        h //= 2
    return arr

# 히프정렬
def heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

# 퀵정렬
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    return sort(0, len(arr) - 1)

# 합병정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # mid: 리스트의 중간 지점
    mid = len(arr) // 2
    # mid를 중심으로 왼쪽 리스트, 오른쪽 리스트로 분리
    leftArr = arr[:mid]
    rightArr = arr[mid:]
    leftArr = merge_sort(leftArr)
    rightArr = merge_sort(rightArr)
    # 재귀 반복
    return merge(leftArr, rightArr)

def merge(left, right): # 분리된 리스트를 합치는 함수
    result = []
    # left와 right의 첫 번째 요소를 비교해 작은 값을 result에 저장
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

# 래딕스 정렬
def radix_sort(arr, base=10):
    size = len(arr)
    maxval = max(arr)
    exp = 1
    while exp <= maxval:
        output = [0]*size
        count = [0]*base
        for i in range(size): 
            count[(arr[i]//exp)%base] += 1
        for i in range(1,base): 
            count[i]+=count[i-1]
        for i in range(size-1,-1,-1):
            j = (arr[i]//exp)%base
            output[count[j]-1] = arr[i]
            count[j] -= 1
        for i in range(size): arr[i]=output[i]
        exp *= base
    return arr

# 메인 함수
if __name__=="__main__":
    
    # array: 20만개 수치데이터를 저장한 배열
    array = []
    
    # 20만 개 난수 데이터 생성
    num = random.randrange(0,250000)

    for i in range(200000):
        while num in array:
            num = random.randrange(0,250000)
        array.append(num)
    
    # 정렬된 결과(오름차순)
    array = sorted(array)
    
    # 선택정렬 수행 시간 출력
    start = time.time()  # 시작 시간 저장
    selection_sort(array)
    print("(1) 선택정렬:", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    
    # 버블정렬 수행 시간 출력
    start = time.time() 
    bubble_sort(array)
    print("(2) 버블정렬:", time.time() - start) 
    
    # 삽입정렬 수행 시간 출력
    start = time.time() 
    insertion_sort(array)
    print("(3) 삽입정렬:", time.time() - start) 
    
    # 쉘정렬 수행 시간 출력
    start = time.time() 
    shell_sort(array)
    print("(4) 쉘정렬:", time.time() - start) 
    
    # 히프정렬 수행 시간 출력
    start = time.time() 
    heap_sort(array)
    print("(5) 히프정렬:", time.time() - start) 
    
    # 퀵정렬 수행 시간 출력
    start = time.time()
    quick_sort(array)
    print("(6) 퀵정렬:", time.time() - start) 
    
    # 합병 정렬 수행 시간 출력
    start = time.time() 
    merge_sort(array)
    print("(7) 합병정렬:", time.time() - start) 
    
    # 래딕스정렬 수행 시간 출력
    start = time.time() 
    radix_sort(array)
    print("(8) 래딕스정렬:", time.time() - start) 
