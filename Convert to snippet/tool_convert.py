print('**************START**************')

def convert_format_snippet_vs_code(line):
    '''
    Convert line of code to format of snippet in vs code
    @param: string to convert
    @return: string after convert
    '''
    # replace double mark `"` -> `\"`
    line = line.replace('"', '\\"')
    # add double mark to start and end of line
    new_line = '"' + line[0:len(line) -1] + '",' + line[len(line) -1:]
    return new_line

with open('snippet.py') as f:
    # Read data
    lines = f.readlines()
    # Open file to save new format
    file_save = open("snippet_format.py", "w")
    for line in lines:
        new_line = convert_format_snippet_vs_code(line)
        file_save.write(new_line)

    # Close file
    f.close()
    file_save.close()


print('**************END**************')
