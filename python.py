import subprocess

def get_latest_commit_message():
    try:
        # Run git command to get the latest commit message
        commit_message = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B"],
            cwd="."
        ).decode("utf-8").strip()
        print("Latest Commit Message:")
        print(commit_message)
    except Exception as e:
        print("Error fetching commit message:", e)

if __name__ == "__feature2__":
    get_latest_commit_message()
