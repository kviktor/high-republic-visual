from __future__ import annotations

from pathlib import Path
import json
import re

image_directory = "public/images/"


def slugify(value):
    value = str(value)
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_").replace("_", "-")



iterator = Path(image_directory).glob("**/*")
data = []

for path in iterator:
    tags = []
    for parent in path.parents[::-1][3:]:
        tags.append(parent.name)

    parent = "_".join(slugify(tag) for tag in tags)
    if path.is_dir():
        data.append(
            {
                # "type": "d",
                "name": path.name,
                "slug": slugify(path.name),
                "parent": parent or None,
            },
        )
    else:
        suffix = path.suffix
        if suffix.lower() != ".webp":
            continue

        data.append(
            {
                # "type": "i",
                "name": path.name,
                "slug": slugify(path.name),
                "parent": parent or None,
            },
        )


with open("src/assets/structure.json", "w") as f:
   json.dump(data, f, separators=(',', ':'))
