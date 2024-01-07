# Github Classroom Regrader

## Overview

This project contains a Python script designed to automate the updating process of student repositories in GitHub Classroom. The primary goal of this script is to ensure all student repositories have the proper grading files and to send a commit to re-trigger the autograder. This is particularly useful for educators who need to distribute grading updates or trigger autograding across multiple student repositories efficiently.

## Prerequisites

- Python 3.x
- Git and GitHub CLI installed and configured on your machine with the classroom extention found [here](https://github.com/github/gh-classroom)
- Access to the GitHub Classroom repositories with sufficient permissions to clone and push changes

## Setup

1. Clone this repository to your local machine.
2. Ensure you have a directory named `template` in the same directory as the script. Place any files or folders you want to copy into each student repository inside this `template` directory.

## Running the Script

To run the script, use the following command in the terminal:

```bash
python grader.py [assignment_number]
```

## What the Script Does

1. Clones the student repositories from GitHub Classroom into a directory.
2. Copies files from the template directory into each cloned repository, overwriting any existing files with the same name.
    - The template file provided in this here is for grading the following [repo](https://github.com/phuijse/python-github-classroom)
3. Commits the changes in each repository. If there are no new changes, an empty commit is made. This commit serves to re-trigger the autograder.
4. Pushes the commits to the corresponding repositories on GitHub.

## Caution

- This script will overwrite files in the student repositories if they have the same name as those in the template directory. Use with caution.
- Ensure you have the necessary permissions before attempting to push changes to student repositories.
