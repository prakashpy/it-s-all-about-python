#uses of re module of python for manipulating with regualr expressions

import re

input = "12_34_abc.1aX1b_final.vcf.gz"

#code below is not compliant with pep-8 standard
new_input_renamed = re.sub("\.gz$", "", input)
print new_input_renamed
# output on console: 12_34_abc.1aX1b_final.vcf


#code below is not compliant with pep-8 standard
new_input_renamed = re.sub(r"\.gz$", "", input)
print new_input_renamed
# output on console: 12_34_abc.1aX1b_final.vcf



# TIP 
""" Replace "re.search('\.gz$', file)" with "file.endswith('.gz')" which is ten-times faster and reduces overhead. """
file = "some_random_name.vcf.gz"
if re.search('\.gz$', file):
    print "File do has gz extension"
# code below is more efficient than above
if file.endswith('.gz'):
    print "File do has gz extension"

if file.startswith('some'):
    print "file name starts with some."

# root, ext = os.path.splitext(filename)
