import time
import keyboard
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def recognize():
	content = ''
	while True:
		print("Say something ...")

		with mic as source:
			r.adjust_for_ambient_noise(source) #雑音対策
			audio = r.listen(source)

		print ("Now to recognize it...")

		try:
			result = r.recognize_google(audio, language='ja-JP')
			print(result)
			if "エンター" in result:
				content += result.replace("エンター",'')
				print("end")
				keyboard.press_and_release('t')
				time.sleep(1)
				keyboard.write(content)
				time.sleep(1)
				keyboard.press_and_release('enter')
				time.sleep(0.5)
				keyboard.press_and_release('esc')

				main()
				break
			elif "キャンセル" in result:
				print("end")
				main()
				break
			else:
				content += result
		# 以下は認識できなかったときに止まらないように。
		except sr.UnknownValueError:
			print("could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
def main():
		keyboard.wait('v')
		recognize()

main()