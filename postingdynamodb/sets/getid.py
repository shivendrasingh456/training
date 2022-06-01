
def GetId(dict):        
        return ''.join(e.upper() for e in dict["display_name"] if e.isalnum())