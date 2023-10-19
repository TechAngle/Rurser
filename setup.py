from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1}},
    zipfile = None,
    console = [{
            "script":"rurser.py",
            "icon_resources": [(0, "rurser.ico")],
            "dest_base":"Rurser"
            }],
)

