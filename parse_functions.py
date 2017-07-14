import re

def parse(file, regex):
    single_items = []
    dim_items = []
    dims = []
    single_dict = {}
    dim_dict = {}
    items_dict = {}
    matched = re.findall(regex, file)
    dim_regex = re.compile(r'(\[\d+\s*:\s*\d+\s*\])')
    for each in matched:
        dim = [];
        dim = re.findall(dim_regex, each)
        if dim:
            temp = re.sub(r'(\[\d+\s*:\s*\d+\s*\])', '', each)
            temp = re.sub(r'\s', '', temp)
            dim_items = dim_items + re.split(r',', temp)
            for each in dim_items:
                dims.append(dim)
        else:
            temp = re.sub(r'\s', '', each)
            single_items = single_items + re.split(r',', temp)
            for each in dim_items:
                dims.append(dim)
    for each in single_items:
        single_dict[each] = '[0:0]'
    dim_dict = dict(zip(dim_items, dims))
    items_dict.update(single_dict)
    items_dict.update(dim_dict)
    print items_dict
    return items_dict