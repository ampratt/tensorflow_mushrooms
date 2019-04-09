import sys
import os
import shutil
import argparse

FLAGS = None

# dir_path = os.path.dirname(os.path.realpath(__file__))
base_path = os.getcwd()

def main(_):
    target_path = os.path.join(base_path, FLAGS.target_dir)
    for path, subdirs, files in os.walk(target_path):
        if (path != target_path):
            print("%s, image count [ %d ]" % (path, len(files)))

parser = argparse.ArgumentParser()
parser.add_argument(
    '--target_dir',
    type=str,
    default='',
    help='Path to folders of labeled images.'
)
FLAGS, unparsed = parser.parse_known_args()
main(sys.argv[0])
