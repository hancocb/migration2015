#!/python25/python

import string, os, sys, datetime, time#, md5crypt, sqlite3
from time import gmtime, strftime




def remove(path, log):


    if os.path.isdir(path):
        try:
            os.rmdir(path)
            log.write('Removed directory: ' + path + '\n')
            #print "removed: %s" % path
        except OSError:
            print "Unable to remove folder: %s" % path
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
                log.write('Removed file: ' + path + '\n')
        except OSError:
            print "Unable to remove file: %s" % pypath


def deleteOldSessions(path, log):
    #current directory of script

    number_of_days = 14

    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            stat = os.stat(full_path)
 
            if stat.st_mtime <= time_in_secs:
                remove(full_path, log)

        if root is not path:
            remove(root, log)

    
    
def main():
    log = open(os.path.abspath(os.path.dirname(__file__)) + "\\delete.log" ,'w')
    log.write('Performing deletions on ' + strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n')

    path = os.path.abspath(os.path.dirname(__file__)) + "\\tmp"
    deleteOldSessions(path, log)
    log.close();

if __name__ == '__main__':
    main()