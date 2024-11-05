from pathlib import Path
import subprocess

from tqdm import tqdm

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

    old_size = path.stat().st_size

    result = subprocess.run(
         ["cwebp", "-q", "75", "-m", "6", "-af", "-metadata",  "all",  str(path), "-o", str(path).replace(suffix, ".webp")],
        capture_output=True,
    )

    if result.returncode == 0:
        path.unlink()
