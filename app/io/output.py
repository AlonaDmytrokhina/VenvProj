def write_to_console(text):
    """
        Prints text to the console.
        <0, isinstance? file? console?

        Note:
            This function takes a string and prints it to the console.

        Examples:
            >>> write_to_console("Hello, world!")
            Hello, world!

        Args:
            text (str): The text to print.

        Returns:
            None
        """
    print(text)


def write_to_file(filepath, text):
    """
        Writes text to a file using built-in Python capabilities.
        <0, isinstance? file? console?

        Note:
            This function appends a given text to a specified file.

        Examples:
            >>> write_to_file("data/output.txt", "Hello, world!")
            (Appends "Hello, world!" to output.txt)

        Args:
            filepath (str): The path to the file.
            text (str): The text to write.

        Returns:
            None
        """
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")