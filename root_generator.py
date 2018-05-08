import os
import os.path
import random
import argparse

STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TREE_MODEL = {"file":"abcd", "a":"efg", "b":"h", "c":0, "d":"ij", "e":"kl", "f":0, "g":"mn", "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0}

def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument("root_name")
    pars.add_argument("depth", type = int)
    return pars

def create_tree():
    tree, leaves = TREE_MODEL, list(filter(lambda key: TREE_MODEL[key] == 0, TREE_MODEL.keys()))
    tree[random.choice(leaves)] = "Minotaur"
    return tree

def dir_tree_generate(root, depth, dir_list):
    if depth <= 0:
        return
    try:
        os.mkdir(root)
        dir_list.append(root)
        for i in range(0, random.randint(1, 5)):
            new_dir = ""
            for j in range(0, 5):
                new_dir += random.choice(STRING)
            dir_tree_generate("{0}/{1}".format(root, new_dir), depth - 1, dir_list)
    except OSError:
        raise
        

def create_files(dir_list):
    tree = create_tree()
    for key, value in tree.items():
        with open(os.path.join(random.choice(dir_list), "{}.txt".format(key)), "w") as new_file:
            if value == "Minotaur":
                new_file.write(value)
            elif value == 0:
                new_file.write("Deadlock")
            else:
                for i in range(0, len(value)):
                    new_file.write("@include {}.txt\n".format(value[i]))

if __name__ == '__main__':
    try:
        dir_list, namespace = list(), create_parser().parse_args()
        dir_tree_generate(namespace.root_name, namespace.depth, dir_list)
        create_files(dir_list)
        print("Successfully done!")
    except OSError:
        print("The directory \"{}\" already exists!".format(namespace.root_name))
