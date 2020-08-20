from os import system as sys
p = input("\t\t\tChat me for For your requirements \n").lower()
while True:
  if("run" in p)or ("open" in p):
    if("browser" in p):
      if("chrome" in p):
        sys("chrome")
        break
      elif("firefox" in p):
        sys("firefox")
        break
      elif("edge" in p):
        sys("start microsoft-edge:")
        break
      elif("chromium" in p):
        sys("chromium-browser")
        break
      else:
        sys("iexplore")
        break
    elif((("media" in p)and("player" in p))or("mp3 player"in p) or (("music" in p)nd("player" in p)):
      path=input("Can u say me the path where is should find the mp3 player or i will direcly load the player")
      if(path!=""):
        sys("wmplayer"+path)
      sys("wmplayer")
      break
    elif("calculator" in p):
      sys("calc")
      break
    elif("about windows" in p):
      sys("winver")
      break
    elif("administrative tools" in p):
      sys("control admintools")
      break
    elif("c drive" in p):
      sys("c:")
      break
    elif("check disk" in p):
      sys("chkdsk")
      break
    elif("command prompt" in p):
      sys("cmd")
      break
    elif("powershell" in p):
      sys("powershell")
      break
    elif("contacts"in p):
      sys("wab")
      break
    elif("date and time"in p):
      sys("timedate.cpl")
      break
    elif("time" in p):
      sys("time")
      break
    elif("excel"in p):
      sys("excel")
      break
    elif("file explorer"in p)or("file manager" in p):
      sys("explorer")
      break
    elif("file history" in p):
      sys("filehistory")
      break
    elif("outlook"in p):
      sys("Outlook")
      break
    elif("paint" in p):
      sys("mspaint")
      break
    elif("powerpoint" in p):
      sys("powerpnt")
      break
    elif("narrator" in p):
      sys("narrator")
      break
    elif("network connection" in p):
      sys("control netconnections")
      break
    elif("dvd player"in p):
      sys("dvdplay")
      break
    elif("scanner" in p):
      sys("wiaacmgr")
      break
    elif("services" in p):
      sys("services.msc")
      break
    elif("sound setting"in p):
      sys("mmsys.cpl")
      break
    elif("task manager"in p):
      sys("launchtm")
      break
    elif("task scheduler"in p):
      sys("taskschd.msc")
      break
    elif("active connection"in p):
      sys("netstat")
      break
    elif("volume setting"in p):
      sys("sndvol")
      break
    elif("firewall"in p):
      sys("firewall.cpl")
      break
    elif("word[ad" in p):
      sys("wordpad")
      break
    elif("word"in p):
      sys("word")
      break
    elif("notepad" in p):
      sys("notepad")
      break
    elif("ip data"in p):
      sys("ipconfig")
      break  
    elif("disk cleaner" in p):
      sys("cleanmgr")
      break
    elif("control panel"in p):
      sys("control")
      break
  elif("log out" in p):
     sys("logoff")
     break 
  elif("power off"in p):
    sys("shutdown /s")
    break
  elif("java web starter" in p):
    sys("javaws")
    break
  elif("python"in p):
    sys("python")
    break
  elif("step recoreder"in p):
    sys("psr")
    break
  elif("keyboard"in p):
    sys("osk")
    break
  elif("math input"in p):
    sys("mip")
    break
  elif("console root"in p):
    sys("mmc")
  elif("exit"in p)or("quit" in p):
    sys("break")
    break