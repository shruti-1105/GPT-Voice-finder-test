import openai
import speech_recognition as sr
import pyttsx3
import time 

openai.api_key = "sk-u8JdqahbFnF7g7ERQbRtT3BlbkFJgOsb63n90wzc8G6fZYq55"

engine=pyttsx3.init()


def transcribe_audio_to_test(filename):
    recogizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recogizer.record(source) 
    try:
        return recogizer.recognize_google(audio)
    except:
        print("skippinG error")

def generate_response(prompt):
    response= openai.completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response ["Choices"][0]["text"]
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Say 'slave' to start recording your question")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower()=="slave":
                    #record audio
                    filename ="input.wav"
                    print("Say your question")
                    with sr.Microphone() as source:
                        recognizer=sr.recognize()
                        source.pause_threshold=1
                        audio=recognizer.listen(source,phrase_time_limit=100,timeout=None)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                            

                    text=transcribe_audio_to_test(filename)
                    if text:
                        print(f"yuo said {text}")
                        
                        #Generate the response
                        response = generate_response(text)
                        print(f"chat gpt 3 say {response}")
                            
                        #read resopnse using GPT3
                        speak_text(response)
            except Exception as e:
                
                print("An error ocurred : {}".format(e))
if __name__=="__main__":
    main()
