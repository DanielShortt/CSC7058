import unittest, winreg

class test_reg (unittest.TestCase):
    def test_reg(self):
        #Path of the variable
        REG_PATH = "SOFTWARE\DAZ\Studio4"
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
        #get the element to be updated
        sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) 
        newPath = "FILE FOUND" #insert Variable for check
        winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
        #Getting the value of variable set for test
        value, regtype = winreg.QueryValueEx(sKey, 'StartupScene')
        #Test if variable set is equal to variable retrieved from registry
        self.assertIn(value, 'FILE FOUND')
        winreg.CloseKey(sKey) #close the value
        winreg.CloseKey(reg) #close the registry

if __name__ == "__main__":
    unittest.main()