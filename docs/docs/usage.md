## Using the Accessibility test tool

The tool t akes a series of urls or a single url to support accessibility testing.

It uses the axe library to test. 
    
Do not run this too often: it is a heuristic to help test, not a replacement for manual testing. Results may change between runs.

### Installing

The tool is a command line tool that relies on having at least the Firefox webdriver to run. You can optionaly run it with a Chrome driver, but this needs to be installed. 

### Using the Tool

The main usage is to run:

```
python accessibility.py
```

It takes some options. 

A single url:

```
python accessibility.py -u https://google.com
```
or 
```
python accessibility.py -url https://google.com
```

A file of urls

```
python accessibility.py -f mylist.csv
```
or 
```
python accessibility.py -file=mylist.csv
```

Chrome

```
python accessibility.py -c -f mylist.csv
```
or 
```
python accessibility.py chome -file=mylist.csv
```

This will enable Chrome as a driver. 