import logging
from testmodule.testmodule import testmodule
from testmodule.testmoduleerror import testmoduleconnectionerror, testmoduleerror

testmodulelogger = logging.getLogger('testmodule')
testmodulelogger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

testmodulelogger.addHandler(sh)