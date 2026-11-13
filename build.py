"""
Zip the Porchlight packs for the server.

    python build.py

Writes to dist/:
  porchlight-trophies.zip   -> drop into <world>/datapacks/ on the server, then /reload
  porchlight-resources.zip  -> host it and set resource-pack / resource-pack-sha1
                               in server.properties (the SHA-1 is printed below)

Standard library only. Every file is validated as JSON first so a typo fails
here rather than silently in-game.

Adding a trophy later:
  1. datapack: add a loot table under data/porchlight/loot_table/trophies/ that
     names a player head, plus whatever advancement/function awards it.
  2. resource pack: add the model + texture under assets/porchlight/, then add
     one more entry to "cases" in assets/minecraft/items/player_head.json whose
     "when" lists the exact name(s) the loot table gives.
"""

import hashlib
import json
import pathlib
import sys
import zipfile

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
PACKS = {
    "porchlight-trophies": "porchlight-trophies.zip",
    "porchlight-resources": "porchlight-resources.zip",
}
# Fixed timestamp so the zip (and its SHA-1) only changes when the contents do.
ZIP_DATE = (2026, 1, 1, 0, 0, 0)


def validate(folder: pathlib.Path) -> int:
    errors = 0
    for path in sorted(folder.rglob("*")):
        if path.suffix in (".json", ".mcmeta"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except ValueError as exc:
                print(f"  INVALID JSON  {path.relative_to(HERE)}: {exc}")
                errors += 1
    return errors


def build(folder: pathlib.Path, target: pathlib.Path) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                info = zipfile.ZipInfo(path.relative_to(folder).as_posix(), ZIP_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(info, path.read_bytes())


def main() -> int:
    DIST.mkdir(exist_ok=True)
    errors = sum(validate(HERE / name) for name in PACKS)
    if errors:
        print(f"{errors} file(s) failed validation; nothing was built.")
        return 1
    for name, zip_name in PACKS.items():
        target = DIST / zip_name
        build(HERE / name, target)
        sha1 = hashlib.sha1(target.read_bytes()).hexdigest()
        print(f"{target.relative_to(HERE)}  ({target.stat().st_size} bytes)  sha1 {sha1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
