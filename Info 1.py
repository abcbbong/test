import os

show_expected_result = False
show_hint = False

def file_info():
    totalbytes = 0
    folder ="deps"
    
    dirlist = os.listdir(folder)
    for entry in dirlist:
        if os.path.isfile(folder = "/" + entry) and entry.endswith(".txt"):
            filesize = os.path.getsize(folder + "/" + entry)
            totalbytes += filesize
    return totalbytes

