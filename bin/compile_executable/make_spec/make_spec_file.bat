@echo off

:: Date: 2019 - 06 - 08
:: Author: KMcRae 

:: Description: 	Uses the pyi-makespec program which gets installed along with PyInstaller
::					This will generate a spec file for PyInstaller to compile a program to exe using options specified by this
::					Requires PyInstaller to be installed to the project's virtual environment prior to running this.
::					Review each variable below to generate the spec file. Once it's compiled add in any extra files to include
::					with the packaged installer (Reference the spec file example in this same directory for details on how to do this)

:: Note: For more pyi-makespec details, review the docs here: https://pythonhosted.org/PyInstaller/man/pyi-makespec.html

:: Set pyi-makespec variables

	:: Location of pyi-makespec for the program relative to this batch file. Should be the location of where PyInstaller is installed in the venv
	SET project_pyi-makespec=..\..\env\Scripts\pyi-makespec

	:: Location of main program Python file relative to this batch file to reference for compiling the exe with PyInstaller
	SET project_main_program=..\..\..\test_internet_speed\test_internet_speed.py

	:: Log level verbosity for PyInstaller. Will output logs to .\build
	SET log_level=DEBUG

	:: Set name to assign to exe
	SET executable_name=test_internet_speed

	:: Set relative location of icon to assign to exe. Icon may not display for exe within executable dir of project. In this case,
	:: copy the exe to another another location andit should show up
	:: Uncomment when icon has been added	

	::SET icon=..\program_icon\IconName.ico	

:: Create spec file in same dir as batch file. Add --noconsole to prevent shell from
:: displaying with program; e.g., You are building a GUI only
:: Add --icon %icon% when an icon has been added

	%project_pyi-makespec% %project_main_program% ^ --onefile --log-level %log_level% --name %executable_name%

		