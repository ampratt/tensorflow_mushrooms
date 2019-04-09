import sys
import os
import shutil
import argparse

FLAGS = None

base_path = os.getcwd()

def main(_):
    target_path = os.path.join(base_path, FLAGS.target_dir)
    for path, subdirs, files in os.walk(target_path):
        if (path != target_path and len(files) < 20):
            # print ("Ready to delete %s, of count %d " % (path, len(files)))
            deleteDir(path)


def deleteDir(path):
    print ("Ready to delete %s " % path)
    try:
        shutil.rmtree(path)
        print ("Successfully Deleted directory %s " % path)
    except OSError:
        print ("Error Deleting directory %s" % path)

parser = argparse.ArgumentParser()
parser.add_argument(
    '--target_dir',
    type=str,
    default='',
    help='Path to folders of labeled images.'
)
FLAGS, unparsed = parser.parse_known_args()
print(sys.argv[0])
main(sys.argv[0])
