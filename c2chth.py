import os
import sys
import logging
import argparse

import transform

__version__ = '0.1.0'
__author__ = 'Torsten Lueckow'
__license__ = 'MIT'

log = logging.getLogger(__name__)

def transform_file(file, pattern, output):

  try:
    with open(file) as f:
      blocks = f.readlines()
    r = transform.transform(blocks, pattern)
    try:
      output.write("\n".join(r))
    except OSError as err:
       log.error("Failed writing file %s: %s", output, err)
  except FileNotFoundError as err:
    log.error("Failed reading file %s: %s", file, err)
    
def parse_command_line(argv):
    """Parse command line argument. See -h option.
    Arguments:
      argv: arguments on the command line must include caller file name.
    """

    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description="Code to Code transfomer - Hope This Helps",
                                     formatter_class=formatter_class)
    parser.add_argument("-V", "--version", action="version",
                        version="%(prog)s {}".format(__version__))
    parser.add_argument("-p", "--pattern",
                        help="pattern will be applied to all input code blocks")                    
    parser.add_argument("-v", "--verbose", dest="verbose_count",
                        action="count", default=0,
                        help="increases log verbosity (can be specified multiple times)")
    parser.add_argument("-o", "--output", metavar="FILE",
                        type=argparse.FileType("w"), default=sys.stdout,
                        help="redirect output to a file")
    parser.add_argument("file",
                        help="file name to process")                    
    arguments = parser.parse_args(argv[1:])

    if not (arguments.pattern):
        parser.error(
            '--pattern missing')

    # Sets log level to WARN going more verbose for each new -V.
    log.setLevel(max(3 - arguments.verbose_count, 0) * 10)
    return arguments

def command_line(argv):
    arguments = parse_command_line(argv)
    transform_file(arguments.file, arguments.pattern, arguments.output)


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    try:
        command_line(sys.argv)
    finally:
        logging.shutdown()

if __name__ == "__main__":
    sys.exit(main())