from __future__ import print_function
import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description="Manage some services!")
parser.add_argument(
    "--service-names",
    nargs="+",
    required=True,
    help="A list of services to be managed!",
)
parser.add_argument(
    "--action",
    nargs=1,
    required=True,
    choices=("start", "stop", "restart"),
    help="Action to be taken on those services!",
)
parser.add_argument(
    "--location",
    nargs=1,
    required=False,
    default="/etc/init.d/",
    help="If specified, this is where the script will look for the services!",
)
args = parser.parse_args()

if os.getenv("USER") != "root":
    print("You must run this script as ROOT!")
    raise SystemExit

for service in args.service_names:
    print("Working on: {}".format(service))

    if os.path.isfile(os.path.join(args.location, service)):
        print("Checking status of service!")
        Command = """ $(ps -ef | grep -v grep | grep {} | wc -l) """.format(service)

        ServiceStatus = subprocess.Popen(
            Command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        OK, ERR = ServiceStatus.communicate()

        servicestate = "start"
        if "0: not found" in OK.replace("\r\n", ""):
            servicestate = "stop"

        if args.action == servicestate:
            print("Incompatible action with the current state, skipping action!")
            continue

        Command = os.path.join(args.location, service) + " " + args.action[0]
        print("Trying to perform action: {}".format(Command))
        ActionResult = subprocess.Popen(
            Command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        OK, ERR = ActionResult.communicate()

        if ERR is None:
            print("OK: The service was successfully {}ed!".format(args.action[0]))
        else:
            print("ERROR: changing service state to: {}".format(ERR))
    else:
        print(
            "The service's file could not be found on: {}, skipping!".format(
                os.path.join(args.location, service)
            )
        )
