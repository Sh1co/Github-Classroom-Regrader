import argparse
import subprocess
import os
import shutil


def run_command(command, cwd=None, capture_output=False):
    try:
        result = subprocess.run(
            command,
            check=True,
            shell=True,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return result.stdout if capture_output else None
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None


def copy_template_to_repo(template_path, repo_path):
    if not os.path.exists(template_path):
        print("Template folder does not exist.")
        return

    for item in os.listdir(template_path):
        source = os.path.join(template_path, item)
        destination = os.path.join(repo_path, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)


def commit_changes(repo):
    run_command("git add -A")
    run_command(f'git commit --allow-empty -m "Grading update for {repo}"')


def main(assignment_number):
    new_folder = "cloned_repos"
    template_folder = "template"
    os.makedirs(new_folder, exist_ok=True)

    clone_command = f"gh classroom clone student-repos -a {assignment_number}"
    run_command(clone_command, cwd=new_folder)

    try:
        first_repo_folder = next(
            os.path.join(new_folder, d)
            for d in os.listdir(new_folder)
            if os.path.isdir(os.path.join(new_folder, d))
        )
    except StopIteration:
        print("No directories found in the cloned repositories folder.")
        return

    for repo in os.listdir(first_repo_folder):
        repo_path = os.path.join(first_repo_folder, repo)
        if os.path.isdir(repo_path):
            print(f"Updating {repo}")
            copy_template_to_repo(template_folder, repo_path)
            os.chdir(repo_path)
            commit_changes(repo)
            print(f"Pushing the update for {repo}")
            run_command("git push origin")
            os.chdir("../../..")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Clone GitHub Classroom repositories, update with template, commit changes, and push."
    )
    parser.add_argument(
        "assignment_number", type=str, help="The assignment number for GitHub Classroom"
    )

    args = parser.parse_args()
    main(args.assignment_number)
