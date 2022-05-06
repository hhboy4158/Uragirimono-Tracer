from get_traitor import GetTraitor
import argparse


def main():

    parser = argparse.ArgumentParser(description='fuck traitors')
    parser.add_argument('--p', dest='p', action='store')
    parser.add_argument('--r', dest='r', action='store')
    args = parser.parse_args()
    traitor = GetTraitor(args.r, args.p)

    traitor.loadfile()

if __name__ == '__main__':
    main()