"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_title = ""
    old_title = filename.replace(" ", "_").replace(".TXT", ".txt")
    print(old_title)
    for index, char in enumerate(old_title):
        if char.isspace():
            char = "_"
        elif char.isalpha:
            try:
                previous_char = old_title[index - 1]
                next_char = old_title[index + 1]
                if next_char.isupper() or next_char == "(":
                    char += "_"
                elif previous_char == "(":
                    char = char.upper()
            except IndexError:
                pass

        new_title += char
    new_title += ".txt"
    return new_title



# def demo_walk():
#     """Process all subdirectories using os.walk()."""
#     os.chdir('Lyrics')
#     for directory_name, subdirectories, filenames in os.walk('.'):
#         print("Directory:", directory_name)
#         print("\tcontains subdirectories:", subdirectories)
#         print("\tand files:", filenames)
#         print("(Current working directory is: {})".format(os.getcwd()))
#
#         for filename in filenames:
#             path_name = os.path.join(directory_name, filename)
#             new_name = os.path.join(directory_name, get_fixed_filename(filename))
#             os.rename(path_name, new_name)
#             print(f"{path_name} is changed to {new_name}")



main()
# demo_walk()