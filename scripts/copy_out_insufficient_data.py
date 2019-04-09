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
    target_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.originals_dir)
    cleaned_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.copy_dir)
    createNewDir(cleaned_path)

    for path, subdirs, files in os.walk(target_path):
        if (path != target_path and len(files) < 20):
            dirName = os.path.basename(path)
            # print ("Ready to delete %s, of count %d " % (dirName, len(files)))
            # make safety copy of insufficient data
            newDir = os.path.join(cleaned_path, dirName)
            # print ("Ready to create %s" % newDir)
            createNewDir(newDir)
            copyFiles(path, newDir)
            # delete insufficient data from training data set
            deleteDir(path)
    sendCompletedNotification("SUCCESS", "Program finished running")


def deleteDir(path):
    try:
        shutil.rmtree(path)
        print ("Successfully Deleted directory %s " % path)
    except OSError:
        print ("Error Deleting directory %s" % path)


def createNewDir(path):
    if (not os.path.exists(path)):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

def copyFiles(sourceDir, destinationDir):
    files = os.listdir(sourceDir)
    for file in files:
        sourceFilePath = os.path.join(sourceDir,file)
        destinationFilePath = os.path.join(destinationDir,file)
        try:
            if (not os.path.isfile(destinationFilePath)):
                shutil.copy(sourceFilePath, destinationDir)
                print ("Successfuly copied to copy_dir: %s " % destinationFilePath)
        except Error:
            print ("Error copying file %s to copy_dir" % file)


parser = argparse.ArgumentParser()
parser.add_argument(
    '--base_dir',
    type=str,
    default='',
    help='Path to folders of labeled images.'
)
parser.add_argument(
    '--originals_dir',
    type=str,
    default='images_cleaned',
    help='Path to folders of labeled images that need to be cleaned.'
)
parser.add_argument(
    '--copy_dir',
    type=str,
    default='insufficient_data',
    help='Path to folders of cleaned images.'
)

FLAGS, unparsed = parser.parse_known_args()
print(sys.argv[0])
main(sys.argv[0])
