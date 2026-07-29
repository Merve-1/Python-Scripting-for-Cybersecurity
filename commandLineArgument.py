import sys

def add_to_hosts_from_args():
    """
    Takes an IP (arg 1) and Hostname (arg 2) from the command line
    and appends them to /etc/hosts.
    """
    # 1. Check if we have enough arguments
    # sys.argv[0] is the script name itself
    # sys.argv[1] is the first argument (IP)
    # sys.argv[2] is the second argument (Hostname)
    if len(sys.argv) < 3:
        print(f"Error: Not enough arguments.", file=sys.stderr)
        print(f"Usage: sudo python3 {sys.argv[0]} <IP_ADDRESS> <HOSTNAME>", file=sys.stderr)
        sys.exit(1)  # Exit with an error code

    try:
        # 1. Get inputs from arguments
        ip = sys.argv[1]
        hostname = sys.argv[2]

        # 2. Format the new line
        new_entry = f"{ip}\t{hostname}\n"

        # 3. Open /etc/hosts in 'a' (append) mode
        with open("/etc/hosts", "a") as hosts_file:
            hosts_file.write(new_entry)

        print(f"\nSuccessfully added:")
        print(f"{new_entry}")

    except PermissionError:
        print("\nError: Could not write to /etc/hosts.", file=sys.stderr)
        print("Please run this script with sudo.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    add_to_hosts_from_args()