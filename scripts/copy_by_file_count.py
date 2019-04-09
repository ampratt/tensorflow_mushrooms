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
    original_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.originals_dir)
    copy_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.copy_dir + str(FLAGS.min_files))
    createNewDir(copy_path)
    numNewDirs = 0

    for path, subdirs, files in os.walk(original_path):
        if (path != original_path and len(files) >= FLAGS.min_files):
            dirName = os.path.basename(path)
            print ("Ready to copy %s, of count %d " % (dirName, len(files)))
            newDir = os.path.join(copy_path, dirName)
            createNewDir(newDir)
            copyFiles(path, newDir)
            numNewDirs += 1
    print ("%d directories copied " % numNewDirs)
    sendCompletedNotification("SUCCESS", "Program finished running")


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
    print ("Copying %d files..." % len(files))
    for file in files:
        sourceFilePath = os.path.join(sourceDir,file)
        destinationFilePath = os.path.join(destinationDir,file)
        try:
            if (not os.path.isfile(destinationFilePath)):
                shutil.copy(sourceFilePath, destinationDir)
                # print ("Successfuly copied to copy_dir: %s " % destinationFilePath)
        except Error:
            print ("Error copying file %s to copy_dir" % file)


parser = argparse.ArgumentParser()
parser.add_argument(
    '--base_dir',
    type=str,
    default='',
    help='Base path to folders of labeled images.'
)
parser.add_argument(
    '--originals_dir',
    type=str,
    default='images_cleaned',
    help='Path to folder of labeled images to be make a filtered copy of.'
)
parser.add_argument(
    '--copy_dir',
    type=str,
    default='cleaned_over_',
    help='Path to folders of newly copied images.'
)
parser.add_argument(
    '--min_files',
    type=int,
    default=20,
    help='Min number of images to copy over.'
)
FLAGS, unparsed = parser.parse_known_args()
print(sys.argv[0])
main(sys.argv[0])
