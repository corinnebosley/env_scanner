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
    
7. Activating the SSS environment:

    a. (In terminal):
    
    export PATH=/opt/scitools/environments/default/current/bin:$PATH
    
    b. (At top of python file; shebang):
    
    '#!/opt/scitools/environments/default/current/bin/ python'
    
    c. (In terminal with module load):
    
    module load scitools
    
8. Making a PR against a PR:

    git push origin branch_name
    
    Then go to Github, press 'Make PR' button, and select remote and branch name to make the PR against (instead of 'Upstream' and 'Master').
    
9. Using kapture:

    kapture lives in backpack/kapture, to which there is a link in my pth files (use the alias 'pth' to view these).
    
    This folder contains several shell scripts to run the kapture module and display the blockview graphic.  Make new run scripts based on these to run kapture with other scripts.
    
    Kapture takes samples of processor activity at various stages during the run of the script, so the horizontal stripes in the blockview graphic represent what is being processed at any given sample time.  Processes which take a long time will be represented by long vertical stripes formed by many samples of the same process.

10. Re-running a build for the SSS:

    Any additions that have been made (a new or updated recipe or patch) will prompt a tarball to be built in my local copy of the SSS.
    
    If this fails, or I need to make changes and re-run the build, I will need to remove the already-built libraries that I would like to rebuild.  These can be found here:
    
    /data/local/cbosley/conda_bld/root/linux-64
    
11. Accessing the HPC:

    (In a terminal, type any of these options to connect to the selected node)
   
    ssh -Y xcel00
        
    ssh -Y xcel01
        
    ssh -Y xcfl00

    ssh -Y xcfl01
    
12. Kicking a cron to run while I watch it (pervy...)

    For the controlling SSS crontab:
    
    - Switch to AVD user:
    
      su - avd 
      
      [password]
      
    - ssh onto cron host machine:
    
      ssh -Y els056
      
      bash
      
    - navigate to crontabs folder and open cron in editor:
    
      cd $LOCALTEMP
      
      cd avd_crons/
      
      cd crontabs/
      
      gedit els056.avd.crontab &
      
    - edit execution time of section I want to run so that it runs a few minutes after this process
    
    - back in terminal, tell cronanny to register the changes locally:
    
      cd ..
    
      ./cronanny.sh crontabs/
      
    - watch for execution of cron:
    
      top
      
      u avd
      
    - in a new terminal, navigate to folder containing updates of cron:
    
      cd $SCRATCH
      
      cd ../avd
      
      cd logs/
      
    - when top shows that the cron is running, list the log directory to find the running cron log and tail it:
    
      ls -ltr
      
      tail -f [logfile]
      
