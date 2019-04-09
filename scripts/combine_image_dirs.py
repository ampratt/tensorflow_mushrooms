import sys
import os
import shutil
import argparse
from win10toast import ToastNotifier
import time

FLAGS = None

# dir_path = os.path.dirname(os.path.realpath(__file__))
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

# def main(_):
#     # root = base_path    # "/home/patate/directory/"
#     target_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.originals_dir)
#     cleaned_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.cleaned_dir)
#     createNewDir(cleaned_path)

#     for path, subdirs, files in os.walk(target_path):
#         # print("Path: ", path)
#         subDir = os.path.basename(path).split("_")
#         # if we parsed out the numbers '12321_species_kind
#         if (len(subDir) > 1):
#             subDir = subDir[1]
#             print("Species folder: [ %s ], image count %d " % (subDir, len(files)))
#             newDir = os.path.join(cleaned_path, subDir)
#             createNewDir(newDir)
#             copyFiles(path, newDir)

# originals already have numbers removed from directory
def main(_):
    target_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.originals_dir)
    cleaned_path = os.path.join(base_path, FLAGS.base_dir, FLAGS.cleaned_dir)
    createNewDir(cleaned_path)

    for path, subdirs, files in os.walk(target_path):
        # print("Path: ", path)
        subDir = os.path.basename(path).split("_")
        # if we parsed out the numbers '12321_species_kind
        if (len(subDir) > 1):
            subDir = subDir[0]
            print("Species folder: [ %s ], image count %d " % (subDir, len(files)))
            newDir = os.path.join(cleaned_path, subDir)
            createNewDir(newDir)
            copyFiles(path, newDir)
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
    for file in files:
        sourceFilePath = os.path.join(sourceDir,file)
        destinationFilePath = os.path.join(destinationDir,file)
        try:
            if (not os.path.isfile(destinationFilePath)):
                shutil.copy(sourceFilePath, destinationDir)
                print ("Successfuly copied to cleaned_dir: %s " % destinationFilePath)
        except Error:
            print ("Error copying file %s to cleaned_dir" % file)


# print("name: ", __name__)
# if __name__ == '__main__':
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
    default='images',
    help='Path to folders of labeled images that need to be cleaned.'
)
parser.add_argument(
    '--cleaned_dir',
    type=str,
    default='combined_subtypes',
    help='Path to folders of cleaned images.'
)

FLAGS, unparsed = parser.parse_known_args()
# print("args: ", sys.argv)
# print(FLAGS.base_dir)
print(sys.argv[0])
main(sys.argv[0])
