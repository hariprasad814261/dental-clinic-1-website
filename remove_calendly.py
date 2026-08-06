import os

path = r"d:\Anti gravity Folder\Workspace\dental website-1\lumora-dental"

for root, dirs, files in os.walk(path):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = content.replace("https://calendly.com/shreyasrajsony11", "#")
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {filepath}")
