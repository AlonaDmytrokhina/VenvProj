import pandas as pd

def read_from_console():
    """
    Reads text input from the console.
    <0, isinstance? file? console?

    Note:
        This function prompts the user to enter a text string via the console.

    Examples:
        >>> read_from_console()
        Enter the text: Hello
        'Hello'

    Args:
        None

    Returns:
        str. The input text from the console.
    """
    return input("Enter the text: ")


def read_from_file(filepath):
    """
    Reads text from a file using built-in Python capabilities.
    <0, isinstance? file? console?

    Note:
        This function opens a text file in read mode and returns its contents.
        If the file is not found, it returns an error message.

    Examples:
        >>> read_from_file("data/input.txt")
        'Hello, world!'

    Args:
        filepath (str): The path to the text file.

    Returns:
        str. The file content or an error message if the file is missing.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filepath} is not found."


def read_from_csv(filepath):
    """
    Reads text from a CSV file using the pandas library.
    <0, isinstance? file? console?

    Note:
        This function loads a CSV file into a pandas DataFrame and returns its contents as a string.
        If the file is not found, it returns an error message.

    Examples:
        >>> read_from_csv("data/input.csv")
        'name, age\\nJohn, 25\\nAlice, 30'

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        str. The file content as a formatted string or an error message if the file is missing.
    """
    try:
        df = pd.read_csv(filepath)
        return df.to_string(index=False)  # Перетворюємо DataFrame у текстовий формат
    except FileNotFoundError:
        return f"File {filepath} is not found."
