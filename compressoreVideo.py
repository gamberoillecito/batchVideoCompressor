import subprocess
import os
import sys
import argparse
import re


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", help="Path to the folder containing the videos to compress")
    parser.add_argument("-d", "--destination", 
				help="The folder where to put the compressed videos. (Equals to path by default)")
    args = parser.parse_args()

    if os.path.isdir(args.path):
            compress(args.path, args.destination)
    else:
        printError("Unknown error")
    
   
def compress(folder, destination):
    
    if destination != None:
        try:
            subprocess.run('mkdir "%s"' %(folder + '\\' + destination), check=True, shell=True)
        except subprocess.CalledProcessError:
            if len(os.listdir(folder + '\\' + destination) ) != 0:
                sys.exit(1)
        except:
            print('Errorre')
            sys.exit(1)
    else:
        destination = ''
    for root, dirs, files in os.walk(folder, topdown=True):
        for filename in files:
            if os.path.isfile(folder + '\\' + filename):
                diviso = re.split("([\d\w_?\-. \(\)]+).(..[\d\w]+)", filename)
                nuovoNome = folder + '\\' + destination + '\\'
                nuovoNome += diviso[1]
                est = diviso[2]
                nuovoNome += '_c.'
                nuovoNome += est
                # subprocess.run('cp "%s" "%s"' %(folder + '\\' + filename, nuovoNome), check=True)
                try:
                    subprocess.run('ffmpeg -i "%s" -vf scale=-1:720 -c:v libx264 -crf 18 -preset slow  -c:a copy "%s"' %(folder + '\\' + filename, nuovoNome), check=True, shell=True)
                except subprocess.CalledProcessError:
                    sys.exit(1)
            
   
   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)