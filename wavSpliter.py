#                               Wav Splitter Class

#                    This script contains a class that splits wav
#           audio files up.


#IMPORTS
from pydub import AudioSegment
import math, os

#It will be assummed that the filepaths contain the location and
#the specific file reference in a string

class AudioSplitter(object):
    """Splits wav files up."""

    def __init__(self, original_filepath):
        """Initialize the object."""

        self.original_filepath = original_filepath
        self.audio = AudioSegment.from_wav(self.original_filepath)


    @property
    def getAudio_duration(self):
        """Get the duration of the wav file in seconds."""

        return self.audio.duration_seconds


    def single_split(self,from_min,to_min,split_filepath):
        """Split the file one time."""

        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(split_filepath,format="wav")


    def multiple_split(self, min_per_split,split_folderpath,common_filename):

        total_mins = math.ceil(self.getAudio_duration / 60)

        for i in range(0, total_mins, min_per_split):

            split_fn = str(i) + "_" + common_filename
            common_filepath = os.path.join(split_folderpath, split_fn)
            self.single_split(i, i + min_per_split, common_filepath)

            print(str(i) + " Done")

            if i == total_mins - min_per_split:
                print("All splited successfully.")


def main():
    """Run this function if script is run directly."""

    print("Do not run this script directly")


if __name__ == "__main__":
    main()
        
