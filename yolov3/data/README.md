# Data Directory

This directory stores all the training images and the corresponding labeling files (20 example images and labeling files are stored here).

File `classes.txt` stores the names of all the target classes. This file is generated automatically from `LabelImg`.

Scripts `creating-files-data-and-name.py` and `creating-train-and-test-files.py` (modified from https://github.com/jakkcoder/training_yolo_custom_object_detection_files) are used to generate all the necessary files for training the YOLO model: `classes.names`, `labelled_data.data`, `train.txt`, `test.txt`.
