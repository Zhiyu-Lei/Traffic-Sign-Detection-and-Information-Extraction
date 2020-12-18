#!/usr/bin/env python3

# Modified from https://github.com/jakkcoder/training_yolo_custom_object_detection_files
# Creating files labelled_data.data and classes.names for training in Darknet framework

# Algorithm:
# Setting up full paths --> Reading file classes.txt -->
# --> Creating file classes.names -->
# --> Creating file labelled_data.data

# Result:
# Files classes.names and labelled_data.data needed to train in Darknet framework


full_path_to_images = 'data'

# Defining counter for classes
c = 0

# Creating file classes.names from existing one classes.txt
with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:
    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names
        # Increasing counter
        c += 1

# Creating file labelled_data.data
with open(full_path_to_images + '/' + 'labelled_data.data', 'w') as data:
    # Writing needed 5 lines
    # Number of classes
    data.write('classes = ' + str(c) + '\n')
    # Location of the train.txt file
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')
    # Location of the test.txt file
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')
    # Location of the classes.names file
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')
    # Location where to save weights
    data.write('backup = backup')
