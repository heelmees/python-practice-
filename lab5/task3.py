with open('lab5\src\general_group.txt', 'r', encoding='utf-8') as file:
    children = file.readlines()

children_data = [child.strip().split() for child in children]

youngest_child = min(children_data, key=lambda x: int(x[2]))
oldest_child = max(children_data, key=lambda x: int(x[2]))

with open('lab5\src\junior_group.txt', 'w', encoding='utf-8') as file:
    file.write(f"{youngest_child[0]} {youngest_child[1]} {youngest_child[2]}")

with open('lab5\src\senior_group.txt', 'w', encoding='utf-8') as file:
    file.write(f"{oldest_child[0]} {oldest_child[1]} {oldest_child[2]}")
