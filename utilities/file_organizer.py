from pathlib import Path
import shutil


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path.")
        return

    moved_files = 0

    for file in folder.iterdir():
        # Only organize files, not folders
        if not file.is_file():
            continue

        # Get the extension without the dot
        extension = file.suffix.lower().lstrip(".")

        if extension == "":
            extension = "no_extension"

        # Create the destination folder
        destination_folder = folder / extension
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / file.name

        # Avoid overwriting existing files
        if destination_file.exists():
            print(f"Skipped (already exists): {file.name}")
            continue

        shutil.move(str(file), str(destination_file))
        print(f"Moved: {file.name} -> {extension}/")
        moved_files += 1

    print(f"\nDone! {moved_files} file(s) organized.")


if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()

    organize_folder(path)
