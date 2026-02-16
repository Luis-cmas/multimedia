import librosa
import numpy as np
from pydub import AudioSegment
AudioSegment.converter = "C:\\FFmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\FFmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\FFmpeg\\bin\\ffprobe.exe"
from gtts import gTTS
import soundfile
import pyaudio
import speech_recognition as sr
import os
import datetime
import matplotlib.pyplot as plt


opcion="0"
while opcion !="6":
    print("\nhola mundo,este es mi proyecto de multimedia y exploraremos lo que podemos hacer con los audios")
    print(" \n 1)Crear nota en el diario\n 2)Analizar un archivo de audio\n 3)Unir dos audios\n 4)Dividir un audio\n 5)Convertir texto a audio\n 6)salir")
    opcion = input("Seleccione una opcion")
    if opcion == "1":

        
        y=input('presione enter para empezar')
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language = 'ES')
        print(f'Has dicho: {text}')
        #abriendo el diario
        
        file = open("diario.txt", "a")
        file.write(str(datetime.datetime.now()) + os.linesep)
        file.write(text+ os.linesep)
        file.close()
        x=input('accion realizada,presione enter para volver al menu')
        os.system("cls")

    elif opcion == "2":
        
        myaudio=input("escriba el archivo a usar (si no esta en la carpeta escriba la ruta)\n")
        y,fs=librosa.load(myaudio)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=fs)
        #Graficar el audio
        plt.figure(figsize=(12, 4))
        librosa.display.waveshow(y, sr=fs)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud')
        plt.title('Audio')
        plt.show()

        # Calcular el espectrograma
        spectrogram = librosa.stft(y)

        # Convertir a escala logarítmica
        log_spectrogram = librosa.amplitude_to_db(spectrogram, ref=np.max)
        # Visualizar el espectrograma
        plt.figure(figsize=(12, 6))
        librosa.display.specshow(log_spectrogram, sr=fs, x_axis='time', y_axis='log')
        #, x_axis='tiempo', y_axis='log'
        #plt.xlabel('Tiempo (s)')
        #plt.ylabel('Amplitud(log)')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Espectrograma')
        plt.show()



        print('\nEl audio tiene un tempo de: {:.2f} beats por minuto'.format(tempo))
        print('\nse tiene una frecuencia de muestreo de:',fs,"muestras por segundo")
        input("\npresione enter para continuar\n")
        os.system("cls")

    elif opcion == "3":
        
        audio1s=input('ingrese la ruta y nombre del archivo de audio inicial\n')
        audio2s=input('ingrese la ruta y nombre del archivo de audio final\n')
        
        audio1=AudioSegment.from_wav(audio1s)
        audio2=AudioSegment.from_wav(audio2s)
        audiof = audio1 + audio2
        audiof.export("union.wav")
        os.system("start union.wav")
        print("opcion 3,presione enter para continuar\n")
        x=input()
        os.system("cls")

    elif opcion == "4":
        
        audios=input('ingrese la ruta y nombre del archivo de audio a cortar\n')
        tiempo1=input('desde que segundo quiere cortarlo')
        tiempo2=input('hasta que segundo quiere cortarlo')

        audio=AudioSegment.from_wav(audios)
        corte = audio[int(tiempo1)*1000:int(tiempo2)*1000]
        corte.export("corte.wav")
        os.system("start corte.wav")
        
        print("opcion 4,presione enter para continuar\n")
        x=input()
        os.system("cls")

    elif opcion == "5":
        texto = input("Escriba el texto que desea convertir en audio\n")
        oracion = gTTS(text=texto,lang='es-us',slow=False)
        oracion.save("discurso.wav")
        os.system("start discurso.wav")
        input("trabajo realizado,presione enter para volver al menu\n")
        
    elif opcion == "6":
        print("fue un placer UwU")
    
    else:
        x=input("Esa opcion no esxiste >:c,presione enter para continuar\n")
        os.system("cls")