# We can work with Directories using pathlib module in python
from pathlib import Path

# Check if path exists
path = Path('3. Python Files, API/Photos')
print(path.exists()) # Returns boolean value

# Create directory if not exist and delete an existing directory
path = Path('new_folder')
print(path.mkdir()) # Create a folder
print(path.rmdir()) # Delete a folder

# List files from current directory (Just like 'ls' in Unix)
path = Path()
for file in path.glob('*.py'):
    print(file)
