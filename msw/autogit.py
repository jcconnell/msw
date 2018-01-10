from git import Repo,remote
import os


def autoGit(local_directory :str, commit_comment : str, author : str):
    """
    """
    # Intialise repository using local directory
    repo = Repo(os.path.abspath(local_directory))
    #  Git push
    repo.git.commit('-m', commit_comment, author=author)
    # Define origi
    origin = repo.remote(name='origin')
    # Push to remote directory
    origin.push()