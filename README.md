# Overview

This script is designed to organize files within a specified directory by moving files into subfolders based on their file extensions. Specifically, it moves .pdf and .png files into respective folders labeled "pdf files" and "png files".

# Requirements

The script uses two modules:

`os:` For interacting with the operating system, such as listing files and checking if directories exist.

`shutil:` For moving files from one directory to another.

# How it works

**1. Define the Path:** The script requires you to specify the `path` of the directory where the files to be organized are located.
   
**2. List Files:** The script will list all files present in the specified directory.
 
**3. Create Folders:** It checks if folders named `pdf files` and `png files` already exist in the directory. If they don't exist, the script will create these folders.
   
**4. Move Files:**
  If a file with the `.png` extension is found, it is moved to the `png files` folder.
  If a file with the `.pdf` extension is found, it is moved to the `pdf files` folder.
  The script ensures that no duplicate files are moved by checking whether the file already exists in the destination folder.

# Instructions

1. Both `os` and `shutil` are built-in Python modules, so no additional installation is needed.
   
2. Replace `r"Enter path here"` with the path to the folder you want to organize. Make sure to use raw string formatting (precede the path string with `r` to avoid issues with escape characters).

# Examples

Assuming the folder `C:/Users/Example/Documents/`contains files like:  

`image1.png`

`file1.pdf`

`image2.png`

The script will:

1. Create a folder `pdf files` and move all `.pdf` files there.

2. Create a folder `png files` and move all `.png` files there.

