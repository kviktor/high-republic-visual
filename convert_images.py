from pathlib import Path
import subprocess
import os

from PIL import Image
from pilkit.processors import ResizeToFill
from pilkit.utils import save_image
from tqdm import tqdm


def to_webp():
    image_directory = "The High Republic Visual Guide"


    iterator = tqdm(list(Path(image_directory).glob("**/*")))
    for path in iterator:
        if path.is_dir():
            continue

        suffix = path.suffix
        if suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue


        iterator.set_description(path.name)
        iterator.refresh()

        result = subprocess.run(
            ["cwebp", "-q", "75", "-m", "6", "-af", "-metadata",  "all",  str(path), "-o", str(path).replace(suffix, ".webp")],
            capture_output=True,
        )

        if result.returncode == 0:
            path.unlink()


def generate_thumbnails():
    image_directory = "public/images/"
    iterator = tqdm(list(Path(image_directory).glob("**/*")))

    for path in iterator:
        thumbnail = str(path).replace("/images/", "/thumbnails/")
        if path.is_dir():
            os.makedirs(thumbnail, exist_ok=True)
        else:
            suffix = path.suffix
            if suffix.lower() != ".webp":
                continue

            img = Image.open(str(path))
            processor = ResizeToFill(350, 350)
            new_img = processor.process(img)
            save_image(new_img, thumbnail, "webp")


if __name__ == "__main__":
    generate_thumbnails()
