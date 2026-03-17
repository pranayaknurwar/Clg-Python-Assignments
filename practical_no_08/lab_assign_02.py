def remove_comments(line):
    line = line.strip()
    if line.startswith("#") or line == "":
        return None
    return line


def copy_without_comments(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()

        cleaned_lines = []

        for line in lines:
            cleaned = remove_comments(line)
            if cleaned:
                cleaned_lines.append(cleaned + '\n')

        with open(destination_file, 'w') as dest:
            dest.writelines(cleaned_lines)

        print("\n--- Source File Content ---")
        with open(source_file, 'r') as src:
            print(src.read())

        print("\n--- Destination File Content (No Comments) ---")
        with open(destination_file, 'r') as dest:
            print(dest.read())

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source = input("Enter source Python file: ")
destination = input("Enter destination file: ")

copy_without_comments(source, destination)