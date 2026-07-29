#!/usr/bin/env python3

def add_to_hosts():
    """
    Asks the user for an IP and Hostname and appends them to /etc/hosts.
    """
    try:
        # 1. Get user input
        ip = input("Enter IP: ")
        hostname = input("Enter Hostname: ")

        # 2. Format the new line
        #    \t is a Tab character, \n is a new line
        new_entry = f"{ip}\t{hostname}\n"

        # 3. Open /etc/hosts in 'a' (append) mode
        with open("/etc/hosts", "a") as hosts_file:
            hosts_file.write(new_entry)

        print(f"\nSuccessfully added:")
        print(f"{new_entry}")

    except PermissionError:
        print("\nError: Could not write to /etc/hosts.")
        print("Please run this script with sudo.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    add_to_hosts()