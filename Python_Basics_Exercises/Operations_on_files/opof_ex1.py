import os

def numerate_files(filepath):
    for index, file in enumerate(os.listdir(filepath)):
        name_and_extension = file.split('.')
        file_name = name_and_extension[0]
        if len(name_and_extension) == 2:
            extension = name_and_extension[1]
        else:
            extension = ""
        os.rename(
            os.path.join(filepath, file),
            os.path.join(filepath, f'{file_name}_{index}.{extension}')
        )
numerate_files("/home/lenovo")

# TODO: Dawid ask about filepaths