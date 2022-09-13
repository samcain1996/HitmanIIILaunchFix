# HitmanIIILaunchFix

## Description

For some reason, on some systems, Hitman III will not boot on Windows past the launcher when its AppData 
directory has files in it. This script empties that directory and then launches the Hitman III launcher.

**THIS ONLY WORKS ON WINDOWS**

## Requirements
- Python 3
- Hitman III

## How to Use

1. Download FixAndLaunch.py

2. Get the locations of the Hitman III launcher directory and its AppData directory.
   If you do not know where the AppData directory for Hitman III is it is likely: *Drive*:\Users\*User Name*\AppData\Local\IO Interactive\HITMAN3

3. In the directory you downloaded FixAndLaunch.py to, run the following command:
   ```
   python FixAndLaunch.py HitmanIII_AppData_directory_path HitmanIII_launcher_path
   ```

   or

   Run: `python FixAndLaunch.py` and then enter the directory paths in the HitmanIIIFix.conf file that it creates in the same directory

4. After the first time it successfully runs, arguments are no longer needed unless the directory paths change
   ```
   python FixAndLaunch.py
   ```
