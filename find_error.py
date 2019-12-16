# how to find the python execute file
# almost in "/usr/bin" or "/usr/local/bin"

# Procedure for finding the Error on log files.
# 1. Find the log files for today.
# 2. Find the error on each log files.
# 2-1. If the error is exist on the file, output the filename.
# 2-2. If the error is not exist on the file, just skip.

# 2rd party
from datetime import datetime # module about date or time
import subprocess             # module for execute some command
import re                     # regular expression


def input_db_cmd(cmd):
    """
    Execute the command

    :param cmd: Command for linux or something else.
    """
    print("CMD: {}".format(cmd))
    subprocess.call(cmd.split(" "))


def notify_error(filename):
    """
    Send the notify about filename with error 

    :param filename: Log file name.
    """
    print("\nFilename: {}".format(filename))

    # Expected text filter list
    error_filter = re.compile(r"[e|E]rror|ERROR")

    # Unexpected text filter list
    ora_00942_filter = re.compile(r"ORA-00942")
    
    f = open(filename, 'r') 
    raw_data = f.read()
    f.close()

    # List of Filterd
    errors = error_filter.findall(raw_data)
    ora_00942 = ora_00942_filter.findall(raw_data)
    
    if len(errors) == len(ora_00942):
        print("-: No ERROR")
        return
    else:
        print("-: Please check the ERRORs")
        # if you need some commands, please add the command with the function of 'input_db_cmd'
        # way1: input_db_cmd("cmd1 cmd2 %s cmd3 cmd4" % filename)
        # way2: input_db_cmd("cmd1 cmd2 {} cmd3 cmd4".format(filename))
        # way2-2: input_db_cmd("cmd1 {} cmd2 {} cmd3".format(filename, filename))
        return


def main():
    start_string = "START TO FIND THE ERRORS"
    print("=" * len(start_string))
    print(start_string)
    print("-" * len(start_string))
    # find the logs files
    ## get string for today as some format.
    today = datetime.now().strftime("_%Y%m%d")

    ## get name list of log files
    print(" [Find the log files]")
    cmd = ['find', '-name', '*' + today + ".log"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log_files = p.communicate()[0].split('\n')[:-1]

    print("   >> Found log files; {}".format(log_files))

    for log_file in log_files:
        notify_error(log_file)

    print("")
    finish_string = "FINISH TO FIND THE ERRORS"
    print("-" * len(finish_string))
    print(finish_string)
    print("=" * len(finish_string))

if __name__=="__main__":
    main()
