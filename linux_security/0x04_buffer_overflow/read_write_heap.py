#!/usr/bin/python3
"""
Module to find and replace strings in the heap of a process.
"""
import sys

def print_usage_and_exit():
    """Prints usage and exits with status 1."""
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def main():
    """Main function to perform heap search and replace."""
    if len(sys.argv) != 4:
        print_usage_and_exit()

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

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
            print("Error: Heap not found")
            sys.exit(1)

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
            mem_file.seek(heap_start)
            heap_data = mem_file.read(heap_end - heap_start)

            search_bytes = search_str.encode('ascii')
            replace_bytes = replace_str.encode('ascii')

            try:
                index = heap_data.index(search_bytes)
            except ValueError:
                print(f"Error: {search_str} not found in heap")
                sys.exit(1)

            print(f"[*] Found at {hex(heap_start + index)}")
            
            mem_file.seek(heap_start + index)
            mem_file.write(replace_bytes)
            

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
