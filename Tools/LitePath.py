from langchain.tools import tool
from typing import List
import os
import json

@tool
def LitePath(path: List[str]) -> str:
    """This tool helps to find all files and directories (level one only) in given paths.

    Args:
        path (list): A list of directory paths to search. Each path will be scanned for immediate files and directories.

    Returns:
        json: A JSON string containing files with their types and directories from all specified paths.
    """
    
    results = {}
    all_files = []
    all_directories = []
    
    for directory in path:
        try:
            items = os.listdir(directory)
            files = []
            directories = []
            
            for item in items:
                full_path = os.path.join(directory, item)
                if os.path.isfile(full_path):
                    file_extension = os.path.splitext(item)[1] if os.path.splitext(item)[1] else "No extension"
                    file_info = {
                        "path": full_path,
                        "name": item,
                        "type": file_extension
                    }
                    files.append(file_info)
                    all_files.append(file_info)
                elif os.path.isdir(full_path):
                    directories.append(full_path)
                    all_directories.append(full_path)
            
            results[directory] = {
                "files": files,
                "directories": directories
            }
        except Exception as e:
            results[directory] = {"error": str(e)}
    
    final_result = {
        "locations": results,
        "summary": {
            "total_files": len(all_files),
            "total_directories": len(all_directories)
        }
    }
    return json.dumps(final_result, indent=2)
