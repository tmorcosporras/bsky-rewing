import os

def find_root(subpath):
    match os.path.basename(subpath):
        case "/" | "~":
            raise Exception("Root directory not found. Make sure the parent folder of 'bsky_rewing_project' is called 'bsky-rewing'")
        case "bsky_rewing" | "bsky-rewing":
            return subpath
        case _:
            return find_root(os.path.dirname(subpath))
