
# Gitcreeper

OSINT Tool automating scraping emails from user commits. For contacting maintainers, nothing else.


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Features
Requires Python 3.6+
- -a Scrape Account
- -r Scrape Repo
- -o Save To File


## Usage

```javascript
python3 gitcreeper.py -a username -o output.txt

  ▄████  ██▓▄▄▄█████▓ ▄████▄   ██▀███  ▓█████ ▓█████  ██▓███  ▓█████  ██▀███  
 ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▒▓█    ▄ ▓██ ░▄█ ▒▒███   ▒███   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██░░ ▓██▓ ░ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██░  ▒██▒ ░ ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒░▒████▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▓    ▒ ░░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░  ▒ ░    ░      ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ▒ ░  ░      ░          ░░   ░    ░      ░   ░░          ░     ░░   ░ 
      ░  ░           ░ ░         ░        ░  ░   ░  ░            ░  ░   ░     
                     ░                                                                                              
OSINT Tool to scrape emails from Github commits by @Alfredo
    
Scanning account: username
Cloning repo: ./tmp/repo
Found emails: ['email', 'email','email', 'email','email', 'email']
Cloning repo: ./tmp/repo
Found emails: ['email', 'email','email', 'email','email', 'email']
Total found emails:
['email']
```

