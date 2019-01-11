import collections


index = collections.defaultdict(list)
for item in nums:
    key = item % 2
    index([key].append(item))
