#                               mp3_to_wav script

#           It takes the name of a mp3 audio file from the folder "mp3_audio"
#            As a command line argumment and converts it to a wav audio file
#                 And places it in the original_audio folder


#IMPORTS
import sys, os
from pydub import AudioSegment

#GLOBAL CONSTANTS

MP3_FOLDER = "mp3_audio"
WAV_FOLDER = "original_audio"


def main(): 
    """Make everything work together."""

    #If the input is not appropiate abort operations

    if not check_input():
        print("Inappropiate Input.")
        return

    convert_to_wav(sys.argv[1])
    

def check_input():
    """Checks the programme input is appropiate."""

    #If the length of the input is different from 2 return False
    if len(sys.argv) != 2:
        return False

    else:

        #If the input does not contain the string ".mp3" or
        #Its length is less than 4 return False     
        if ".mp3" not in sys.argv[1] or  len(sys.argv[1]) <= 4:
            return False

        for mp3_filename in os.listdir(MP3_FOLDER):

            #Return True if the input is found in the MP3_FOLDER
            if mp3_filename == sys.argv[1]:
                return True


        #If it is not in the mp3 folder return False
        return False
    

def convert_to_wav(mp3_filename):
    """Converts an mp3 file to a wav file."""

    wav_filename = mp3_filename[:-4] + ".wav"
    complete_mp3FileName = os.path.join(MP3_FOLDER, mp3_filename)
    complete_wavFileName = os.path.join(WAV_FOLDER, wav_filename)

    mp3_file = AudioSegment.from_mp3(complete_mp3FileName)
    mp3_file.export(complete_wavFileName, format="wav")

    print(f"The mp3 file {complete_mp3FileName} was successfully converted to " \
          + f"the wav file {complete_wavFileName}.")



if __name__ == "__main__": 
    main()
