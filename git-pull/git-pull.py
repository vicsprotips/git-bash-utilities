# git fetch: search for .git folders from given root and pull origin for each
# usage: python3 gf.py ~/git
# Vic Baker
import os, sys, subprocess
queue = []
errors = []
for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for d in dirs:
        if d == '.git':
            try:
                cmd = f'cd {root}; git -c color.status=always pull'
                returned_output = subprocess.check_output(cmd,shell=True).decode('utf-8')
                if 'nothing to commit' not in returned_output:
                    #queue.append(root)
                    print(f'{root}\n{returned_output}')
            except Exception as e:
                errors.append(root)
                print(f'!!!!!!!!!!!!!!!!!!! {root}\n{e}')


# print('\n\nSummary:')
# for q in queue:
#     print(q)

print('\n\nNot Fetched:')
for q in errors:
    print(q)
