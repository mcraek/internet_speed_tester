#!/bin/bash

# Author: Kyle McRae
# Date: May 18 / 2019
# Portions of script taken from https://gist.github.com/noelboss/3fe13927025b89757f8fb12e9066f2fa

# About:
# This script determines how incoming git pushes are handled
# At a high level, it will push files to production from the development
# directory for a Python project, and also upload the README / .exe for a project
# to production as well. Review the variables in the next section and configure accordingly
# for the project

# Set project variables

	# Initial project details
	
		projectNm="test_internet_speed" # Should match name of the Python project
		projectOwner="kyle" # Match username on scripting server for who the owner of the project is
		executableExists="True" # Set to false if there is no .exe for the project
		branch="master" # Define git branch to check out below and upload production files to py_files dir / Production. Can leave this at the default setting
		
	# Source / destination locations for development / production files
		
		gitDir="/Namek/Scripts/Development/Other/$projectNm" # Source Development directory for the project where git pushes are received
		targetPyFilesDir="/Namek/Scripts/Development/Other/$projectNm/py_files" # Define location to upload raw Python script files to when an update is received. Set to production directory if desired; e.g., if there's no .exe
		executableLocation="$targetPyFilesDir/executable" # Set location of where the executable for the project will exist on the scripting server (for the most part, you can leave this at default)
		targetExecutableDir="/Namek/Scripts/Production/Other/$projectNm" # Location to upload .exe for the project for production. For the most part, this should be wherever the production files for the project are uploaded to
		
# Push Raw Python Script Files to py_files Directory for project
# only checking out the master (or whatever branch you would like to deploy)

while read oldFiles newFiles ref
	do
		if [ "$ref" = "refs/heads/$branch" ];
		then
			echo "Ref $ref received. Deploying ${branch} branch to production..."
			git --work-tree=$targetPyFilesDir --git-dir=$gitDir checkout -f
		else
			echo "Ref $ref received. Doing nothing: only the ${branch} branch may be deployed on this server."
		fi
	done

# Upload Executable and README to Production Directory if exe exists, add Execute permission to them

	if [ "$executableExists" = "True" ]; # Remember case sensitivity with variable checks
	then
		cp -f $executableLocation/* $targetExecutableDir # Will force overwrite of production file
		cp -f $targetPyFilesDir/readme.txt $targetExecutableDir # Copies README file for project to the target .exe production dir
		cp -f $targetPyFilesDir/LICENSE $targetExecutableDir # Copies license file for project to the target .exe production dir
		chmod 775 $targetExecutableDir/* # Add [owner=full][groupOwner (Devs) = full][Other = Read / Execute] Permissions to the production files for the project
	fi

# Set py_files dir permissions to allow [full][full][none]

	chmod -R 770 $targetPyFilesDir # Especially useful when py_files is located in the Production directory. This ensures others have read / execute access to the script files

# Allow read / execute permission to others on source files specific to project only (GPL licensing)
# Allows others to git pull as well

	# chmod -R 775 $targetPyFilesDir/$projectNm

# 