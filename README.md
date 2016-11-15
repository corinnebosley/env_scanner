# learning

This repo is entirely for my own benefit, and is intended to house the learning materials I accrue in my career at the Met Office.


## Reminders

1. Where your .pth files live:

    /home/h06/cbosley/.local/lib/python2.7/site-packages
    
2. How to symlink:

    ln -s /path/to/file /path/to/symlink
    
    rm link (no slash on end of link)
    
3. How to check the disk usage (file sizes) of stuff in my home space:

    du -sh *
    
4. Rebasing:

    git rebase -i HEAD~number-of-commits-to-squash

    git rebase --abort
    
5. Fetching a remote branch:

    git remote add marqh https://github.com/marqh/iris.git
    
    git fetch marqh mpldep:marks_mpldep
    
    git checkout marks_mpldep
    
    OR (this is my preference as it seems less confusing):
    
    git remote add [fork name(i.e. patrick)] [repo_URL(i.e. https://github.com/pp-mo/iris.git)]
    
    git fetch [forkname]
    
    git checkout -b [new branch name] [fork name/fork branch to track]
    
6. Watching a changing directory:

    watch -n0.5 "ls -ltr | tail -20"
    
    (This means update the terminal every 0.5 sedonds for changes and list the last 20 items in the directory.)
    
    
