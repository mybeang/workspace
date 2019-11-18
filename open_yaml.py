import yaml

file_path = "D:\\python_project\\workspace\\test_yaml.yaml"

with open(file_path, "r") as f:
    data = yaml.load(f)

print(data)