import pathlib
import os
import re

def main() -> None:
  base = r"C:\Users\mstar\Desktop\PythonProjects\harvard_cs50p"
  list_directory_recursive(base)

def list_directory_recursive(base: str) -> None:
  base_handle = list(os.walk(base))
  path_arrays = [
    [os.path.join(path, file_name) for file_name in file_names] 
    for path, directories, file_names in base_handle
    ]
  paths = [path for path_array in path_arrays for path in path_array]
  paths = list(set(paths))
  python_file_paths = filter(lambda path: pathlib.Path(path).suffix == ".py", paths)

  occured_in_files = []
  for python_file_path in python_file_paths:
    with open(python_file_path, "r", encoding="utf-8") as python_file:
      for line in python_file:
        if matches := re.search(r"hardvard", line):
          occured_in_files.append(python_file.name)
  print(*set(occured_in_files), sep="\n")


  # for path in paths:
  #   if matches := re.search(r"hardvard", path):
  #     print(matches)

  # path_arrays = [ for file_name_array in file_name_arrays]
  # print(*file_name_arrays, sep="\n")
  # file_names = []
  # for file_name_array in file_name_arrays:
  #   file_names.extend(file_name_array)
  # file_names = list(set(file_names))
  # # python_files = []
  

  # # search all directories for hardvard
  # subdirectories = [handle[0] for handle in base_handle]
  # for directory in subdirectories:
  #   if matches := re.search(r"hardvard", directory):
  #     print(matches)


if __name__ == '__main__':
  main()