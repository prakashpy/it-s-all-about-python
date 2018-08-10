import os
import sys

#change present working directory
os.chdir("/home/analysis")

# prints present working dir
print os.getcwd()

# get list of files in some directory
list_of_files = os.listdir("/home/analysis")
print "list_of_files: ", list_of_files


# get's the file name and removes all prefixes
input_file = os.path.basename("/home/analysis/my-test-file.py")
print input_file

PIPELINE_DIR = "/usr/lib/projct_path/modules"
sys.path.insert(0, PIPELINE_DIR)

PIPELINE_DIR = '/usr/lib/projct_path'
sys.path.append(PIPELINE_DIR + '/modules')

if os.path.isfile("my-file-name.py") is True:
    print "file exits!"

if os.path.isdir(PIPELINE_DIR) is False:



if str(os.getcwd()) != str(genotype_pipeline_path):
    print "not equal"

#delete file only if exists
if os.path.isfile(file_name):
    os.remove(file_name)
