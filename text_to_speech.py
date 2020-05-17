from gtts import gTTS
import os

fh=open("test.txt","r",encoding="utf8")
myText=fh.read().replace("\n"," ")

language='hi'

output=gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")
