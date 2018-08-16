# use of subprocess to call R files

import subprocess

# make sure file is present in pwd
r_script_path = 'some_random.R'

# return val 0 means successful execution

""" executes the R Script and returns 1 on success; """
cmd = (
    ['Rscript', r_script_path, '--input-file', 'test', "--my-test-param", "y"])

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
""" Ensure script completes """
out, err = proc.communicate()
ret_code = proc.returncode
""" return code 0 means successful execution; """
if ret_code is 0:
    print 1
else:
    print "FAIL"