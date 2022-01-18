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




main()
