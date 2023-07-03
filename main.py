from fs import *
from decompile import *
from del_com import *
from dang_func import *

import argparse
import os

def create_output_dir():
    cur_path = os.getcwd() 
    if os.path.exists(cur_path+ '\output') == False:
        pt = cur_path + '\output'
        os.mkdir(pt)
    return cur_path+ '\output'
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program for decompiling and analyzing jar files, pls provide the path to the directory where you want to find the dangerous functions or the path to the server with the .jar files  ")
    parser.add_argument('-dec', dest="dec", 
        choices=['cfr','procyon'], type=str, const=None, help="Select decompliler")
    parser.add_argument('-s', dest="s", 
        type=str, const=None, help = "Path to server directory")
    parser.add_argument('-d', dest="d", 
        type=str, const=None, help = "Path to the directory where you want to find the dangerous functions")
    parser.add_argument('-f', dest='f', 
        type=str, const=None, help='Path to the file with dangerous functions')
    parser.add_argument('-ptd', dest='ptd', 
        type=str, const=None, help='Path to decompilers')
    parser.add_argument('-comments', dest='comments', 
        type=str, const=None, help='Additional options which allow deleting comments in .java files. This option reduces the percentage of false positives ')
    args = parser.parse_args()
    if(args.dec == None or (args.s == None and args.d == None) or args.f == None or args.ptd == None):
        print("There are no necessary arguments")
        quit()
    
    path_to_output = create_output_dir()
#-dec procyon -d \"E:\\jar_parse\\output\\procyon_2023-07-01_17-47-37\" -f E:\\jar_parse\\dangerous_func.txt -ptd E:\\decompilers\\
    if (args.s != None):
        list = fs(args.s) #list of jar file
        pt = dec(args.dec, args.ptd, list)#decompile all jar files
        if(args.comments != None):
            del_com(path_to_output)#deleting comments in *.java file
        search_dang_func(args.dec, pt, args.f)
    elif ( args.d != None):
        #-d \"E:\\jar_parse\\output\\procyon_2023-07-01_17-47-37\"
        #-s F:\UEMS_CentralServer
        if(args.comments != None):
            del_com(path_to_output)#deleting comments in *.java file
        search_dang_func(args.dec, args.d, args.f)


    