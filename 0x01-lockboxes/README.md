# Lockboxes

This project contains a Python function `canUnlockAll` that determines if all boxes can be opened starting from the first box.

## Function Description

The function `canUnlockAll(boxes)` takes a list of lists where each inner list represents a box containing keys to other boxes. Keys with the same number as a box can open that box. The function starts with the first box unlocked (`boxes[0]`) and attempts to open all other boxes using collected keys.

If all boxes can be opened, the function returns `True`; otherwise, it returns `False`.

## Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
