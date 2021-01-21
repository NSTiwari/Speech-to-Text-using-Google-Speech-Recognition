import speech_recognition as sr 
import moviepy.editor as mp

clip = mp.VideoFileClip(r"audio.mp4") 
 
clip.audio.write_audiofile(r"audio_converted.wav")
r = sr.Recognizer()

audio = sr.AudioFile("audio_converted.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file) # language='hi-IN')

with open('recognized.txt', mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")