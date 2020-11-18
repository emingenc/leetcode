"""
Largest Item Association
https://leetcode.com/discuss/interview-question/782606/Amazon-or-OA-2020-or-Largest-Item-Association


"""

from collections import deque, defaultdict


def largest_item_association(item_association):
    item_map = set()
    for items in item_association:
        item_map[items[0]].add(items[1])
        item_map[items[1]].add(items[0])
    largest_group = []
    visited = set()
    for item in item_map:
        if item in visited:
            continue
        group = []
        queue = deque()
        queue.add(item)
        while queue:
            cur_item = queue.popleft()
            visited.add(cur_item)
            group.append(cur_item)
            for neighbor in item_map[cur_item]:
                if neighbor not in visited:
                    queue.append(neighbor)
        if len(group) > len(largest_group):
            largest_group = group.copy()
    largest_group.sort()
    return largest_group
