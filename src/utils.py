import patoolib
import os

def make_rar(file_path:str):
    counter = 0
    path = ""
    with open("counter.txt", "r") as file:
        counter = file.readline()
        rar_file = "rar_file" + counter + ".rar"
        path = os.path.join("Zip Files\\", rar_file)
    patoolib.create_archive(path, (file_path, "readme.txt", r"src\tree_constructor.py"))
    return path


if __name__ == "__main__":
    # patoolib.create_archive(r"Zip Files\rar_file1.rar", (r"Files\file1.pkl", "readme.txt", r"src\tree_constructor.py"))
    path = make_rar("Files\\file1.pkl")
    print(path)