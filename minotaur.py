import os
import os.path
import argparse

def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument("root_name")
    pars.add_argument("-f", "--file_name", default = "minotaur_result.txt")
    return pars

def write_in_file(path_to_minor, new_file_name):
    with open(new_file_name, "w") as output:
        for elem in path_to_minor:
             output.write("{}\n".format(elem))

def search_file(start_dir, file_name):
    for root, dirs, files in os.walk(start_dir):
        for f in files:
            if f == file_name:
                return os.path.join(root, f)
    return None

def search_Minotaur(start, file_name, chain):
    chain.append(search_file(start, file_name))
    now_path = chain[-1]
    if now_path is not None:
        with open(now_path) as now:
            lines = now.readlines()
            try:
                if lines[0].strip() == "Minotaur":
                    return 1
                elif lines[0].strip() == "Deadlock":
                    chain.pop()
                    return 0
                for way in lines:
                    if way.split()[0] == '@include' and way.split()[1].endswith(".txt"):
                        if search_Minotaur(start, way.split()[1], chain) == 1:
                            return 1
            except IndexError:
                print("Incorrect file data in {}!".format(now_path))
                return 0
    chain.pop()
    return 0

def start(namespace):
    chain, start_file = list(), "file.txt"
    start_dir, result_file = namespace.root_name, namespace.file_name
    if search_Minotaur(start_dir, start_file, chain) == 1:
        write_in_file(chain, result_file)
        print("Success!")
    else:
        print("There is no Minotaur here") 
    
if __name__ == '__main__':
    start(create_parser().parse_args())
