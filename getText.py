
#IMPORTS
import os, math, shutil, sys
import speech_recognition as sr
from wavSpliter import AudioSplitter

#GLOBAL CONSTANTS
SPEECH_RECOGNIZER = sr.Recognizer() #It should be global
ORIGINAL_AUDIO_FOLDER = "wav_audio"
AUDIO_CHUNKS_FOLDER = "audio_chunks"
TRANSCRIPTS_FOLDER = "extracted_transcripts"

#The programme gets as a command line argument one of the audio files to
#work with, All audio files must be in the folder "original_audio"
#DO NOT SPECIFY THE FOLDER IN THE COMMAND LINE ARGUMENT

def main():
  """Makes the whole programme work."""

  #Check that the input is appropiate
  if not check_audioFilename(ORIGINAL_AUDIO_FOLDER):
    print("Inappropiate input.")
    return

  #Store the complete name of the audio filename
  complete_audioFilename = os.path.join(ORIGINAL_AUDIO_FOLDER,
                                        sys.argv[1])
  #Clear the audio chunks folder
  delete_folderContent(AUDIO_CHUNKS_FOLDER)

  #Split the original audio file in chunks of 1 minute each and
  #save them in the chunk folder

  split_audioFile(complete_audioFilename,
                  1,
                  AUDIO_CHUNKS_FOLDER,
                  sys.argv[1][:-4] + ".wav")

  #Get the transcript out of each chunk
  total_transcriptContent = []
  unordered_chunk_names = []

  for chunk_name in os.listdir(AUDIO_CHUNKS_FOLDER):
    unordered_chunk_names.append(chunk_name)

  ordered_chunk_names = order_chunkNames(unordered_chunk_names)

  for chunk_name in ordered_chunk_names:
    complete_chunkName = os.path.join(AUDIO_CHUNKS_FOLDER,chunk_name)
    
    try:
      chunk_transcriptContent = extract_transcriptContent(complete_chunkName)
      total_transcriptContent.append("\n\n" + chunk_transcriptContent + "\n\n")

    except:
      print(f"An error happened when interpreting the chunk " \
            + f"{complete_chunkName}.\nContinuing to the next one.")
      
      continue

  #Write all the content in a word document
  transcript_filename = os.path.join(TRANSCRIPTS_FOLDER,sys.argv[1][:-4])
  write_transcript(total_transcriptContent,transcript_filename)
    

def order_chunkNames(chunk_namesList):
  """Return an ordered list for chunk names."""

  final_list = [] #Final list to be returned
  
  #Create a dictionary that relates "chuck_number" and "chunk_name
  chunks_nums_n_names = dict()

  for chunk_name in chunk_namesList:
    #Find the serial number of each chunk
    chunk_number = int(chunk_name[:chunk_name.find("_")])
    chunks_nums_n_names.update({chunk_number : chunk_name})

  #Append the chunk names to the final list the with the sorted dictionary
  for chunk_num in sorted(chunks_nums_n_names):
    final_list.append(chunks_nums_n_names[chunk_num])

  #Return the listed of ordered chunk names
  return final_list

    
def delete_folderContent(folder_to_clear):
  """Deletes all the content of a folder."""

  for item in os.listdir(folder_to_clear):

    complete_itemName = os.path.join(folder_to_clear,item)

    try:
      os.remove(complete_itemName)

    except PermissionError:
      shutil.rmtree(complete_itemName) #Dealing with folders


  print(f"\nThe folder {folder_to_clear} was cleared successfully.")
      

def extract_transcriptContent(audio_filename):
  """Returns the text from an audio file."""

  audio_file = sr.AudioFile(audio_filename)

  with audio_file as source:
    transcript_record = SPEECH_RECOGNIZER.record(source) 
    return SPEECH_RECOGNIZER.recognize_google(transcript_record)

  print(f"\nTranscript of {audio_filename} was got successfully.")


def split_audioFile(audio_filepath,
                    min_per_split,
                    chunks_location,
                    chunk_common_filename):
  """Split the original audio file in multiple audio files."""

  splitter = AudioSplitter(audio_filepath)
  splitter.multiple_split(min_per_split,
                           chunks_location,
                           chunk_common_filename)  


def check_audioFilename(files_container):
  """Checks that the audio filename is valid."""

  #If the length of the command line arguments is different from zero return False

  if len(sys.argv) != 2:
    return False

  #Check all the files present in the folder "files_container"
  for filename in os.listdir(files_container):

    if filename == sys.argv[1]: #The second command line argument is a file that belongs to the folder
      return True

  return False


def write_transcript(transcript_content,audio_filename):
  """Writes the transcript of an audio file in a specific folder."""

  with open(audio_filename + ".docx","w") as transcript_file:
    transcript_file.writelines(transcript_content)

  print(f"\nThe transcript was written successfully.")

if __name__ == "__main__":
    main()
