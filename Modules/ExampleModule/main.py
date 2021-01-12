# @rebootstr

# You can import all modules
from Utils.sample_text_util import text

# You can add custom name for you module
MODULE_CUSTOM_NAME = "Module Sample"


# logic for run your module (NEED!!!)
def run():
    print(text)


# if you want run module without runner
if __name__ == '__main__':
    run()
