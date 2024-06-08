import os
import ast

def get_imports_from_file(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)
    imports = {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
    imports.update({f"{node.module}.{alias.name}" if node.module else alias.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) for alias in node.names})
    return imports

def get_imports_from_directory(directory):
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_imports = get_imports_from_file(file_path)
                all_imports.update(file_imports)
    return all_imports

def write_requirements_file(imports, file_path='requirements.txt'):
    with open(file_path, 'w') as file:
        for imp in sorted(imports):
            file.write(f"{imp}\n")

# Directory containing your Python scripts
directory_path = 'path_to_your_python_project'

# Get all imports from the directory
imports = get_imports_from_directory(directory_path)

# Write the imports to requirements.txt
write_requirements_file(imports)

print(f"requirements.txt file has been created with {len(imports)} packages.")
import os
import ast

def get_imports_from_file(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)
    imports = {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
    imports.update({f"{node.module}.{alias.name}" if node.module else alias.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) for alias in node.names})
    return imports

def get_imports_from_directory(directory):
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_imports = get_imports_from_file(file_path)
                all_imports.update(file_imports)
    return all_imports

def write_requirements_file(imports, file_path='requirements.txt'):
    with open(file_path, 'w') as file:
        for imp in sorted(imports):
            file.write(f"{imp}\n")

# Directory containing your Python scripts
directory_path = '..\\viraltw'

# Get all imports from the directory
imports = get_imports_from_directory(directory_path)

# Write the imports to requirements.txt
write_requirements_file(imports)

print(f"requirements.txt file has been created with {len(imports)} packages.")
