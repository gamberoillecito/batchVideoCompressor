# batchVideoCompressor

A simple python script to compress all the videos in a folder using ffmpeg.

-----------
## How to use ##

Run the .py or .exe files specifying the `path` to the folder containing the videos you want to compress and, if you want, the name of the `destination` folder (which will be created **inside** of `path`); if you want you can instead specify an **absolute path** where to put the compressed wideos with the option `-ad`; if you don't specify anything the videos will be put into `path`.


Example:
If the folder with you videos is called "folder-with-videos" and has the following structure:

```
.
└───folder-with-videos
        v1.mkv
        v2.mkv
        v3.mkv
```
------------------

Using `python3 batchVideoCompressor.py "folder-with-videos" -d "compressed-videos"`

The result will be:
```
.
└───folder-with-videos
    │   v1.mkv
    │   v2.mkv
    │   v3.mkv
    │
    └───compressed-videos
            v1_c.mkv
            v2_c.mkv
            v3_c.mkv
```
------------------
Using `python3 batchVideoCompressor.py "folder-with-videos" -ad "C:\compressed-videos"`

The result will be:
```
.
└───folder-with-videos
        v1.mkv
        v2.mkv
        v3.mkv
C:
└───compressed-videos
        v1_c.mkv
        v2_c.mkv
        v3_c.mkv
```

------------------

Using `python3 batchVideoCompressor.py "folder-with-videos" -ad "C:\compressed-videos"`

The result will be:
```
.
└───folder-with-videos
        v1.mkv
        v1_c.mkv
        v2.mkv
        v2_c.mkv
        v3.mkv
        v3_c.mkv
```
