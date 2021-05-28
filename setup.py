# Note there are some things missing from this; e.g., a license section within the classifiers

import setuptools

# Open README when Executing Program

def readme():
    with open('README.md') as r:
        return r.read()

setuptools.setup(
      name='test_internet_speed',
      version='3.7',
      scripts=['test_internet_speed/check_arguments.py','test_internet_speed/check_html_element.py','test_internet_speed/convert_speed.py','test_internet_speed/get_path.py', 'test_internet_speed/output_progress.py', 'test_internet_speed/output_results.py','test_internet_speed/parse_website.py','test_internet_speed/print_msg.py', 'test_internet_speed/terminate_web_session.py','test_internet_speed/test_internet_speed','test_internet_speed/test_site_connection.py'],
      description='Used for testing Internet upload / download speeds in MB / s using fast.com',
      long_description=readme(), # Auto add the README to the long description attribute
      author='Kyle McRae', 
      author_email='kylemcrae770@gmail.com',
      packages=setuptools.find_packages(), 
      include_package_data=True,
      zip_safe=False,	

      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows",
        "License:: OSI Approved :: GNU Lesser General Public License (LGPL 3)+"
      ],  

)