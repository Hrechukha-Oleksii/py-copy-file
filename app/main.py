import os.path


def copy_file(command: str) -> None:

    command_list = command.split(" ")
    if "cp" not in command_list:
        return
    if len(command_list) != 3:
        return
    input_file_name = command_list[1]
    output_file_name = command_list[2]
    if input_file_name == output_file_name:
        return
    if not os.path.exists(input_file_name):
        return

    with (open(input_file_name, "r") as file_input,
          open(output_file_name, "w") as file_output):
        for content in file_input.read():
            file_output.write(content)
