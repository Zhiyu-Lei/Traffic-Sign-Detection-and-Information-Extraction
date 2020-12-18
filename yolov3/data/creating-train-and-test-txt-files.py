#!/usr/bin/env python3

# Modified from https://github.com/jakkcoder/training_yolo_custom_object_detection_files
# Creating files train.txt and test.txt for training in Darknet framework

# Algorithm:
# Setting up full paths --> List of paths -->
# --> Extracting 15% of paths to save into test.txt file -->
# --> Writing paths into train and test txt files

# Result:
# Files train.txt and test.txt with full paths to images


import os
import random

full_path_to_images = 'data'
os.chdir(full_path_to_images)

# Defining list to write paths in
p = []

# Using os.walk for going through all directories and files in them from the current directory
# Fullstop in os.walk('.') means the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpeg' or '.jpg' or '.png'
        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png'):
            # Preparing path to save into train.txt file
            path_to_save_into_txt_files = full_path_to_images + '/' + f
            # Appending the line into the list
            p.append(path_to_save_into_txt_files + '\n')

random.shuffle(p)

# Slicing first 15% of elements from the list to write into the test.txt file
p_test = p[:int(len(p) * 0.15)]

# Deleting from initial list first 15% of elements
p = p[int(len(p) * 0.15):]

# Creating file train.txt and writing 85% of lines in it
with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        train_txt.write(e)

# Creating file test.txt and writing 15% of lines in it
with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)
