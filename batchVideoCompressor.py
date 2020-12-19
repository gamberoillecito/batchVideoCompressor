import subprocess
import os
import sys
import argparse
import re
import shutil

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", help="Path to the folder containing the videos to compress")
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument("-d", "--destination",
				help="The NAME of the folder where to put the compressed videos.(Equals to path by default)")
    destination.add_argument("-ad", "--absoluteDestination",
				help="The PATH of the folder where to put the compressed videos.")
    args = parser.parse_args()

    # edit the destination format
    if args.destination != None:
        dest = args.path + '\\' +  args.destination
    elif args.absoluteDestination != None:
        dest = args.absoluteDestination
    else:
        dest = args.path


    if os.path.isdir(args.path):
            compress(args.path, dest)
            # print(dest)
    else:
        printError("Unknown error")

def checkExt(s):
    supportedExt = [".mkv", ".mp4", ".avi", ".mov", ".wvm"]

    for e in supportedExt:
    	if s.endswith(e):
    		return True
    return False

def compress(folder, destination):

    if destination == folder:
        destination = folder + "\\temp"
        moveFromTemp = True

    try:
        subprocess.run('mkdir "%s"' %(destination), check=True, shell=True)
    except subprocess.CalledProcessError:
        try:
            if len(os.listdir(destination) ) != 0:
                sys.exit(1)
        except OSError:
            sys.exit(1)
    except:
        print('Errorre')
        sys.exit(1)

    for root, dirs, files in os.walk(folder, topdown=True):
        for filename in files:
            if not checkExt(filename):
                continue
            if os.path.isfile(folder + '\\' + filename):
                diviso = re.split("([\d\w_?\-. \(\)#]+).(..[\d\w]+)", filename)
                nuovoNome = destination + '\\'
                nuovoNome += diviso[1]
                est = diviso[2]
                nuovoNome += '_c.'
                nuovoNome += est
                # subprocess.run('cp "%s" "%s"' %(folder + '\\' + filename, nuovoNome), check=True)
                try:
                    subprocess.run('ffmpeg -i "%s" -vf scale=-1:720 -c:v libx264 -crf 18 -preset slow  -c:a copy "%s"' %(folder + '\\' + filename, nuovoNome), check=True, shell=True)
                except subprocess.CalledProcessError:
                    sys.exit(1)
                except:
                    pass

    # move the files from temp to folder and remove temp
    if moveFromTemp:
        for root, dirs, files in os.walk(destination, topdown=True):
            for filename in files:
                shutil.move(destination + '\\' + filename, folder + '\\' + filename)
        os.rmdir(destination)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
