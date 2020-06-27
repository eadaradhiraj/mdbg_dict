#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
import colorama as clr

from mdbg.mdbg import mdbg_class

clr.init(autoreset=True)

LINE_LENGTH = 60


def ensure_unicode(string):
    if hasattr(string, "decode"):
        return string.decode("utf-8")
    return string


def str2bool(v):
    """
    Used to parse binary flag args
    Copy-paste from stack overflow
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    parser = argparse.ArgumentParser(description="Unoficial CLI for mdbg chinese dictionary.")
    parser.add_argument("simplified", type=str, help="Simplified or Traditional characters",
        choices=[0, 1])
    parser.add_argument("word",
                         type=ensure_unicode,
                         help=("Word to translate."))
    parser.add_argument("--max-results", "-n", type=int, default=10,
                        help="Number of results to display. -1 for no limit.")
    parser.add_argument("--color", "-c", type=str2bool, default=True,
                        help="Use color in output.")
    args = parser.parse_args()

    return args


def print_header(from_lang, to_lang):
    print(u"{}{}{}\n{}{}{}".format(
        from_lang,
        " "*(LINE_LENGTH-len(from_lang)),
        to_lang,
        "="*len(from_lang),
        " "*(LINE_LENGTH-len(from_lang)),
        "="*len(to_lang),
    ))


def print_translation(res, do_color):
    def apply_color(string):
        if do_color:
            # Apply color codes
            string = string.replace("[", clr.Fore.BLUE + "[")\
                            .replace("]", "]" + clr.Fore.RESET)
            string = string.replace("{", clr.Fore.BLUE + "{")\
                            .replace("}", "}" + clr.Fore.RESET)

        return string

    # Three points less for the spaces and one point less for the equal sign,
    # so tables don't break
    padding_len = LINE_LENGTH-len(res['hanzi'])-4
    print(u"{} {} {} {} {}".format(apply_color(res['hanzi']),
                                "."*padding_len,
                                apply_color(res['pinyin']),
                                "."*padding_len,
                                apply_color(res['defs']),
                                ))



def run():
    args = parse_args()

    results = mdbg_class.translate(args.word,
                            args.simplified)
    n_results = len(results)

    if not results:
        print("No results found for {}.".format(args.word))
    else:
        print("Showing {} of {} result(s)\n".format(
            min(args.max_results, n_results), n_results))
    
    for i, res in enumerate(results):
        print_translation(res, args.color)
        if i == args.max_results:
            break


if __name__ == "__main__":
    run()