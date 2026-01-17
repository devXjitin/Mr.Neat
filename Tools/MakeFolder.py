from langchain.tools import tool
from typing import List

@tool
def MakeFolder(folder_path: List[str], folder_name: List[str]) -> str:
    """"This tool creates new folders at specified paths with given names.

    Args:
        folder_path (list): A list of directory paths where the new folder(s) should be created.
        folder_name (list): A list of names for the new folder(s) to be created.

    Returns:
        str: A message indicating the result of the folder creation operation.
    """
    import os

    result = ""

    try:
        for path, name in zip(folder_path, folder_name):
            full_path = os.path.join(path, name)
            if not os.path.exists(full_path):
                os.makedirs(full_path)
                result += f"Folder '{name}' created successfully at '{path}'.\n"
            else:
                result += f"Folder '{name}' already exists at '{path}'.\n"
        return result.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"