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