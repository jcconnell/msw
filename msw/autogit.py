#from git import Repo,remote
import os
import git


def autoGit(local_directory : str,
            file_to_add : str,
            comment : str, 
            author : str):
    """
    """
    # Intialise repository using local directory
    repo = git.Repo(os.path.abspath(local_directory))
    # add file
    repo.git.add(file_to_add)
    #  Git push
    repo.git.commit('-m', comment, author=author)
    # Define origi
    origin = repo.remote(name='origin')
    # Push to remote directory
    origin.push()

