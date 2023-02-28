"""
Author: Patrick Gawron
Date: 2023-03-01
Description: 
    python script to identify invalid windows system path
        which is causing the error 
        "The System Cannot Find The Path Specified" (EN)
        "Das System kann den angegebenen Pfad nicht finden." (DE)
Returns:
    path variable number + invalid path
"""

# Import necessary modules
import subprocess
import os

# get path variables
paths = os.environ["PATH"].split(';')

# True|False : if path is valid
def is_valid_path(path):
    """Checks if a Windows path is valid"""
    return os.path.exists(path)

# Main program
if __name__ == "__main__":

    all_paths_valid = True
    counter = 1;

    # loop through all paths
    for path in paths:
        if path.strip() == "":
            # Skip any empty path
            continue

        if not is_valid_path(path):
            # output the number of the path variable + invalid path
            print(f"Invalid path: {counter}: {path}")
            all_paths_valid = False
        
        counter+=1

    # output, that all are valid
    if all_paths_valid:
        "All paths are valid !"