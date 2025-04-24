def modify_file_content(content):
    return content.upper()

def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
        return

    modified_content = modify_file_content(content)

    output_filename = f"modified_{input_filename}"
    try:
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified file has been saved as '{output_filename}'")
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
