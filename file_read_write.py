def file_read_write(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            data = f.read()

        # Modification: convert text to uppercase
        modified_data = data.upper()

        with open(output_file, "w") as f:
            f.write(modified_data)

        print(f" Successfully wrote modified content to '{output_file}'")

    except FileNotFoundError:
        print(f" Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f" An error occurred: {e}")


# Usage
file_read_write("input.txt", "output.txt")
