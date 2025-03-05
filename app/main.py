# write your code here
def copy_file(command: str) -> None:

    try:
        file_list = command.split(" ")
        if "cp" == file_list[0] and file_list[1] != file_list[2]:
            original_f = file_list[1]
            copy_f = file_list[2]

            with open(original_f, "r") as original, open(copy_f, "w") as copy:
                copy.write(original.read())
    except Exception as e:
        print(f"error: {e}")
