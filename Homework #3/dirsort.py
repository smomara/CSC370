def dirsort(dirs):
    dirs = sorted(dirs, key=lambda x: x.count("/"))
    
    for i in range(1, len(dirs)):
        if dirs[i].count('/') == dirs[i-1].count('/'):
            if dirs[i] < dirs[i-1]:
                j = i
                while j > 0 and dirs[j].count('/') == dirs[j-1].count('/'):
                    if dirs[j] < dirs[j-1]:
                        dirs[j], dirs[j-1] = dirs[j-1], dirs[j]
                    j -= 1
    
    return dirs
