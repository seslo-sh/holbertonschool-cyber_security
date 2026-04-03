#!/usr/bin/python3
"""
Module to find and replace strings in the heap of a process.
"""
import sys


def print_usage_and_exit():
    """Prints usage and exits with status 1."""
    sys.exit(1)


def main():
    """Main function to perform heap search and replace."""
    if len(sys.argv) != 4:
        print_usage_and_exit()

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    if not search_str:
        return

    try:
        with open(f"/proc/{pid}/maps", "r") as maps_file:
            heap_start = None
            heap_end = None

            for line in maps_file:
                if "[heap]" in line:
                    parts = line.split()
                    addr_range = parts[0].split("-")
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break

        if heap_start is None or heap_end is None:
            sys.exit(1)

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            search_bytes = search_str.encode('ascii')
            replace_bytes = replace_str.encode('ascii')

            try:
                index = heap_data.index(search_bytes)
            except ValueError:
                sys.exit(1)

            mem_file.seek(heap_start + index)
            mem_file.write(replace_bytes)

    except (IOError, PermissionError):
        sys.exit(1)


if __name__ == "__main__":
    main()
