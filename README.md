# ИНСТРУКЦИЯ ПО ЭКСПЛУАТАЦИИ

## Запуск программы

**Прежде, чем будете запускать программу, убедитесь, что у Вас установлен Python версии >= 3.5.**

Для запуска программы в директории, где хранится minotaur.py, необходимо написать команду:

    ./minotaur.py root_name

либо же:

    pytnon3 minotaur.py root_name
    
где *root_name* - это имя директории, где будут вестись поиски Минотавра. В ходе работы программа просмотрит все поддиректори и все файлы вида *filename.txt* (начиная обязательно с *"file.txt"*), в которых может быть записано либо *"Minotaur"* (такой файл единственный и его требуется найти), либо несколько строк вида *"@include filename.txt"*, где написаны файлы, где надо продолжить поиск Минтавра, либо *"Deadlock"* (тупик, который не указывает ни на один файл). В случае успеха программа запишет в новый файл путь, который требуется пройти от файла *"file.txt"* к файлу с Минотавром и выведет *"Success!"*, иначе выведет *"There is no Minotaur here"*.

## Пример использования

    ...@...:~$ python3 minotaur.py root
    Success!
    ...@...:~$ cat minotaur_result.txt 
    root/A2/A3/file.txt
    root/A1/file4.txt
    root/A2/file2.txt
    root/A2/A3/file3.txt
