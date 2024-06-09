def findByString(str:str, arr:list):
    try: 
        arr.index(str)
        return True
    except ValueError:
        return False