rm batchVideoCompressor.exe
pyinstaller -c --clean --distpath ./ -F batchVideoCompressor.py
rm -d -r build
rm bruteforceStea.spec
