def open_print_lines(file_original):

    # defining a function makes the code a little DRYer

    try:
        with open(file_original, "r") as file: # avoids the need for closing the file after opening it

            for line in file.readlines():

                print(line.rstrip("\n"))

    except FileNotFoundError as ermsg:
        print("File has not been found!")
        print(ermsg)

    finally:
        print("\n")
        print("All done!")
        print("\n")


def open_read_return(file_main):

    result = []

    try:
        with open(file_main, "r") as file:
            for line in file.readlines():
                newline = line.rstrip("\n")
                result.append(newline)

            return result


    except FileNotFoundError as ermsg:
        print("File not found!")
        print(ermsg)


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
