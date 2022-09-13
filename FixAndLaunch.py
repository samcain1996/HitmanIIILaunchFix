"""

For some stupid reason, the Epic Games version of Hitman 3
only launches when PipelineCache.bin and PipelineLibrary.bin
are deleted from the AppData folder. 

This script deletes those files, then launches the game.

"""


import os
import sys


# Extract hitman directories 
def getDirsFromConfigFile():
    config_file = open(config_filepath, 'r')
    config_vars = [ var[var.find('=') + 1:].replace('\n', ' ').strip() for var in config_file.readlines() ]

    if len(config_vars) != 2:
        print('Unexpected number of configuration variables')
        exit()

    return config_vars

# Exit script if directories are not set
def abortIfNoDirs(message=None):
    if len(hitman_stupid_files_dir) == 0 or len(hitman_exe_dir) == 0:
        print(message)
        exit()


config_filepath = os.curdir + '\\' + "Hitman3Fix.conf"

hitman_stupid_files_dir = str()
hitman_exe_dir     = str()

# Did the user supply the folders as arguments?
user_supplied_folders = len(sys.argv) == 3

if user_supplied_folders:
    hitman_stupid_files_dir = sys.argv[1]
    hitman_exe_dir = sys.argv[2]

# Write to or read from config file
if not os.path.exists(config_filepath) or user_supplied_folders:

    # Create config file
    config_file = open(config_filepath, 'w')
    config_file.write('hitman_stupid_files_dir={0}\nhitman_exe_dir={1}'.format(hitman_stupid_files_dir, hitman_exe_dir))
    config_file.close()

    abortIfNoDirs('Folder paths not set in config file, or supplied as arguments')

else:
    hitman_stupid_files_dir, hitman_exe_dir = getDirsFromConfigFile()

    abortIfNoDirs('Folder paths not set! Aborting...')


# Remove files to allow game to launch
for file in os.listdir(hitman_stupid_files_dir):
    os.remove(hitman_stupid_files_dir + '\\' + file)


# Launch game
game_dir = '\"' + hitman_exe_dir + '\\' + 'HITMAN3.exe' + '\"'
os.system(game_dir)