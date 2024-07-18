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
    cannot be converted to integers, the line is skipped.

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
    status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                         405: 0, 500: 0}
    try:
        for line in sys.stdin:
            parsed_line = line.strip().split()
            if len(parsed_line) < 2:
                continue
            code = int(parsed_line[-2]) if parsed_line[-2].isdigit() else None
            file_size = int(parsed_line[-1]) if parsed_line[-1].isdigit() else None
            if code is not None and file_size is not None:
                if code in status_code_count:
                    status_code_count[code] += 1
                total_file_size += file_size
                total_lines += 1
                if total_lines == 10:
                    total_lines = 0
                    print(f"Total size: {total_file_size}")
                    for code, value in sorted(status_code_count.items()):
                        print(f"{code}: {value}")
    except KeyboardInterrupt:
        print(f"Total size: {total_file_size}")
        for code, value in sorted(status_code_count.items()):
            print(f"{code}: {value}")
