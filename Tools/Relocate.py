from langchain.tools import tool
from typing import List

@tool
def Relocate(source_paths: List[str], destination_paths: List[str]) -> str:
    """Relocates files and directories from source paths to a destination path.

    Args:
        source_paths (list): A list of file and directory paths to be moved.
        destination_paths (list): A list of destination directory paths where the files and directories should be moved.

    Returns:
        str: A message indicating the result of the relocation operation.
    """
    import os
    import shutil

    result = ""

    try:
        for src, dest in zip(source_paths, destination_paths):
            if not os.path.exists(src):
                result += f"Source path '{src}' does not exist.\n"
                continue

            if not os.path.exists(dest):
                os.makedirs(dest)

            base_name = os.path.basename(src)
            dest_path = os.path.join(dest, base_name)

            shutil.move(src, dest_path)
            result += f"Moved '{src}' to '{dest_path}'.\n"

        return result.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"