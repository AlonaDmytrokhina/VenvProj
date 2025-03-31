from app.io.input import read_from_console, read_from_file, read_from_csv
from app.io.output import write_to_console, write_to_file

def main():
    text_console = read_from_console()
    text_file = read_from_file("data/input.txt")
    text_csv = read_from_csv("data/input.csv")

    # To console
    write_to_console(text_console)
    write_to_console(text_file)
    write_to_console(text_csv)

    # To file
    write_to_file("data/output.txt", text_console)
    write_to_file("data/output.txt", text_file)
    write_to_file("data/output.txt", text_csv)

if __name__ == '__main__':
    main()