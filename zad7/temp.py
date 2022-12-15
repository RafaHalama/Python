import numpy as np
import math
import matplotlib.pyplot as plt
import wave 
from scipy.io import wavfile



def main():
    fs, signal = wavfile.read('trumpet_mono.wav')
    
    MAX_X =1000
    MAX_Y =1000
    
    c = 344
    Ear_Width = 0.24
    
    human_x = 0
    human_y = 0
    
    ear_left_pos_x = human_x - Ear_Width/2
    ear_left_pos_y = human_y
    
    ear_right_pos_x = human_x + Ear_Width/2
    ear_right_pos_y = human_y
    
    sound_x = 52
    sound_y = 43
    
    l1 = math.sqrt( ((ear_left_pos_x-sound_x)**2)+((ear_left_pos_y-sound_y)**2))
    l2 = math.sqrt( ((ear_right_pos_x-sound_x)**2)+((ear_right_pos_y-sound_y)**2))
    
    T1 = l1/c
    T2 = l2/c

    
    t1_index = round(fs*T1)
    t2_index = round(fs*T2)
    N = len(signal)
 
    
    output_l = [0] * (len(signal) + t1_index)
    output_r = [0] * (len(signal) + t2_index)

    for index, value in enumerate(signal):
        output_l[index + t1_index] = value / l1

    for index, value in enumerate(signal):
        output_r[index + t2_index] = value / l2
        
        
    print(len(output_l))
    print(len(output_r))
    #wyrownujemy lewy i prawy sygnal
    if(len(output_r) > len(output_l)): 
        output_l = output_l + [0] * (len(output_r) - len(output_l))
    else:
        output_r = output_r + [0] * (len(output_l) - len(output_r))
    
   
 #SECOND SOUND
    fs2, signal2 = wavfile.read('water.wav')
    sound_x = -23
    sound_y = 24
    
    l1 = math.sqrt( ((ear_left_pos_x-sound_x)**2)+((ear_left_pos_y-sound_y)**2))
    l2 = math.sqrt( ((ear_right_pos_x-sound_x)**2)+((ear_right_pos_y-sound_y)**2))
    
    T1 = l1/c
    T2 = l2/c

    
    t1_index = round(fs2*T1)
    t2_index = round(fs2*T2)
    
  
    output2_l = [0] * (len(signal2) + t1_index)
    output2_r = [0] * (len(signal2) + t2_index)

    for index, value in enumerate(signal2):
        output2_l[index + t1_index] = value / l1

    for index, value in enumerate(signal2):
        output2_r[index + t2_index] = value / l2
    
    #wyrownujemy lewy i prawy sygnal
    
    print(len(output2_l))
    print(len(output2_r))
    
    if(len(output2_r) > len(output2_l)): 
        output2_l = output2_l + [0] * (len(output2_r) - len(output2_l))
    else:
        output2_r = output2_r + [0] * (len(output2_l) - len(output2_r))
    
    
    final_output_l =[]
    final_output_r =[]
    
    
    #dodajemy sygnaly, sygnal 1 jest krotszy od drugiego
    
    for i in range(0, len(output_l)):
        final_output_l.append(output_l[i] + output2_l[i])
        final_output_r.append(output_r[i] + output2_r[i])

        
    for i in range(len(output_l),len(output2_l)):
        final_output_l.append(output2_l[i])
        final_output_r.append(output2_r[i])
    
    #zapisujemy sygnaly
    
    write_data = np.array([final_output_l, final_output_r]).T
    write_data = np.array(write_data, dtype=np.int16)
    wavfile.write('stereo.wav', fs, write_data)


if __name__ == '__main__':
    main()