import os
import json
from datetime import datetime
from . import os_functions

root_path = os_functions.find_root(__file__)
rsc_path = "rsc"
atproto_did: "did:plc:ewvi7nxzyoun6zhxrhs64oiz"

pr_js = "app.bsky.actor.profile" # You finished your NUMBER year in bsky
lk_js = "app.bsky.feed.like" # You liked NUMBER posts
ps_js = "app.bsky.feed.post" # You made NUMBER posts, with WORDS being your top 5 most common word and TOPICS your main topics
rp_js = "app.bsky.feed.repost" # You made NUMBER reposts, with PERSON being the most usua with NUMBER reposts
fl_js = "app.bsky.feed.post" # You followed NUMBER people, with MONTH being the highest month with NUMBER follows

#def time_extract(TIME):
    

def read_profile_jsons(DID):
    os.chdir(os.path.join(root_path, rsc_path, DID, pr_js))
    with open("self.json") as file:
        profile = json.load(file)
    #profile["description"]
    print(datetime.strptime(profile["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ"))
