from git import Repo, Git
import requests
import json
import shutil
import argparse


def get_repos(github_username: str) -> list:
    url = "https://api.github.com/users/{}/repos".format(github_username)
    response = requests.get(url)
    repos = json.loads(response.text)
    for repo in repos:
        yield repo["ssh_url"]


def get_repo_commits(repo_url: str) -> list:
    folder_name = f"./tmp/{repo_url.split('/')[-1]}"
    print(f"Cloning repo: {folder_name}")
    try:
        repo = Repo.clone_from(repo_url, folder_name, bare=True)
        g = Git(folder_name)
    except Exception:
        print(f"Error cloning: {repo_url}")
        return
    return list(repo.iter_commits())


def get_commit_emails(commits) -> list:
    emails = []
    for commit in commits:
        if "noreply" not in commit.author.email:
            emails.append(commit.author.email)

    if emails is None:
        return

    emails = list(set(emails))
    print(f"Found emails: {emails}")
    return emails


if __name__ == "__main__":
    print(
        """


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
    """
    )

    shutil.rmtree("./tmp/", ignore_errors=True)

    found_emails = []
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", help="Scan an entire account")
    parser.add_argument("-r", "--repo", help="Scan a single repo")
    parser.add_argument("-o", "--output", help="Output file")

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit(0)

    if args.account is None and args.repo is None:
        parser.print_help()
        exit(0)

    if args.account:
        print(f"Scanning account: {args.account}")
        repos = get_repos(args.account)
        for repo in repos:
            try:
                commits = get_repo_commits(repo)
                emails = get_commit_emails(commits)
                found_emails.extend(emails)
            except Exception:
                print(f"Error scanning: {repo}")
                continue

    if args.repo:
        print(f"Scanning repo: {args.repo}")
        try:
            commits = get_repo_commits(repo)
            emails = get_commit_emails(commits)
            found_emails.extend(emails)
        except Exception:
            print(f"Error scanning: {repo}")

    found_emails = list(set(found_emails))

    if args.output:
        with open(args.output, "w") as f:
            for email in found_emails:
                f.write(email + "\n")

    print("Total found emails:")
    print(found_emails)

    print("Cleaning up")
    shutil.rmtree("./tmp/", ignore_errors=True)
