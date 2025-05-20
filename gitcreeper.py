from git import Repo, Git
import requests
import json
import shutil
import argparse
import Levenshtein


def get_repos(github_username: str) -> list:
    url = "https://api.github.com/users/{}/repos".format(github_username)
    response = requests.get(url)
    repos = json.loads(response.text)
    for repo in repos:
        yield repo["clone_url"]


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


def is_email_similar(email_prefix, username, threshold=2):
    """
    Checks if an email prefix is similar to a username based on Levenshtein distance.
    """
    distance = Levenshtein.distance(email_prefix, username)
    return distance <= threshold


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
    similar_emails_by_username = {}  # Changed from similar_emails = []
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", help="Scan an entire account")
    parser.add_argument("-r", "--repo", help="Scan a single repo")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument(
        "--similar-to",
        nargs="+",
        dest="similar_to_usernames",
        help="One or more usernames to check for similar email addresses.",
    )

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
            commits = get_repo_commits(args.repo)
            emails = get_commit_emails(commits)
            found_emails.extend(emails)
        except Exception:
            print(f"Error scanning: {args.repo}")

    found_emails = list(set(found_emails))

    if args.similar_to_usernames and found_emails: # args.similar_to_usernames is now a list
        # Initialize dictionary keys for each target username
        for target_username_init in args.similar_to_usernames:
            if target_username_init not in similar_emails_by_username:
                similar_emails_by_username[target_username_init] = []

        print(f"\nChecking for emails similar to: {', '.join(args.similar_to_usernames)}...")
        
        for target_username in args.similar_to_usernames:
            current_similar_list = []
            for email in found_emails:
                email_prefix = email.split('@')[0]
                # Make sure is_email_similar is called correctly
                if is_email_similar(email_prefix, target_username): 
                    current_similar_list.append(email)
            
            # Ensure uniqueness and store
            if current_similar_list:
                similar_emails_by_username[target_username].extend(current_similar_list)
                # Make emails unique for this specific username
                similar_emails_by_username[target_username] = sorted(list(set(similar_emails_by_username[target_username])))

    # Old similar_emails list is effectively replaced by similar_emails_by_username dictionary
    # The output logic below will be updated in a subsequent step to use similar_emails_by_username

    if args.output:
        with open(args.output, "w") as f:
            for email in found_emails:
                f.write(email + "\n")
        # Updated file output logic for similar_emails_by_username
        if args.similar_to_usernames:
            with open(args.output, "a") as f:
                for username in args.similar_to_usernames:
                    if username in similar_emails_by_username and similar_emails_by_username[username]:
                        f.write("\n---\n")
                        f.write(f"Emails similar to '{username}':\n")
                        for email in similar_emails_by_username[username]:
                            f.write(email + "\n")

    print("Total found emails:")
    print(found_emails)

    # Updated console output logic for similar_emails_by_username
    if args.similar_to_usernames:
        for username in args.similar_to_usernames:
            if username in similar_emails_by_username and similar_emails_by_username[username]:
                print(f"\nEmails similar to '{username}':")
                print(similar_emails_by_username[username])

    print("Cleaning up")
    shutil.rmtree("./tmp/", ignore_errors=True)
