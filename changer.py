import os

# Directory path
directory = 'image/C'

# Get list of files and sort them
files = os.listdir(directory)
files.sort()

# Start new index from 0
new_index = 0

# Rename files
for filename in files:
    if filename.endswith('.png'):
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f'{new_index}.png')
        os.rename(old_path, new_path)
        new_index += 1

print(f'Renamed {new_index} files in {directory}')
