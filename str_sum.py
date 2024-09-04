import re
def add(str_of_nums):
    '''
    num_str       = str_of_nums
    delimeter     = None
    matches       = re.findall(r'^//(.+?)\\n?(.+)$', str_of_nums)
    print(matches)
    if matches and len(matches[0]) > 1:
        num_str_list = matches[0][1]
        delimeter = matches[0][0]
        if delimeter.startswith('[') and delimeter.endswith(']'):
            matches = re.findall(r'\[(.+?)\]')
            delimeter = matches
    print( delimeter, num_str_list)
    '''
    delimeter = False
    if not delimeter:
        num_str_list = re.findall(r'-?\d+', str_of_nums)
    positive_nums = [int(num) for num in num_str_list if (num != '' and num.isnumeric())]
    negative_nums = [-1 * int(num[1]) for num in num_str_list if num.startswith('-') ]
    print(f'StrOfNums: {num_str_list}, PositiveNums: {positive_nums}, NegativeNums: {negative_nums}')
    total = 0
    try:
        if negative_nums:
            raise Exception('Negative numbers not allowed: ' + ','.join([str(i) for i in negative_nums]))
        total = sum(positive_nums)
    except Exception as e:
        print(f'Encountered exception {e}')
    return total

print(add(r'//;\n1\n2;4\n3;-5;-1;-4'))
print(add(r'//;\n1\n2;4\n3'))