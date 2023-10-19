# sourcery skip: use-fstring-for-concatenation
# sourcery skip: use-fstring-for-concatenation
import os
import re
import argparse
import json
import datetime
import sys
from colorama import init,Fore

current_datetime = datetime.datetime.now()

# The code `windows = os.name == 'nt'` is checking if the operating system is Windows. It assigns `True` to the variable
# `windows` if the operating system is Windows, and `False` otherwise.
windows = os.name == 'nt'
init(convert=windows, autoreset=True)

if len(sys.argv) == 1:
    print(f"usage: python {os.path.basename(sys.argv[0])} [options]\nAdd -h to get help")
    sys.exit()

#Colors
RED = Fore.RED
BLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

_OK = GREEN+'[OK]'+RESET
_ERR = RED+'[ERR]'+RESET
_INFO = YELLOW+'[INFO]'+RESET

version_rurser = '1.3'

# Format the date and time as "DD-MM HH:MM:SS"
time = current_datetime.strftime("%Y-%d-%m %H:%M:%S")

time_writing = current_datetime.strftime("%d_%m_%H-%M-%S")

fold_outputs = 'parses'

banner = f"""
{'-'*20}
 _____ _____ _____ _____ _____ _____    _____ _____ _____ _____ _____ _____
| __  |  |  | __  |   __|   __| __  |  |  _  |  _  | __  |   __|   __| __  |
|    -|  |  |    -|__   |   __|    -|  |   __|     |    -|__   |   __|    -|
|__|__|_____|__|__|_____|_____|__|__|  |__|  |__|__|__|__|_____|_____|__|__|

"""

description = """
Rurser - Python tool for parsing RedLine logs
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument('-f', '--folder', action='store', help="folder for parsing logs")
parser.add_argument('-j', '--json', action='store', help="JSON file with sites for searching<br>*P.S. In file must be \'sites\':[...] for correct work*")

args = parser.parse_args()

log_folder = '.' if args.folder in ["", "."] else args.folder
if not os.path.exists(log_folder):
    print(f"{_ERR} Folder {log_folder} not found in current directory!")
    sys.exit()

if not os.path.exists(fold_outputs):
    os.makedirs(fold_outputs) # Creating folder

output_file = f'{fold_outputs}/output{time_writing}.txt'

# Sites list
sites = None
sites_file = 'sites.json'

if not os.path.exists(sites_file):
    print(f'{_ERR} File sites.json not found, creating...')
    str_to_json = {
        "sites": [

        ]
    }
    with open('sites.json', 'w', encoding='utf-8') as json_file:
        json.dump(str_to_json, json_file, sort_keys=True, indent=2)
        json_file.close()
    print(f'{_OK} sites.json was created')
    sys.exit()

with open('sites.json', 'r') as sites_json:
    sites = json.loads(sites_json.read())['sites']
    sites_json.close()

# Regular pattern
pattern = r'URL: (https://[^\n]+)\nUsername: ([^\n]+)\nPassword: ([^\n]+)'

folder_time_name = f"{fold_outputs}/{fold_outputs}{time_writing}" # Folder to writing parses

if not os.path.exists(folder_time_name):
    os.makedirs(folder_time_name) # Creating folder

# File descriptors
file_handles = {}

# Main parsing cycle
#################################################################################################
# Banner wrote or not
banner_written = {}

for folder_name in os.listdir(log_folder):
    folder_path = os.path.join(log_folder, folder_name)

    if os.path.isdir(folder_path) and len(folder_name) >= 2 and folder_name[:2].isalpha():
        country = folder_name[:2] # Country

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if file_name == "Passwords.txt":
                    log_path = os.path.join(root, file_name)

                    with open(log_path, 'r', encoding='utf-8') as log_file:
                        log_data = log_file.read()
                        matches = re.finditer(pattern, log_data) #Finding matches in log file

                        for match in matches:
                            url = match.group(1)
                            username = match.group(2)
                            password = match.group(3)

                            for site in sites:
                                print(YELLOW+f"Checking for site {site}...")
                                if site in url:
                                    print(GREEN+f"{site} found!")

                                    # Checking if banner wrote to file
                                    if site not in banner_written:
                                        banner_written[site] = True
                                        # Opening site with site's name
                                        dot_index = site.find('.')
                                        if dot_index != -1:
                                            site = site[:dot_index]

                                            with open(f"{folder_time_name}/{site.upper()}.txt", "a", encoding='utf-8') as output_f:
                                                output_f.write(f"{banner}\nRURSER PARSER v{version_rurser}\nTime: {time}\n")
                                                output_f.write(f"Format: \n{' '*5}URL: (URL) [username:password]\n")

                                    else:
                                        # Opening file without writing banner
                                        dot_index = site.find('.')

                                        if dot_index != -1:
                                            site = site[:dot_index]
                                        output_f = open(
                                            f"{folder_time_name}/{site.upper()}.txt",
                                            "a",
                                            encoding='utf-8',
                                        )

                                    # Write data to file
                                    output_f.write(f"URL: {url} [{username}:{password}]\n")
                                    output_f.write(f"Country: {country}\n")
                                    output_f.write("=" * 40 + "\n")

                                    output_f.close()
                                    break

#################################################################################################

# Closing all files descriptors
for handle in file_handles.values():
    handle.close()

print(f"{_OK} Logs from folder successfully parsed")

input(YELLOW+"Press Enter to exit...")
