#!/usr/bin/env python3
import shutil
import subprocess
import os
from textnode import *
from directorycopy import directory_copy, copying_function
from pagegenerator import generate_page, generate_pages_recursive
def main():
	public_dir = "/home/mici/gitHub/MicahsProjects/staticWebsite/public"
	template_dir = "/home/mici/gitHub/MicahsProjects/staticWebsite/template.html"
	from_dir = "/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html"
	static_dir = "/home/mici/gitHub/MicahsProjects/staticWebsite/static"
	print("Hello world! Executing main.py!")
	shutil.rmtree(public_dir)
	directory_copy(static_dir, public_dir)
	generate_pages_recursive(from_dir,template_dir,public_dir)
	subprocess.run(["python3", "-m", "http.server", "8888"], cwd=public_dir)
main()
	
