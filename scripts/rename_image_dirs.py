import sys
import os
import shutil
import argparse
from win10toast import ToastNotifier
import time

FLAGS = None

base_path = os.getcwd()


def sendCompletedNotification(title, body):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                   body)
                #    icon_path=None,
                #    duration=10000,
                #    threaded=False)
    # Wait for threaded notification to finish
    # while toaster.notification_active(): time.sleep(0.1)

def main(_):
    target_path = os.path.join(base_path, FLAGS.target_dir)

    for path, subdirs, files in os.walk(target_path):
        # print("Path: ", path)
        subDir = os.path.basename(path).split("_",1)
        # if we parsed out the numbers '12321_species_kind
        # if (len(subDir) > 1 and type(subDir[0]) is int):
        if (len(subDir) > 1 and subDir[0].isdigit()):
            original = os.path.basename(path)
            renamedDir = os.path.join(target_path, subDir[1])
            # print ("rename %s to %s" %(path, renamedDir))
            try:
                os.rename(path, renamedDir)
                print ("Successfuly renamed %s to %s" %(os.path.basename(path), subDir[1]))
            except OSError as error:
                print ("Error Renaming dir %s. %s" % (path, error))
    sendCompletedNotification("SUCCESS", "Program finished running")

parser = argparse.ArgumentParser()
parser.add_argument(
    '--target_dir',
    type=str,
    default='',
    help='Path to folders of labeled images.'
)
FLAGS, unparsed = parser.parse_known_args()
main(sys.argv[0])
