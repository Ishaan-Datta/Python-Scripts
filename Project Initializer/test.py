import os

file_dir = os.path.dirname(os.path.realpath(__file__))
print(file_dir)

path_list = file_dir.split("\\")
print(path_list)

print(path_list[7])
path_list[7] = "New"
print(path_list[7])
print(path_list[0:8])
del path_list[-1]

final_path = "\\".join(path_list[0:8])
print(final_path)
