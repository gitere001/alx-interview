#!/usr/bin/env python3
"""read_from_stdin.py module"""
import sys


def read_from_stdin():
    """
    Reads input from stdin and processes it to calculate file size and status
    code statistics.

    This function reads input from stdin line by line and processes each line
    to extract the file size and status code.
    It keeps track of the total number of lines and the total file size.
    It also maintains a dictionary to count the
    occurrences of each status code.

    If a line does not have enough parts or if the status code or file size
    cannot be converted to integers, the line  is skipped.

    After processing 10 lines, the function prints the total file size and the
    status code statistics. It then resets the counters and continues
    processing the remaining lines.

    If a KeyboardInterrupt is caught, the function prints the total file size
    and the status code statistics before exiting.
    Parameters:
    None

    Returns:
    None
    """
    total_lines = 0
    total_file_size = 0
    status_code_dict = {}
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break

            parts = line.split(" ")
            if len(parts) < 7:
                continue

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue

            if status_code in status_code_dict:
                status_code_dict[status_code] += 1
            else:
                status_code_dict[status_code] = 1

            total_lines += 1
            total_file_size += file_size

            if total_lines == 10:
                print(f"File size: {total_file_size}")
                for code, count in sorted(status_code_dict.items()):
                    print(f"{code}: {count}")
                total_lines = 0

    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code, count in sorted(status_code_dict.items()):
            print(f"{code}: {count}")
