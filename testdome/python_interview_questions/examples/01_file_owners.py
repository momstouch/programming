def group_by_owners(files):
    ret_dic = {}
    
    for file, owner in files.items():
        ret_dic[owner] = ret_dic.get(owner, []) + [file]
        
    return ret_dic

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    assert group_by_owners(files) == \
            {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
