from typing import TextIO


def reformat_git_log(input_stream: TextIO, output_stream: TextIO) -> None:
    """
    Reformats the git log output from the input stream and writes to the output stream.

    :param input_stream: The input stream containing git log lines.
    :param output_stream: The output stream to write the reformatted log lines.
    """
    for line in input_stream:
        # Split the input line into parts using tab as the delimiter
        parts = line.strip().split('\t')
        # Extract the relevant parts: SHA-1 and commit message
        sha1 = parts[0][:7]  # First 7 characters of the SHA-1
        message = parts[4]  # Commit message
        # Calculate the length of dots to fill the line to 80 characters
        dots_length = 80 - len(sha1) - len(message)
        dots = '.' * dots_length
        # Write the formatted line to the output stream
        output_stream.write(f"{sha1}{dots}{message}\n")
