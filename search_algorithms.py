# Description: This file contains the search algorithms used in the program.
def linear_search(words, target, result):
    for i, word in enumerate(words):
        if word == target:
            result.append(f"Linear Search: Found '{target}' at index {i}")
            return
    result.append(f"Linear Search: '{target}' not found")


def binary_search(words, target, result):
    low, high = 0, len(words) - 1

    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            result.append(f"Binary Search: Found '{target}' at index {mid}")
            return
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    result.append(f"Binary Search: '{target}' not found")


def jump_search(words, target, result):
    n = len(words)
    step = int(n**0.5)
    prev = 0

    while words[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            result.append(f"Jump Search: '{target}' not found")
            return

    for i in range(prev, min(step, n)):
        if words[i] == target:
            result.append(f"Jump Search: Found '{target}' at index {i}")
            return

    result.append(f"Jump Search: '{target}' not found")
