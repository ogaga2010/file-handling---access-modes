def read_file(file_path):
    with open(file_path, 'r') as file:

        content = file.read()
        print("Reading from file:")
        print(content)

def write_file(file_path, text):
    with open(file_path, 'w') as file:

        file.write(text)
        print(f"Written to file: {text}")

def append_file(file_path, text):
    with open(file_path, 'a') as file:

        file.write(text)
        print(f"Appended to file: {text}")

def read_write_file(file_path, text):
    with open(file_path, 'r') as file:

        content = file.read()
        print("Reading from file:")
        print(content)
        file.write(text)
        print(f"Written to file: {text}")

# Codingal usage
file_path = 'Codingal.txt'

# Write to file
write_file(file_path, "Hello, World! \n")

# Read from file
read_file(file_path)

# Append to file
append_file(file_path, "This line is written in read-write mode. \n")

# Read from file again to see all changes
read_file(file_path)