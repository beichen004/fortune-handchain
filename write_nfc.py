import nfc
import ndef

url = 'https://your-fortune.vercel.app?sign=aries&day=today'  # 
替换为你的前端URL
title = '每日运势'

clf = nfc.ContactlessFrontend('usb')
print("请将NFC标签靠近读写器...")
tag = clf.connect(rdwr={'on-connect': lambda tag: False})

if tag:
    record = ndef.SmartposterRecord(url, title)
    message = [record]
    tag.ndef.records = message
    print("URL已成功写入标签！")
clf.close()

