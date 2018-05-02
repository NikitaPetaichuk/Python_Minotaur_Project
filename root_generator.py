import os
import os.path
import random
import sys

STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TREE_MODEL = {"file":"abcd", "a":"efg", "b":"h", "c":0, "d":"ij", "e":"kl", "f":0, "g":"mn", "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0}

def dir_tree_generate(root, depth):
    if depth <= 0:
        return
    try:
        os.mkdir(root)
        os.chdir(root)
        for i in range(0, random.randint(1, 3)):
            new_dir = ""
            for j in range(0, 5):
                new_dir += random.choice(STRING)
            dir_tree_generate(new_dir, depth - 1)
        os.chdir('..')
        return 1
    except OSError:
        print("This directory already exists!")
        return 0

def create_files(tree, root_list):
    for key, value in tree.items():
        with open(os.path.join(random.choice(root_list), key + ".txt"), "w") as new_file:
            if value == "Minotaur":
                new_file.write(value)
            elif value == 0:
                new_file.write("Deadlock")
            else:
                for i in range(0, len(value)):
                    new_file.write("@include " + value[i] + ".txt\n")

if __name__ == '__main__':
    try:
        root_name, depth = sys.argv[1], int(sys.argv[2])
        if dir_tree_generate(root_name, depth) == 0:
            sys.exit(0)
    except (IndexError, ValueError):
        print("Incorrect arguments!")
        sys.exit(0)
    tree, now_key = TREE_MODEL, "file"
    while tree[now_key] != 0:
        now_key = random.choice(tree[now_key])
    tree[now_key], file_sys_tuple, root_list = "Minotaur", os.walk(root_name), list()
    for elem in file_sys_tuple:
        root_list.append(elem[0])
    create_files(tree, root_list)
