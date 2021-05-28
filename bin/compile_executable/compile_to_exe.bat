@echo off

:: Date: 2019 - 05 - 31
:: Author: KMcRae 

:: Description: 	Used for compiling Python program to single executable with PyInstaller. Don't forget to install PyInstaller to the venv for the project
::			  		Be sure to review each line below and adjust where necessary to make it applicable to the project, particularly the variables
::					This works only to compile a program to a Windows binary and will output to the projects executable directory

:: Note: For more PyInstaller arguments you can use, see https://pyinstaller.readthedocs.io/en/v3.3.1/usage.html

:: Set variables

	:: Set PyInstaller variables

		:: Set spec file name here and path relative to this batch file
		SET py_spec_file=.\make_spec\test_internet_speed.spec

		:: Location of PyInstaller for the program relative to this batch file. Should be the location of where PyInstaller is installed in the virtual environment
		SET project_pyinstaller=..\env\Scripts\PyInstaller

		:: Set executable for verpatch to reference (This needs to match the exe name given to your program by the PyInstaller spec file)
		SET executable_name=test_internet_speed

		:: Relative destination for compiled exe to output to
		SET destination=..\..\executable

		:: Working directory for PyInstaller to place temporary files
		SET working_dir=%windir%\temp %executable_name%.py

	:: Set variables for verpatch to add metadata to exe (version, description, etc. viewable by right-clicking exe > Properties)

		SET version="1.0.0.0 (%date%)"
		SET product_version=/pv "1.0.0.0 (%date%)"
		SET file_desc=/s desc "Tests Internet download / upload speeds using fast.com"
		SET copyright=/s copyright "Copyright (c) 2019, KM"
		SET product_info=/s product "test_internet_speed"

:: Compile program with PyInstaller variables set above

	%project_pyinstaller% --distpath %destination% %py_spec_file%

:: Cleanup PyInstaller Junk

	::RD /S /Q .\build
	::RD /S /Q .\dist

:: Use VerPatch To Apply Version Info / Metadata to exe

	verpatch-set_exe_metadata\verpatch %destination%\%executable_name%.exe /va %version% %product_version% %file_desc% %copyright% %product_info%
