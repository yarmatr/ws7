import os
import shutil
input_dir = os.environ['BATCH_INPUT_DIR']
output_dir = os.environ['BATCH_OUTPUT_DIR']
file_list = os.listdir(input_dir)
for file_name in file_list:
    file_path = os.path.join(input_dir, file_name)
    if os.path.isdir(file_path):
        shutil.copytree(file_path, output_dir)
    else:
        shutil.copy(file_path, output_dir)