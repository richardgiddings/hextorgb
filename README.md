# README

A simple python script that takes hex string in the format "#AAAAAA" or "AAAAAA" and returns the RGB value.

Usage:
    ```python3 hextorgb.py "<hex>"```
where hex is the value you want to convert to rgb.

Returns a tuple of the RGB values if valid and -1 if the hex value passed in is invalid.

Some basic tests can be run using ```python3 tests.py```