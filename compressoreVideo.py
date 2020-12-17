import subprocess
import os
import sys
import argparse
import re

# comprime tutti i video nella cartella passata come primo parametro
def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("percorso", help="Specifica il percorso ai video da comprimere")
    parser.add_argument("-d", "--destination", 
				help="La cartella dove mettere i video compressi")
    args = parser.parse_args()

    if os.path.isdir(args.percorso):
            comprimi(args.percorso, args.destination)
    else:
        printError("Il percorso non e' una cartella")
    
   
def comprimi(cartella, destinazione):
    if destinazione != None:
        try:
            subprocess.run('mkdir "%s"' %(cartella + '\\' + destinazione), check=True)
        except subprocess.CalledProcessError:
            sys.exit(1)
        except:
            print('Errorre')
            sys.exit(1)
    else:
        destinazione = ''
    for root, dirs, files in os.walk(cartella, topdown=True):
        for filename in files:
            if os.path.isfile(cartella + '\\' + filename):
                diviso = re.split("([\d\w_?\-. \(\)]+).(..[\d\w]+)", filename)
                nuovoNome = cartella + '\\' + destinazione + '\\'
                nuovoNome += diviso[1]
                est = diviso[2]
                nuovoNome += '_c.'
                nuovoNome += est
                # subprocess.run('cp "%s" "%s"' %(cartella + '\\' + filename, nuovoNome), check=True)
                subprocess.run('ffmpeg -i "%s" -vf scale=-1:720 -c:v libx264 -crf 18 -preset slow  -c:a copy "%s"' %(cartella + '\\' + filename, nuovoNome), check=True)
            
            
   
   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)