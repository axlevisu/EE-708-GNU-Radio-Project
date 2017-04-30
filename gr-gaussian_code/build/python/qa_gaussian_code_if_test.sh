#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/axle/Dropbox/Semester\ 8/EE\ 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/axle/Dropbox/Semester\ 8/EE\ 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/build/swig:$PYTHONPATH
/usr/bin/python2 /home/axle/Dropbox/Semester 8/EE 708/project/EE-708-GNU-Radio-Project/gr-gaussian_code/python/qa_gaussian_code_if.py 
