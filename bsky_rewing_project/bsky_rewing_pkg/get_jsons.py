import os
import subprocess

root_path = os.path.abspath(os.path.dirname(__file__))
bin_path = os.path.join(root_path, "bin", "cookbook", "go-repo-export", "go-repo-export")
rsc_path = os.path.join(root_path, "rsc")

DID_tmorcosporras = "did:plc:3hwsg5zd3xfe2h6sdsaojdld"
DID_test1 = "did:plc:42hlwxi6h7df2f5mvvzrciz2"
CAR = ""

def download_repo(DID):
    global CAR
    os.makedirs(rsc_path, exist_ok=True)
    result = subprocess.run(
    [bin_path, "download-repo", DID],
    cwd=rsc_path,
    capture_output=True,
    text=True,
    )
    CAR = result.stdout.split(" to: ")[1].strip()

def unpack_records(CAR):
    subprocess.run([bin_path, "unpack-records", CAR],
    cwd=rsc_path,
    )
    os.remove(os.path.join(rsc_path, CAR))

def get_jsons(DID):
    download_repo(DID)
    print("DR done")
    print(CAR)
    unpack_records(CAR)
    print("End")
