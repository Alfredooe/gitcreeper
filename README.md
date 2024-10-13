
# Gitcreeper

OSINT Tool automating scraping emails from user commits. For contacting maintainers, nothing else.


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Features
Requires Python 3.6+
- -a Scrape Account
- -r Scrape Repo
- -o Save To File


## Usage

### Docker

```javascript
docker run --rm -t -v ./output:/app/output ghcr.io/Alfredooe/gitcreeper -a username -o /app/output/emails.txt

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

Alternatively, if you don't need the emails to be saved to a file, you can just run: `docker run --rm -t ghcr.io/Alfredooe/gitcreeper -a username`

### From local clone

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

