from __future__ import annotations

from pathlib import Path


public_directory = "public/"


iterator = Path(public_directory).glob("**/*")

for path in iterator:
    if not path.is_dir():
        continue

    if path.name.startswith("_"):
        new_path = str(path).replace(path.name, path.name.lstrip("_"))
        path.rename(new_path)
    elif "_" in path.name:
        """
        new_path = str(path).replace(path.name, path.name.replace("_", "'"))
        replace = input(f"{path.name} -> {new_path}")
        if replace == "y":
            path.rename(new_path)
        """
        print(str(path))
