# lab-logging.py
A script that allows SPU lab assistants to log their hours without having to use Banner.

This project aims to get Robert Chung's original script working again. His project can be viewed here: https://github.com/Altrum/LabLoggingScript

The main fix that currently needs to be solved is how to get Mechanize working. Mechanize is one of the packages that is necessary for this script's operation, and it is currently unrecognizable. This is not just on my system, but on a variety of other online sources. I have a feeling this issue stems from the package itself, but regardless, that is currently the main problem.

Once the script gets up and running, one can test it by: 
  (1) Downloading the file
  (2) Hardcoding your SPU username and password into the values in lines 6 and 7.
  (3) Hardcoding the days you worked into the value in line 16.
  (4) Hardcoding the days and time you worked in lines 111-128.
  (5) Running the file.

For Pull Requests:
------------------

Since only a master branch exists in this repo, make sure that your edits and revisions are congruent with the content of labHours.py.
