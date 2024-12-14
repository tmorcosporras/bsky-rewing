import os
import subprocess
import requests
from . import os_functions

root_path = os_functions.find_root(__file__)
gre_repo_path = os.path.join("bin", "cookbook", "go-repo-export") 
gre_bin_path = os.path.join(gre_repo_path, "go-repo-export")
rsc_path = "rsc"
DID = ""
CAR = ""

def make_binary(): # Verifies the existence of the required binaries
    if not os.path.exists(gre_repo_path):
        raise Exception("go-repo-export directory not found. Probably broken install. If the problem persists, inform the author.") # Can't find the go-repo-export directory, then there's a problem with the install
    elif not os.path.exists(gre_bin_path):
        os.chdir(gre_repo_path)
        subprocess.run(["go build ./..."]) # Found the directory, but can't find the bin inside it, needs to go build
        os.chdir(root_path) # Returns to root directory

"""
def check_repo(DID):
    if DID[0:3] != "did:":
        subprocess.run(
        [curl f"https://bsky.social/xrpc/com.atproto.identity.resolveHandle?handle={DID}"],
        capture_output=True
        DID = result.stdout.
    os.path.exists(os.path.join(rsc_path, DID)
"""

def check_repo(ID):
    global DID, CAR
    
    if ID[0:7] == "did:plc:":
        DID = ID
    
    else:
        url = f"https://bsky.social/xrpc/com.atproto.identity.resolveHandle?handle={ID}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            DID = data.get("did")
    
    CAR = f"{DID}.car"
    return os.path.exists(os.path.join(rsc_path, DID))

def download_repo(DID):
    os.makedirs(rsc_path, exist_ok=True)
    
    result = subprocess.run(
    [os.path.join(root_path, gre_bin_path), "download-repo", DID],
    cwd=rsc_path,
    )

def unpack_records(CAR): # Extracts JSONS from .car at rsc/CAR
    subprocess.run(
    [os.path.join(root_path, gre_bin_path), "unpack-records", CAR],
    cwd=rsc_path,
    ) # Runs go-repo-exports unpack-records with the .car file, saves the JSON's folder in rsc/
    
    os.remove(os.path.join(rsc_path, CAR)) # Deletes the .car file

def did2jsons(ID): # Runs the previous functions in order
    global DID, CAR
    os.chdir(root_path)
    make_binary()
    print("Bin done")
    if check_repo(ID):
        print("Records already unpacked")
        return DID
    download_repo(DID)
    print("Download repo done")
    unpack_records(CAR)
    print("Unpack records done")
    print("End")
    return DID
