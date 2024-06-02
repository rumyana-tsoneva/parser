# Log Parser

This is a project to parse log files consisting of (unix_timestamp, host_from, host_to) rows with a python script
The user has to inser file name, start time, end time and a host name.
The script returns a list with all other hosts that were connected to it 
(irrespective of the source of the connection) for the given time range.

### Running

The code has been tested in the following enviornment:
+ python 3.10.9
+ regex 2.2.1


Run the following script to start the demo:

```
python logs_parser.py
```
