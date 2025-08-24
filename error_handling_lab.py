def error_handling_lab():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n File content:\n")
            print(content)

    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f" Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Usage
error_handling_lab()
