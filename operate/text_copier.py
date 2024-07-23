def copy_text(source_file, destination_file):
    with open(source_file, 'r') as file:
        data = file.read()
    with open(destination_file, 'w') as file:
        file.write(data)
    print("Text copied successfully!")
