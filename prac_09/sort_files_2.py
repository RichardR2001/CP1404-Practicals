"""
CP1404/CP5632 Practical
Sort files based on extension and user categorisation
"""
import os


def main():
    """Move files into where user wants to store them based on the file extension."""
    ext_type_to_cat = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        ext = get_extension(filename)
        if ext not in ext_type_to_cat:
            category = input("What category would you like to sort {} files into? ".format(ext))
            ext_type_to_cat[ext] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(ext_type_to_cat[ext], filename))


def get_extension(filename):
    ext = filename.split('.')[-1]
    return ext


main()
