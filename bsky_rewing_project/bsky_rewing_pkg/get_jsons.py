import os
import subprocess

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
gre_repo_path = os.path.join("bin", "cookbook", "go-repo-export") 
gre_bin_path = os.path.join(gre_repo_path, "go-repo-export")
rsc_path = "rsc"
CAR=""

def make_binary(): # Verifies the existence of the required binaries
    if not os.path.exists(gre_repo_path):
        raise Exception("go-repo-export directory not found. Probably broken install. If the problem persists, inform the author.") # Can't find the go-repo-export directory, then there's a problem with the install
    elif not os.path.exists(gre_bin_path):
        os.chdir(gre_repo_path)
        subprocess.run(["go build ./..."])
        os.chdir(root_path) # Found the directory, but can't find the bin inside it, needs to go build

def download_repo(DID): # Downloads the .car file from the AT handle
    global CAR
    os.makedirs(rsc_path, exist_ok=True) # Ensures the existence of rsc directory
    result = subprocess.run(
    [os.path.join(root_path, gre_bin_path), "download-repo", DID],
    cwd=rsc_path,
    capture_output=True,
    text=True,
    ) # Runs go-repo-export download-repo with the AT handle, saves the .car file in rsc/
    CAR = result.stdout.split(" to: ")[1].strip() # Saves the name of the .car file to the CAR variable

def unpack_records(CAR): # Extracts JSONS from .car at rsc/CAR
    subprocess.run(
    [os.path.join(root_path, gre_bin_path), "unpack-records", CAR],
    cwd=rsc_path,
    ) # Runs go-repo-exports unpack-records with the .car file, saves the JSON's folder in rsc/
    os.remove(os.path.join(rsc_path, CAR)) # Deletes the .car file

def get_jsons(DID): # Runs the previous functions in order
    make_binary()
    print("Bin done")
    download_repo(DID)
    print("Download repo done")
    #print(CAR)
    unpack_records(CAR)
    print("Unpack records done")
    print("End")
