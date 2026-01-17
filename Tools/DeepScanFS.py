from langchain.tools import tool
import json


def deep_scan_fs(path: list) -> str:
    """Performs a deep scan of the filesystem starting from the given path.

    Args:
        path (list): The root directory path to start the deep scan.
    Returns:
        json: A detailed report of the filesystem structure.
    """
    import os
    report = []
    for root, dirs, files in os.walk(path[0]):
        for name in dirs:
            report.append({
                "type": "directory",
                "path": os.path.join(root, name)
            })
        for name in files:
            report.append({
                "type": "file",
                "path": os.path.join(root, name)
            })
    return json.dumps(report, indent=4)

# Example usage:
print(deep_scan_fs(["X:\\"]))