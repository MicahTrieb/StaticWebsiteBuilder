#!/usr/bin/env python3
import shutil
import subprocess
import os
from textnode import *
from directorycopy import directory_copy, copying_function
from pagegenerator import generate_page
def main():
	public_dir = "/home/mici/gitHub/MicahsProjects/staticWebsite/public"
	print("Hello world! Executing main.py!")
	shutil.rmtree("/home/mici/gitHub/MicahsProjects/staticWebsite/public")
	directory_copy("/home/mici/gitHub/MicahsProjects/staticWebsite/static", "/home/mici/gitHub/MicahsProjects/staticWebsite/public")
	generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","/home/mici/gitHub/MicahsProjects/staticWebsite/public")
	subprocess.run(["python3", "-m", "http.server", "8888"], cwd=public_dir)
main()
	
