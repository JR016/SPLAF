Speech Recognition for Large Audio Files

This programming project uses the terminal window to run.

WARNINGS:

DO NOT DELETE OR RENAME ANY OF THE FOLDERS OR PYTHON FILES OF THIS PROJECT, AS THEY ARE ESSENTIAL FOR THE WORKINGS OF THIS PROJECT.

THIS PROJECT MIGHT NOT WORK FOR WAV FILES THAT ARE SHORTER THAN 1 MIN.

DO NOT WIRTE THE NAME OF THE FOLDER IN WHICH THE AUDIO FILES YOU WANT TO WORK ON ARE PLACED, THE PROGRAMME HAS A WAY TO DEAL WITH IT.

THIS PROJECT IS NOT ACCURATE, SO IT WILL MAKE MISTAKES.

The terminal must be placed at the folder location of the project.

If it's your first time using this project, please run the "run_first.py" file first, it will install all the required modules for audio handling and
Speech Recognition and also vital folders that the project needs to work.

There are two python files that are run through the terminal and need command line arguments to work properly, otherwise they will return "Inappropiate Input."

The first one is "mp3_to_wav.py". This python files converts mp3 audio files to wav audio files placed on the "mp3_audio" folder.
To run this file, execute the command "python mp3_to_wav.py some_audio.mp3" being "some_audio.mp3" a mp3 file placed in the "mp3_audio" folder.

The second one is "getText.py" gets the speech content from wav files from the "original_audio" folder and creates a Microsoft Word document as a transcript in the "extracted_transcripts" folder.
To run this file, execute the command "python getText.py some_audio.wav" being "some_audio.wav" a wav file placed in the "original_audio" folder.
The transcript of that file will appear in the "extracted_transcripts" folder.

The "getText.py" file uses a splitter object from the "wavSpliter.py" file, it splits wav files in chunks of 1 minute each that are placed in the "audio_chunks" folder.

Each time you run the file "getText.py" and associate the name of a wav file to it, the program clears the "audio_chunks" folder. So, there is no need for doing that yourself.

