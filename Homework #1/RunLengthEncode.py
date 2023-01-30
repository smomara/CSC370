class RunLengthEncode:
    def encode(s):
        ret = ''
        
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            count = j - i
            if count >= 5:
                ret += "/{:02d}{}".format(count, s[i])
            else:
                ret += s[i:j]
            i = j
        return ret
