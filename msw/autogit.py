import os
import git


def autoGit(local_directory : str,
            file_to_add : str,
            comment : str, 
            author : str):
    """
    Automates commiting a file to remote git hub repo.
    
    Parameters
    --------
    local_directory : the local git hub repo, str
    file_to_add : file you would like to add to remote git repo, str
    comment : commit comment you would like to use, str 
    author : author of the commit, str
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

