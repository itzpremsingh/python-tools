from pathlib import Path

tree = []


def walk(_dir: str):
    path = Path(_dir)
    iters = path.iterdir()
    files, folders = [], []

    for iter in iters:
        if iter.is_file():
            files.append(iter.name)

        elif iter.is_dir():
            folders.append(str(iter))

    branch = []

    branch.append(str(path))
    branch.append(files)
    branch.append(folders)

    tree.append(branch)

    for folder in folders:
        walk(folder)

    return tree


for path, files, folders in walk("../"):
    print(path)
    if files:
        print("files:", ", ".join(files))

    if folders:
        print("folders:", ", ".join(folders))
