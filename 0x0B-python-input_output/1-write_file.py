def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as file:
        chars_written = file.write(text)
    return chars_written
