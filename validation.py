

class Validation:

    def checkEmpty(self,dataList):
        for d in dataList:
            if d=='':
                return True
        
        return False
    
    def checkMobile(self,data):
        if len(data)!=10 or (not data.isdigit()):
            return True
        
        return False
    
    def checkAlpha(self,data):
        if (not data.isalpha()):
            return True
        return False
    
    def checkDigit(self,data):
        if not data.isdigit():
            return True

        return False
