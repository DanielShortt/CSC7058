import winreg

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)

newPath = "lol" #insert path of scene here.

winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath)
winreg.CloseKey(sKey)
winreg.CloseKey(reg)