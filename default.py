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
import os

def post_scpt(file,destination):
	"Actions to perform on the file name or file (copy, archive,whatever)"
	return file,destination
	
def format(file):
	"Format that a file should match, should return (Destination folder,Name for the file) and raise an error if the file is not in that format and not to be sorted"
	return file.split("-",1)

def ignore(file):
	"Format that a file should match for it to be ignored (boolean)"
	return os.path.isdir(file)
