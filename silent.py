import os
import numpy as np
import soundfile as sf

def is_silent(audio_file, threshold=0.001):
    data, _ = sf.read(audio_file)
    rms = np.sqrt(np.mean(data ** 2))
    return rms < threshold

def delete_silent_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            filepath = os.path.join(folder, filename)
            if is_silent(filepath):
                os.remove(filepath)
                print(f"Deleted {filepath}")

# Replace 'path_to_folder' with the path to the folder containing the audio files
delete_silent_files(r"C:\Users\mausu\Downloads\Birds_sounds\Crow")
