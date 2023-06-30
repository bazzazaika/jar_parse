from fs import *
from decompile import *
from del_com import *
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program for decompiling and analyzing jar files")
    parser.add_argument('-dec', dest="dec", 
        choices=['cfr','procyon'], type=str, const=None, help="Select decompliler")
    parser.add_argument('-s', dest="s", 
        type=str, const=None, help = "Path to server directory")
    parser.add_argument('-f', dest='f', 
        type=str, const=None, help='Path to the file with dangerous functions')
    parser.add_argument('-comments', dest='comments', 
        type=str, const=None, help='Additional options which allow deleting comments in .java files. This option increases the percentage of false positives ')
    args = parser.parse_args()
    if(args.dec == None or args.s == None or args.f == None):
        print("There are no necessary arguments")
        quit()

    #list = fs(args.s) #list of jar file
    #dec(args.dec, list)#decompile all jar files
    if(args.comments != None):
        del_com()#deleting comments in *.java file
    


    