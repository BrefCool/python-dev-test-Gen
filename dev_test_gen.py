import sys
import os
import shutil

is_exe_file = getattr(sys, 'frozen', False)

if is_exe_file:
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    APPLICATION_PATH = sys._MEIPASS
else:
    APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

# TEMPLATES_LOCATION = os.path.join(sys.path[0], 'templates')
DEST_PATH = os.getcwd()
DEV_FILE_NAME = "dev.py"
UTEST_FILE_NAME = "dev_unittest.py"

os.chdir(APPLICATION_PATH)

if __name__ == "__main__":
    counts = len(sys.argv)
    data = ""
    if counts > 1:
        # get file name to be created
        dev_file_name = sys.argv[1]
        if is_exe_file:
            src_dir = os.path.abspath(os.path.join(APPLICATION_PATH, "../.."))
        else:
            src_dir = APPLICATION_PATH
        dst_dev_file_name = "{}.py".format(dev_file_name)
        dst_tst_file_name = "{}_ut.py".format(dev_file_name)
        # copy template file to the local path
        try:
            shutil.copy2(os.path.join(src_dir, 'templates', DEV_FILE_NAME),
                        os.path.join(DEST_PATH, dst_dev_file_name))
            shutil.copy2(os.path.join(src_dir, 'templates', UTEST_FILE_NAME),
                        os.path.join(DEST_PATH, dst_tst_file_name))
        except Exception as e:
            print("copy failed: %s" % e)
            sys.exit(-1)
        # modify the content of the dev.py
        try:
            with open(os.path.join(DEST_PATH, dst_tst_file_name), 'r+') as file:
                for line in file.readlines():
                    line = line.format(dev_file_name)
                    data += line
            with open(os.path.join(DEST_PATH, dst_tst_file_name), 'r+') as file:
                file.writelines(data)
        except Exception as e:
            print("convert error: %s" % e)
            sys.exit(-2)
    else:
        print("you should input the dev file's name!")
        sys.exit(1)