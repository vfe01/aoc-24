import os

for i in range(1, 26):
    dir_name = f"{i:02}"
    os.makedirs(dir_name, exist_ok=True)
    with open(os.path.join(dir_name, '.gitkeep'), 'w') as f:
        pass