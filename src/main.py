#!/usr/bin/env python3
from textnode import *
from directorycopy import directory_copy, copying_function
from pagegenerator import generate_page
import shutil
def main():
	print("Hello world! Executing main.py!")
	shutil.rmtree("/home/mici/gitHub/MicahsProjects/staticWebsite/public")
	directory_copy("/home/mici/gitHub/MicahsProjects/staticWebsite/static", "/home/mici/gitHub/MicahsProjects/staticWebsite/public")
	generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","/home/mici/gitHub/MicahsProjects/staticWebsite/public")

main()
	
