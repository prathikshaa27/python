from pathlib import Path
from pathlib import PurePosixPath

home_dir = Path.home()
print(home_dir)

to_get_cwd = Path.cwd()
print(to_get_cwd)

to_get_current_file = Path(__file__)
print(to_get_current_file)

first_folder = Path.cwd().parent
print(first_folder)

joined_path = Path.cwd()/'HTML'
print(joined_path)

new_file = Path.cwd()/"sample.txt"
print(new_file.is_file())

#file name with extension
file_extension = Path("sample.txt")
new_path = file_extension.with_suffix('.csv')
print(new_path)

posix_path = PurePosixPath('/home/Web Fundamentals/Python')
print("Posix Path:")
print("Parts:",posix_path.parts)
print("Drive:",posix_path.drive)
print("Parent:",posix_path.parent)
print("Name:",posix_path.name)
print("Suffix:",posix_path.suffix)
print("Absolute:",posix_path.is_absolute)

print()








