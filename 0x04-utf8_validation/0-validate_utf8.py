#!/usr/bin/python3
"""a function that determines if a given data set represents a valid
UTF-8 encoding."""


def validUTF8(data):
    """
    Check if data is a valid UTF-8 encoding.
    Returns True if valid, False otherwise.
    """
    count = 0
    mask1 = 0b10000000  # 128 in decimal
    mask2 = 0b01000000  # 64 in decimal

    for i in data:
        mask_byte = 0b10000000  # Start with the most significant bit

        if count == 0:

            while mask_byte & i:
                count += 1
                mask_byte = mask_byte >> 1

            # Check for valid UTF-8 lengths
            if count == 0:
                continue  # Single-byte character (valid)
            if count == 1 or count > 4:
                return False  # Invalid UTF-8 byte length
        else:
            # Check if continuation byte starts with 10
            if not (i & mask1 and not (i & mask2)):
                return False  # Invalid continuation byte

        count -= 1  # Expect one less continuation byte

    return count == 0  # Ensure no unmatched continuation bytes remain
