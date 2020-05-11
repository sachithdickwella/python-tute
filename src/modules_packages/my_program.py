#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from modules_packages.my_module import my_func
from modules_packages.MyMainPackage import my_main_script                # Un-resolved import hence this package in 
from modules_packages.MyMainPackage.SubPackage import my_sub_script      # sub-folder. Do not work even used the full-qualified name here. 

# FULL-QUALIFIED name must use to access the package outside of the package and subsequent packages.
# VS Code warns when subsequent package access without full-qualified name, but doesn't work. Only
# works when access without full-qualified name (current directory) to access subsequent packages from
# inside a package that be parent to this subsequent packages. 

my_func()
my_main_script.report_main()
my_sub_script.sub_report()