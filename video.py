import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate,vfx

op = 0
while op != '7':
        print('\nBienvenido al editor de videos\n')
        print('\n1)unir dos videos\n2)dividir un video\n3)multiplicar color\n4)cambio de velocidad\n5)voltear video\n6)ejercicio while\n7)Salir')
        op = input('\nIngrese una opcion')

        if op == '1':
        
            ruta_video1 = input('\nIngrese la ruta del primer video:\n') 
            ruta_video2 = input('\nIngrese la ruta del segundo video:\n') 
            
            video1 = VideoFileClip(ruta_video1)
            video2 = VideoFileClip(ruta_video2)
            
            video_final = concatenate([video1, video2])
            
            video_final.write_videofile('video_unido.mp4')
        elif op == '2':
            
            ruta_video = input('\nIngrese la ruta del video:\n')
            tiempo_inicio = input('\nIngrese el tiempo donde incia:\n')  
            tiempo_fin = input('\nIngrese el tiempo donde termina:\n')  
            
            video = VideoFileClip(ruta_video)
            
            video_cortado = video.subclip(int(tiempo_inicio), int(tiempo_fin))
            
            video_cortado.write_videofile('video_corte.mp4')
        elif op == '3':
            ruta_video = input('\nIngrese la ruta del video:\n')
            factor = input('\ningrese el factor a multiplicar\n')
            video = VideoFileClip(ruta_video)
            video_color = video.fx(vfx.colorx,int(factor)) 
            
            video_color.write_videofile('video_color.mp4')
        elif op == '4':
            ruta_video = input('\nIngrese la ruta del video:\n')
            factor = input('\ningrese el factor a multiplicar\n')
            video = VideoFileClip(ruta_video)
            video_vel = video.fx(vfx.speedx, int(factor))
            video_vel.write_videofile('video_vel.mp4')
        elif op == '5':
            ruta_video = input('\nIngrese la ruta del video:\n')
            video = VideoFileClip(ruta_video)
            video_rotado = video.fx(vfx.mirror_y)
            video_rotado.write_videofile('video_rotado.mp4')
        elif op == '6':
            ruta = input('\nIngrese la ruta del video: ')
            video = cv2.VideoCapture(ruta)
            fps = video.get(cv2.CAP_PROP_FPS)
            cont = 0
            while video.isOpened():
                ret, frame = video.read()
                if ret:
                    if cont % int(fps) == 0:
                        cv2.imwrite(f'fotograma_{cont}.jpg', frame)
                    cont += 1
                else:
                    break
                
            video.release()

        elif op == '7':
            print('\nHasta la proximaaaaa\n')




