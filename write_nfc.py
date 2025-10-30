import nfc
import time

FRONTEND_URL = "https://fortune-handchain-web-git-main-feifeizhengs-projects.vercel.app?sign=aries&day=today"

def on_connect(tag):
    print("NFC 标签已连接！")
    tag.ndef.message = nfc.ndef.UriRecord(FRONTEND_URL)
    print(f"已写入 URL: {FRONTEND_URL}")
    return True

print("请将 NFC 标签靠近读卡器...")
with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': on_connect})
