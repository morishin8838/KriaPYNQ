#
# Please Vitis Command Prompt and python.exe run_hls.py
#
# 1) Download HLS-Tiny-Tutorials
# 2) open Vitis Command Prompt
# 3) cd .\HLS-Tiny-Tutorials
# 4) python.exe run_hls.py
#

import os
import subprocess
_current=os.getcwd()
print(_current)
for current, subfolders, subfiles in os.walk(_current):
    print("-------------------------------------------------------")
    print(f"current folder is  : {current}")
    print(f"sub-folder list is : {subfolders}")
    print(f"files is           : {subfiles}")
    print("-------------------------------------------------------")
    if 'run_hls.tcl' in subfiles:
        os.chdir(str(current))
        print(os.getcwd())
        if os.path.isfile('run_hls.tcl'):
            print('run_hls.tcl')
            cmd = "vitis_hls -f run_hls.tcl"
            os.system(cmd)
#            subprocess.run(cmd)
print("")
print("<<< Completed >>>")
abc="cd "+ str(_current)
print(abc)
os.system(abc)
   
