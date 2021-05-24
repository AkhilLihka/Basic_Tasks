import os
import fnmatch
import shutil
import stat
from datetime import datetime
import time
import threading


# lookup recursive
def file_copy(pattern, src, dst):
    t = time.time()
    result = fnmatch.filter(os.listdir(src), pattern)
    if result:
        for filename in result:
            print(filename)
            src_temp = os.path.join(src, filename)
            dst_temp = os.path.join(dst, filename)
            shutil.copy(src_temp, dst_temp)
            print("file 11 copy", filename)
    else:
        print("not a valid pattern", pattern)
    print("Files copied", pattern)
    print('Time taken to copy files for pattern: ' + pattern + ": ", time.time() - t)


def extract(patterns):
    directory = "database_" + str(datetime.now().strftime("%m%d%Y"))
    Destination = "/Users/akhil/Desktop/Tenant/"
    src = "/Users/akhil/Desktop/Apps/ACC"
    dst = os.path.join(Destination, directory)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for pattern in patterns:
        pattern = pattern + "*DBF"
        print(pattern)
        t1 = threading.Thread(target=file_copy(pattern, src, dst))
        t1.start()
    t1.join()
    print("Extraction completed")


patterns = [""]
extract(patterns)