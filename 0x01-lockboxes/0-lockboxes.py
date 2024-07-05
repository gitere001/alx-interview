#!/usr/bin/python3
"""Defines a function that determines if all boxes can be opened."""


def canUnlockAll(boxes):
    """
    Given a list of boxes, each containing a list of keys that can open it,
    this function determines if all boxes can be opened.

    Parameters:
    - boxes (list): A list of lists, where each inner list represents a box and
      contains the keys that can open it.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.

    Algorithm:
    1. Initialize an empty list `open_boxes` to keep track of the boxes that
       have been opened. Add the first box (index 0) to `open_boxes`.
    2. Initialize a set `keys` with the keys from the first box.
    3. While there are keys left to process:
        a. Initialize an empty set `new_keys` to keep track of the new keys
           that can be opened in the next iteration.
        b. For each key in `keys`:
            i. If the key is within the range of the number of boxes and the
                key is not already in `open_boxes`, add the key to `open_boxes`
                and update `new_keys` with the keys that can be opened by the
                current key.
        c. Replace `keys` with `new_keys`.
    4. Return True if the number of boxes opened is equal to the total number
       of boxes, False otherwise.
    """
    open_boxes = [0]
    keys = set(boxes[0])
    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and key not in open_boxes:
                open_boxes.append(key)
                new_keys.update(boxes[key])
        keys = new_keys
    return len(open_boxes) == len(boxes)
