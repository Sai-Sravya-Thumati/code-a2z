from collections import Counter
import heapq

def topKFrequent(nums, k):
    # Step 1: Count frequency of each element
    freq = Counter(nums)

    # Step 2: Use heap to get k most frequent elements
    return [item for item, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]

# Example usage:
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2
    print("Top", k, "frequent elements:", topKFrequent(nums, k))
