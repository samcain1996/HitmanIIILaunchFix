# Hitman 3 Fix And Launch Game

## Description

For some reason, on some systems, Hitman 3 will not boot on Windows past the executable when its AppData 
directory has files in it. This script empties that directory and then launches the Hitman 3 executable.

## How to Fix Manually

Before launching the game, navigate to Hitman 3's AppData folder and delete everything in it.

**THIS ONLY WORKS ON WINDOWS**

## Requirements
- Python 3
- Hitman 3

## How to Use

1. Download FixAndLaunch.py

2. Get the locations of the Hitman 3 executable directory and its AppData directory.
   If you do not know where the AppData directory for Hitman 3 is it is likely: *Drive*:\Users\*User Name*\AppData\Local\IO Interactive\HITMAN3

3. In the directory you downloaded FixAndLaunch.py to, run the following command (type single quotes as they appear below):
   ```
   python FixAndLaunch.py 'Path\To\Hitman3\AppData' 'Path\To\Hitman3\Executable'
   ```

   or

   Run: `python FixAndLaunch.py` and then enter the directory paths in the Hitman3Fix.conf file that it creates in the same directory

4. After the first time it successfully runs, arguments are no longer needed unless the directory paths change
   ```
   python FixAndLaunch.py
   ```
