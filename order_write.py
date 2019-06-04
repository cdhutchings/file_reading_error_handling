# In this file we will be able to write files

# Same logic as before: takes file to write but also takes items to write into files

# open the file using the write option "w"
# write our item into file

# as always, handling all errors as we go


def write_to_file(filename, list):

    try:
        # syntax of with: with <file> as <placeholder>

        with open(filename, "a") as file:
            for item in list:
                file.write(item + "\n") # if the append option has been included in the open function, then write will
                                    # append

    except FileNotFoundError as ermsg:
        print("File not found!")
        print(ermsg)

    finally:
        print("All done!")


write_to_file("order.txt", ["potato salad", "curry", "cheesecake"])
