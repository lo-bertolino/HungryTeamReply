# -*- coding: utf-8 -*-
###########################################################################
#             #                                                           #
#   #####     #  euLOGy v0.1 -- Copyright © 2018 Giovanni Squillero       #
#  ######     #  http://staff.polito.it/giovanni.squillero/               #
#  ###   \    #  giovanni.squillero@polito.it                             #
#   ##G  c\   #                                                           #
#   #     _\  #  This code is licensed under a BSD 2-clause "simplified"  #
#   |  _/     #  license -- see the file LICENSE.md for details.          #
#             #                                                           #
###########################################################################

import os
import sys
import logging


class ConsoleFormatter:
    # A terse formatter that display INFO messages with no string attached,
    # and tries to avoid line breaks

    SEPARATOR1 = "ᐅ"
    SEPARATOR2 = "§"     # unicode alternatives: « » ¶ §
    RESET = "\033[0;0m"
    BLACK = "\033[0;30m"
    BLUE = "\033[0;34m"
    GREEN = "\033[0;32m"
    CYAN = "\033[0;36m"
    RED = "\033[0;31m"
    PURPLE = "\033[0;35m"
    BROWN = "\033[0;33m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_PURPLE = "\033[1;35m"
    YELLOW = "\033[1;33m"
    WHITE = "\033[1;37m"

    formatter_debug = logging.Formatter(fmt=BLUE + "%(asctime)s " + BLUE + SEPARATOR1 + RESET + " %(message)s", datefmt="%H:%M:%S")
    formatter_info = logging.Formatter(fmt=BLUE + "%(asctime)s " + CYAN + SEPARATOR1 + RESET + " %(message)s", datefmt="%H:%M:%S")
    formatter_warning = logging.Formatter(fmt=BLUE + "%(asctime)s " + YELLOW + SEPARATOR1 + RESET + " %(message)s", datefmt="%H:%M:%S")
    formatter_error = logging.Formatter(fmt=BLUE + "%(asctime)s " + LIGHT_RED + SEPARATOR1 + RESET + " %(message)s", datefmt="%H:%M:%S")

    UTF8 = None
    COLOR = None

    def __init__(self, terminal_width=None, utf8=None, color=None):
        if utf8 is None:
            ConsoleFormatter.UTF8 = os.name != 'nt'
        if color is None:
            ConsoleFormatter.COLOR = os.isatty(2) and os.name != 'nt'

        if terminal_width:
            self.terminal_width = terminal_width
        else:
            try:
                ts = os.get_terminal_size(sys.stderr.fileno())
                self.terminal_width = ts.columns
            except OSError:
                self.terminal_width = None

    def formatException(self, exc_info):
        return ConsoleFormatter.formatter_error.formatException(exc_info)

    def format(self, record, **kargs):
        npc = 0
        if record.levelno == logging.DEBUG:
            line = ConsoleFormatter.formatter_debug.format(record)
            npc = len(self.BLUE + self.CYAN + self.SEPARATOR1 + self.RESET)
        elif record.levelno == logging.INFO:
            line = ConsoleFormatter.formatter_info.format(record)
            npc = len(self.BLUE + self.CYAN + self.SEPARATOR1 + self.RESET)
        elif record.levelno == logging.WARNING:
            line = ConsoleFormatter.formatter_warning.format(record)
            npc = len(self.BLUE + self.CYAN + self.SEPARATOR1 + self.RESET)
        else:
            line = ConsoleFormatter.formatter_error.format(record)
            npc = len(self.BLUE + self.CYAN + self.SEPARATOR1 + self.RESET)
        line = line.replace('\n', ' ¶ ')
        if self.terminal_width and record.levelno % 10 != 1:
            words = line.split()
            line = " ".join(words)
            while len(line) - npc > self.terminal_width -2:
                words = words[:-4] + ["[...]"] + words[-2:]
                line = " ".join(words)

        return line


def init_logging(logger_name="", console_log_level=logging.INFO, enable_file_log=False, enable_debug_log=False, log_filename=None, terminal_width=None):
    logger = logging.getLogger(logger_name)
    logger.handlers = list()
    logger.setLevel(logging.DEBUG)

    # console
    if enable_debug_log:
        # debug: full info on stdout (no formtting)
        debug_console_handler = logging.StreamHandler(stream=sys.stdout)
        logger.setLevel(0)
        logging.addLevelName(1, "TRACEALL")
        debug_console_handler.setFormatter(logging.Formatter("%(relativeCreated)012d %(levelname)s " + ConsoleFormatter.SEPARATOR1 + " %(message)s " + ConsoleFormatter.SEPARATOR2 + " [%(module)s.%(funcName)s@%(filename)s:%(lineno)d]"))
        debug_console_handler.setLevel(0)
        logger.addHandler(debug_console_handler)
        ConsoleFormatter.COLOR = False
    else:
        # standard: some info on stderr
        standard_console_handler = logging.StreamHandler(stream=sys.stderr)
        standard_console_handler.setFormatter(ConsoleFormatter(terminal_width=terminal_width))
        standard_console_handler.setLevel(console_log_level)
        logger.addHandler(standard_console_handler)

    if not ConsoleFormatter.UTF8:
        ConsoleFormatter.SEPARATOR1 = "#"
        ConsoleFormatter.SEPARATOR2 = "|"

    if not ConsoleFormatter.COLOR:
        ConsoleFormatter.BLACK = ConsoleFormatter.BLUE = ConsoleFormatter.BROWN = ConsoleFormatter.CYAN = ConsoleFormatter.DARK_GRAY = ConsoleFormatter.GREEN = ConsoleFormatter.LIGHT_BLUE = ConsoleFormatter.\
        LIGHT_CYAN = ConsoleFormatter.LIGHT_GRAY = ConsoleFormatter.LIGHT_GREEN = ConsoleFormatter.LIGHT_PURPLE = ConsoleFormatter.LIGHT_RED = ConsoleFormatter.\
        PURPLE = ConsoleFormatter.RED = ConsoleFormatter.RESET = ConsoleFormatter.WHITE = ConsoleFormatter.YELLOW = ""

    # file
    if enable_file_log:
        if log_filename is None:
            log_filename = os.path.splitext(os.path.basename(sys.argv[0]))[0] + ".log"
            assert log_filename != os.path.basename(sys.argv[0])
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(logging.Formatter("%(asctime)s (%(levelname)s) " + ConsoleFormatter.SEPARATOR1 + " %(message)s " + ConsoleFormatter.SEPARATOR2 + " %(processName)s(%(process)d)+%(relativeCreated)d [%(module)s.%(funcName)s@%(filename)s:%(lineno)d]"))
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
