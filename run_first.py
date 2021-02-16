#               File to run first before using this programming project
#               Installs the required modules if they are not present
#               And also sets up the required folders for everything to work properly

#IMPORTS
import os, subprocess, importlib, pip

#GLOBAL CONSTANTS

FOLDER_NAMES =("audio_chunks",
               "extracted_transcripts",
               "mp3_audio",
               "wav_audio"
               )

MODULES_NAMES = ("SpeechRecognition",
                 "pydub")


def main(): 
    """Run the whole programme."""

    print("\t\t\t\nTHE RUN FIRST SCRIPT")
    print("\nRun me to install required modules or folders for this project.")
    print("Let's see how it all goes....")

    try:
        install_modules()
        create_folders()

    except Exception as e:
        print("\nSorry, some strange error happened.")
        print(f"According to python, the error is: {e}")
        print("\nGood luck troubleshooting it. :)")

    else:
        print("\n\nEverything went well, enjoy this project.")
        print(":)")

    input("\n\nPress the enter key to exit.")
    

def install_modules():
    """Installs required modules for AI Speech Recognition."""

    #Try to import the required modules, if a failure happens
    #Then install them

    for module in MODULES_NAMES:

        try:
            importlib.import_module(module)

        except ImportError:
            pip.main(["install", module])

    

def create_folders():
    """Creates the required folders for the project."""

    for foldername in FOLDER_NAMES:

        #Check if the folder exists in the project location
        #If not create it
        if not os.path.isdir(foldername):
            os.mkdir(foldername)
            print(f"\nA new folder of name\"{foldername}\" has been created in this location.")
            

        else:
            print(f"\nThe folder \"{foldername}\" already exists in this location.")
            

if __name__ == "__main__": 
    main()
