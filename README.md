<img src="./src/img/rurser.ico" width="150" height="150">

# Rurser

![Version](https://img.shields.io/badge/version-1.0-ffffff?label=Version)
[![Github](https://img.shields.io/badge/Github-gray)](https://github.com/TechAngle)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MIT](https://img.shields.io/badge/License-MIT-blue.svg)

### Introduction

Rurser is an open-source tool that parses log files from Redline log sources.
### Features

- Parse logs from RedLine
- Create a folder with parsed data
- Save the parsed data in a txt file with kind formatting

## Installation

### Using zip with binary:
Run file **run_parsing.bat** and enter folder with Logs.

##### EXAMPLE OF LOGS DIRECTORIES
>*(logs directory)*:\
 -***UA**TETSDF#GS#3...*,\
 -***CZ**DY4HF3S#...*\
 -***RU**UIFSH%3F...*\
>  *Bold letters its country that will in end of datas*\

Then program create a folder "*parses*" that contains folders with parsed data in format:\
 ***URL: (url) [**username**:**password**]***

### Use original binary file to run:
**!BEFORE THIS, YOU MUST ADD RURSER TO *SYSTEM PATH***
1. Open ***your terminal*** and write:\
&emsp;**``
rurser -f <folder> -s <json file>
​``**\

2. Wait while program parse folder
3. Open `parses` folder and choise required parse
4. DONE!

#### If you use source code:
1. You must have Python >= 3.10
2. Install requirements with:

Linux:
>apt-get update && apt-get upgrade\
apt-get install pip3\
pip3 install -r requirements.txt

Windows:
>pip install -r requirements.txt
3. Run in your terminal:\
    `​rurser.py -f <folder> -j <json file>`
4. If there aren't `sites.json` script will create it
5. Your file will saved in folder `parses/parses(current date)`

## Author
### TechAngle
#### &emsp; [**Github**](https://github.com/TechAngle)
#### &emsp; [**Telegram**](https://telegram.me/rect4ngle)
#### &emsp; [**Contact me**](mailto:rect4ngle@programmer.net)

## License
This project is licensed under the **MIT** license
