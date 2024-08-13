# check git: search for .git folders from given root and notify you if you have changes to commit
# usage: python3 check-git.py ~/git
# Vic Baker

import os, sys, subprocess

queue = []
for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for d in dirs:
        if d == '.git':
            print(root, d)
            cmd = f'cd {root}; git -c color.status=always status'
            returned_output = subprocess.check_output(cmd,shell=True).decode('utf-8')
            if 'nothing to commit' not in returned_output:
                queue.append(root)
                print(f'{root}\n{returned_output}')

print('\n\nSummary:')
for q in queue:
    print(q)
