#!/usr/bin/python2
# -*- coding:utf8 -*-

###########################################
# namesort.py
# Nom: namesort
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of yourScpts.
#
# namesort is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# namesort is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
########################################################
# LICENCE                                              #
########################################################

####
# Functions
def ruleout(f):
	"Ruling out a file"
	return os.path.isdir(f)

def whereto(f):
	"Where to sort a file, what name to use"
	return f.split("-",1)

def dprint(p):
	if args.verbose:
		print p

####
# Imports
import sys, os
import argparse

###
# Parser

# ns path -d path2
# ns  . --destination ../ [-dry] [--verbose] [--reverse path.sh]

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=("""\
Sorting files by a nameformat
"""))

parser.add_argument('path', metavar='path',nargs='?', type=str, help='the path to the folder to analyse', default=".")
parser.add_argument('--destination','-d',type=str,help='custom destination to save to')
parser.add_argument('--dry',action='store_true',help='only show actions, don\'t perform any renames')
parser.add_argument('--verbose','-v',action='store_true',help='be verbose')
parser.add_argument('--reverse',type=str,help='custom reverse script, to cancel everything')

####
# Main

args = parser.parse_args()
path_to_sort=args.path
path_to_save=args.destination
if args.reverse:
	scpt=open(args.reverse,"w+")
	scpt.write("#!/bin/sh\n")
if path_to_save==None:
	path_to_save=path_to_sort
dprint("Path: '"+path_to_sort+"'")
dprint("Saving to: '{}'".format(path_to_sort))

try:
	if not (os.path.isdir(path_to_sort)):
		print path_to_sort, "is not a directory"
		sys.exit()
	if not (os.path.isdir(path_to_save)):
		print path_to_save, "is not a directory"
		sys.exit()
except :
	print "Erreur impossible d'acceder au fichier"

listdir=os.listdir(path_to_sort)
try:
	for f in listdir:
		try:
			if not ruleout(os.path.join(path_to_sort,f)):
				where,newname=whereto(f)
				if where!=f:
					fro,to=os.path.join(path_to_sort,f),os.path.join(path_to_save,os.path.join(where,newname))
					dprint("Moving from '{}' to '{}'".format(fro,to))
					if not args.dry:
						os.renames(fro,to)
						scpt.write("mv {} {} \n".format(to,fro))
				else:
					raise ValueError
			else:
				dprint("Directory: "+f)
		except ValueError:
			dprint("Untouched: "+f)
except:
	print "Error", sys.exc_info()[:2]
