def convert_to_uppercase(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        upper_content = content.upper()

        with open(destination_file, 'w') as dest:
            dest.write(upper_content)

        print("File successfully converted to uppercase and saved.")

    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

convert_to_uppercase(source, destination)