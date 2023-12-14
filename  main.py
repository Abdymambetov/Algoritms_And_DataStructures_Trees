# Задача 1: Создание дерева сортировки из файла
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_sort_tree_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    root = None
    for num in numbers:
        root = insert_into_sort_tree(root, num)

    return root

def insert_into_sort_tree(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert_into_sort_tree(root.left, value)
    else:
        root.right = insert_into_sort_tree(root.right, value)
    return root


# Задача 2: Печать элементов дерева

def print_tree_recursive(root):
    if root:
        print_tree_recursive(root.left)
        print(root.value)
        print_tree_recursive(root.right)

def print_tree_non_recursive(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value)
        current = current.right


# Задача 3: Вычисление глубины дерева
def tree_depth(root):
    if not root:
        return 0
    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)
    return max(left_depth, right_depth) + 1


# Задача 4: Вычисление количества узлов на заданном уровне дерева
def nodes_at_level(root, level):
    if not root or level < 1:
        return 0
    if level == 1:
        return 1
    return nodes_at_level(root.left, level - 1) + nodes_at_level(root.right, level - 1)


# Задача 5: Подсчет количества повторяющихся элементов в узлах дерева
def count_duplicates(root):
    counter = {}

    def traverse_and_count(node):
        if node:
            traverse_and_count(node.left)
            counter[node.value] = counter.get(node.value, 0) + 1
            traverse_and_count(node.right)

    traverse_and_count(root)
    return counter



# Задача 6: Нахождение максимального четного значения в дереве
def find_max_even_value(root):
    max_even = float('-inf')

    def traverse_and_update_max(node):
        nonlocal max_even
        if node:
            traverse_and_update_max(node.left)
            if node.value % 2 == 0 and node.value > max_even:
                max_even = node.value
            traverse_and_update_max(node.right)

    traverse_and_update_max(root)
    return max_even



# Задача 7: Проверка, подобны ли два бинарных дерева
def are_trees_similar(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if tree1 and tree2:
        return (are_trees_similar(tree1.left, tree2.left) and
                are_trees_similar(tree1.right, tree2.right))
    return False


# Задача 8: Добавление в дерево нового элемента
def insert_into_tree(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    elif value > root.value:
        root.right = insert_into_tree(root.right, value)
    return root


# Задача 9: Удаление из дерева заданного элемента

def delete_from_tree(root, value):
    if not root:
        return root

    if value < root.value:
        root.left = delete_from_tree(root.left, value)
    elif value > root.value:
        root.right = delete_from_tree(root.right, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = find_min_value_node(root.right)
        root.value = temp.value
        root.right = delete_from_tree(root.right, temp.value)

    return root

def find_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Пример создания дерева из файла
tree_root = build_sort_tree_from_file('numbers.txt')

# Пример печати элементов дерева
print("Рекурсивная печать:")
print_tree_recursive(tree_root)

print("\nНерекурсивная печать:")
print_tree_non_recursive(tree_root)

# Пример вычисления глубины дерева
depth = tree_depth(tree_root)
print("\nГлубина дерева:", depth)

# Пример вычисления количества узлов на заданном уровне
level = 2
level_nodes = nodes_at_level(tree_root, level)
print(f"\nКоличество узлов на уровне {level}: {level_nodes}")

# Пример подсчета количества повторяющихся элементов
duplicates = count_duplicates(tree_root)
print("\nПовторяющиеся элементы:")
for key, value in duplicates.items():
    print(f"{key}: {value} раз")

# Пример нахождения максимального четного значения
max_even = find_max_even_value(tree_root)
print("\nМаксимальное четное значение:", max_even)

# Пример добавления нового элемента в дерево
new_value = 42
tree_root = insert_into_tree(tree_root, new_value)
print(f"\nДерево после добавления элемента {new_value}:")
print_tree_recursive(tree_root)

# Пример удаления элемента из дерева
value_to_delete = 42
tree_root = delete_from_tree(tree_root, value_to_delete)
print(f"\nДерево после удаления элемента {value_to_delete}:")
print_tree_recursive(tree_root)
