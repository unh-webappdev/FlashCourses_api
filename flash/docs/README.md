## Documentation : FlashCourses

     Team: Project Logs

## Installation Steps:

1. Install all requirements listed in requirements.txt: pip install -r requirements.txt
2. Create a "settings_private.py" file in the same directory that common.py is in.
3. Add only the settings you need to overwrite in settings_private.py (DO NOT ALTER COMMON.PY)
4. Run migrations and create super user

Note: Most settings_private will only need the following additions:

SECRET_KEY = 'somerandomstring'
DEBUG = True
