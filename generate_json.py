from __future__ import annotations

from pathlib import Path
import json
import re

image_directory = "public/images"
json_directory = "src/assets"


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
                "name": path.name,
                "slug": slugify(path.name),
                "parent": parent or None,
            },
        )

# some hacking around to make them sorted in ascending order but but the
# children one at the end
first_page = sorted(data[:4], key=lambda x: x["name"])
data = first_page[1:] + [first_page[0]] + data[4:]

with open(f"{json_directory}/structure.json", "w") as f:
   json.dump(data, f, separators=(',', ':'))
