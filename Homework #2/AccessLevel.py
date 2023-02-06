class AccessLevel:
    def canAccess(rights, minPermission):
        ret = ""
        
        for n in rights:
            if n >= minPermission:
                ret += "A"
            else:
                ret += "D"
                
        return ret
