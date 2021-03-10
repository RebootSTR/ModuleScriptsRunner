# @rebootstr

# You can import all modules
from Utils.sample_text_util import text

# ------ OPTIONAL ------- #

# You can add custom name for you module
MODULE_CUSTOM_NAME = "Module Sample"

# You can change module order (default 0 - no priority)
ORDER = 1

# You can hide module from module list (you also can run it if you know number)
HIDE = True
# ------ /OPTIONAL/ ------- #


# logic for run your module (NEED!!!)
def run():
    print(text)


# if you want run module without runner
if __name__ == '__main__':
    run()
