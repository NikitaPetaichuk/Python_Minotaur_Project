import os
import os.path
import sys

def write_in_file(path_to_minor):
    with open("minotaur_result.txt", "w") as output:
        for elem in path_to_minor:
             output.write(elem + "\n")

def search_file(start_dir, file_name):
    for root, dirs, files in os.walk(start_dir):
        for f in files:
            if f == file_name:
                return os.path.join(root, f)
    return None

def search_Minotaur(start, file_name, chain):
    chain.append(search_file(start, file_name))
    now_path = chain[len(chain) - 1]
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
                    if way.split()[0] == '@include' and way.split()[1].endsWith(".txt"):
                        if search_Minotaur(start, way.split()[1], chain) == 1:
                            return 1
            except IndexError:
                print("Incorrect file data in " + now_path + "!")
                return 0
    chain.pop()
    return 0

if __name__ == '__main__':
    try:
        start_dir, now_file, chain = sys.argv[1], "file.txt", list()
        if search_Minotaur(start_dir, "file.txt", chain) == 1:
            write_in_file(chain)
            print("Success!")
        else:
            print("There is no Minotaur here")
    except IndexError:
        print("Usage: python3 minotaur.py root_name")
