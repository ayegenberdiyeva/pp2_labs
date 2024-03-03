# Write a Python program to copy the contents of a file to another file

with open(
    "/Users/aminayegenberdiyeva/Desktop/test/start.txt"
) as start:
    with open(
        "/Users/aminayegenberdiyeva/Desktop/test/end.txt",
        "w",
    ) as end:
        end.writelines(start)