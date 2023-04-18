import re
with open('./regex_test.txt') as f:
    data = f.readlines()
    f.close()

full_name = re.compile('([A-Z][a-z]+) ([A-Z][a-z]*)( [A-Z][a-z]*)?')

for name in data:
    match = full_name.search(name)
    if match:
        print('\n', f"{match[0]}")
    else:
        print('\n','none')
    
    