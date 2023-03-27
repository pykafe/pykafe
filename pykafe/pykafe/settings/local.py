import os
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str

from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str

#GDAL_LIBRARY_PATH = os.environ.get("GDAL_LIBRARY_PATH", "/opt/homebrew/Cellar/gdal/3.6.2_2/lib/libgdal.dylib")
#GEOS_LIBRARY_PATH = os.environ.get("GEOS_LIBRARY_PATH", "/opt/homebrew/Cellar/geos/3.11.1/lib/libgeos_c.dylib") 
