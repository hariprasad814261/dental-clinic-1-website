import os

path = r"d:\Anti gravity Folder\Workspace\dental website-1\lumora-dental"

for root, dirs, files in os.walk(path):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.svg'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = content
            new_content = new_content.replace("Lumora Dental", "Dr. Dinakar’s Dental Care")
            new_content = new_content.replace("Lumora", "Dr. Dinakar’s Dental Care")
            new_content = new_content.replace("hello@lumoradental.com", "test@gmail.com")
            new_content = new_content.replace("+91 9307512816", "+91 96770 77009")
            new_content = new_content.replace("+919307512816", "+919677077009")
            new_content = new_content.replace("Crafted by RapidXAI\n                                    .", "pennyworth.AI")
            new_content = new_content.replace("Crafted by RapidXAI \n                                    .", "pennyworth.AI")
            new_content = new_content.replace("Crafted by RapidXAI .\n", "pennyworth.AI\n")
            new_content = new_content.replace("Crafted by RapidXAI", "pennyworth.AI")
            new_content = new_content.replace('width="156" height="34" viewBox="0 0 156 34"', 'width="350" height="34" viewBox="0 0 350 34"')
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {filepath}")
