# This scripts parses a log file to return a list of all hosts 
# that were connected to a host within a given range of time.
import datetime
import time
import sys
import os
import re

start_execution = time.time()


parent_directory = os.path.split(os.path.abspath(''))[0]
input_folder_path = os.path.join(parent_directory, 'input')


def validate_file_name(file_name):
    
    available_files = [file.strip(".txt") for file in os.listdir(input_folder_path)]
    pattern = r'input-file-[0-9]+'
    if not re.match(pattern, file_name):        
        print(f"Specify a valid input file name. For example: {', '.join(available_files)}")
        return False
    else:
        return True

def validate_time(string_time):
    try:
        time = string_time.strip("'")
        datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError as e:
        print(e)
        print("Specify datetime using 'Y-M-D H:M:S' format.")
        return False
        
        
def parse_unix_log_timestamp(unix_timestamp):
    return datetime.datetime.fromtimestamp(int(unix_timestamp)/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')

def parse_timestamp_to_unix(timestamp):
    timestamp_strip = timestamp.strip("'")
    timestamp_to_datetime = datetime.datetime.strptime(timestamp_strip, '%Y-%m-%d %H:%M:%S') 
    return int(time.mktime(timestamp_to_datetime.timetuple()) * 1000)


def parse_log_file(file_name, time_init_unix, time_end_unix, host):
    result = []
    with open(f"{input_folder_path}/{file_name}.txt", "r") as file:
        for line in file:
            if time_init_unix <= int(line.split(" ")[0]) <= time_end_unix:
                if line.split(" ")[1] == host or line.split(" ")[2].rstrip('\n') == host:
                    unix_timestamp, host_from, host_to = line.rstrip('\n').split(" ")
                    result.append(host_from)
                    result.append(host_to)

    if len(result) >= 1:
        result.remove(host)
        result = ', '.join(list(set(result)))

        return result
    else:
        print(f"There are no connections to host {host} for the specified interval.")


# def parse_log_file(content, time_init, time_end, host):
#     '''Function to test performance when reading the whole log file.'''
    
#     list_of_lists = [[
#                       datetime.datetime.fromtimestamp(int((conn.split(" "))[0])/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f'),
#                       (conn.split(" "))[1:]
#                      ] for conn in content.split("\n")[:-1]]
    
#     filtered_by_time = [item for item in list_of_lists if time_init < item[0] < time_end]
#     filtered_by_host = [item[1][1] for item in filtered_by_time if item[1][0] == host]

#     if len(filtered_by_host) == 0:
#         return "There is no host with this name."
#     else:
#         return filtered_by_host

if __name__ == '__main__':
    print("sys args:", sys.argv)

    if len(sys.argv) == 1:
     
        file_name = input("Please, insert a file name: ")
        if validate_file_name(file_name):
            print("File name is valid.")
        else:
            file_name = input("Please, insert a valid file name: ")

        host = input("Please, insert a host name: ")


        time_init = input("Please insert a time_init using format Y-m-d H:M:S: ")

        if validate_time(time_init):
            time_init_unix = parse_timestamp_to_unix(time_init)
        else:
            time_init = input("Please insert a valid timestamp using format Y-m-d H:M:S: ")

        time_end = input("Please insert a time_end using format Y-m-d H:M:S: ")

        if validate_time(time_end):
            time_end_unix = parse_timestamp_to_unix(time_end)
        else:
            time_end = input("Please insert a valid timestamp using format Y-m-d H:M:S: ")
        
        result = parse_log_file(file_name, time_init_unix, time_end_unix, host)
        print(result)
        end_execution = time.time()

    else:
        # Implement logic where only host is provided as an argument when running the script and we want to parse all available log files
        pass

    
    print(f"Running script took: {round(end_execution-start_execution), 2} ms") 