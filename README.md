### LightweightCSVReporter

Ver 1.0

## Summary

A Lightweight CSV (Excel File) Reporter using Python.

Traverses through a given directory and gives prints out a csv report containing what file names, types, size, and last modified.

## Usage
- Directory
    Directory where the operation will happen.
- Dump Directory
    Where the csv output will be sent to
- Dump Name
    What the output csv file's name will be
- Exlusions
    File types excluded. Seperate by commas to exclude multiple types.
- Check Reclusively
    Do we want to check for folders within folders?
- Run
    Click to start process

## Known Issues
  # BUGS
    - Dump Directories must lead to an existing location. If not it will give out an error
    - Dump Name does not check for ".csv" in the entry leading to a ".csv.csv" scenario
    - Data gets destorted if running through massive amounts of files(only sometimes)
  # User Experience
    - Status does not properly display the state of the tool.
    - 

## Planned Features

1. Restoring input from previous session

## Feedback

## License & Permission
Personal Use ONLY, no commercial Use permitted

Copyright(c) 2023 Carlos Miguel Aquino
