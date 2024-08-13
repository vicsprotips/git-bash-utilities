# git fetch (multi-process): search for .git folders from given root and pull origin for each
# much faster than non-mp version
# usage: python3 gf.py ~/git
# Vic Baker

import multiprocessing
import subprocess

import os,sys
import requests

def doWork(params):
    # check provided dir for git updates
    try:
        dir = params
        # print(f"processing: {dir}")
        cmd = f'cd {dir}; git -c color.status=always pull'
        returned_output = subprocess.check_output(cmd,shell=True).decode('utf-8')
        return f"{dir}:{returned_output}".strip()
    except Exception as e:
        return f"{dir}: unable to pull -- local changes?".strip()

if __name__ == '__main__':
    rootDir=sys.argv[1]
    
    import os, sys, subprocess
    queue = []
    print(f"Generating queue for {rootDir}")
    for root, dirs, files in os.walk(rootDir, topdown=True):
        if ".git" in dirs:
            queue.append(root)

    print("Queue created.  Starting pool")
    
    pool = multiprocessing.Pool()
    results = pool.map(doWork, queue)
    pool.close()
    print("Subprocess pools done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    c = 0
    updates = []
    for r in results:
        if not r.endswith("Already up to date."):
            c = c + 1
            updates.append(r.split(':', 1)[0])
            print(r)
    if len(updates) > 0:
        print("\n\nThe following repos had updates:")
        for r in updates:
            print(r)


    