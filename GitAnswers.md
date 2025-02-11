1.	What is the difference between git and GitLab?  
git is the distributed version control system (VCS) that works locally on the computer, and gitlab is the server where we can store a remote repository
VCS: track cahnges to files and collaborate 
manage different versions of code/files locally / remotely

gitlab: repo management service (web based platform)


2.	What is the difference between GitLab, GitHub, and BitBucket?  
different services that provide servers and interfaces for storing repos remotely

3.	Why would I ever want to use git, but not GitLab?  
if you are only working on one computer alone and dont need to collaborate 

4.	What are the steps to update the GitLab server with some changes I made on my computer?  
1. git add (files)
2. git commmit (write what was done)
3. git push

5.	What is a branch and why would I use one?  
its your own parallel universe you can work on without affecting the other collaborators branches or the main branch. 
it is useful if you wanna go off in a direction without having to stay in sync with the main branch or the others

6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?  
seperate figure made (breakout_branch_visualized)

7.	Give an example of a set of git commands that would result in a merge conflict.  
user 1: makes a change to line 3
user 1: adds to staging area
user 1: commits 

user 2: makes a change to line 3
user 2: adds to staging area
user 2: commits 

user 1: pushes to remote server
user 2: pushes to remote server -> error
user 2: pulls from remote server -> error

solution: resolve conflict before pushing

8.	Is Git suitable for latex documents?  

9.	Should I from now on version my word and powerpoint slides using git? Why/why not?  


10.	What could happen when I push my latest commit to the remote repository without pulling first?  
there might be a conflict with a file if someone has worked on the same thing as you 

11.	What happens when I pull without commiting my local changes first?  


12.	What is the difference between branching and forking?