#you need to install two modules first!
# 1- Speechrecognation   use the command "pip install SpeechRecognition" or you can refer "https://pypi.org/project/SpeechRecognition/" for more details
# 2- Pyaudio use command "pip install PyAudio" or you can visit this "https://pypi.org/project/PyAudio/" for more 
# after sucessful installation of these two modules you can start typing the below code!
# pro tip---if you are using pycharm it would be good to download as...there you work in environments and one env dont disturbs the others envs

import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("bolo beta")
    audio=r.listen(source)

    try:
        print("Text is : " + r.recognize_google(audio,language='hi-IN'))
    except:
        pass

