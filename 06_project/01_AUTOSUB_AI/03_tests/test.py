import os
current_path = os.path.abspath(os.path.dirname(__file__))
print(current_path)

print(os.path.exists(current_path))
print(os.path.isdir(current_path))
print("github.com")