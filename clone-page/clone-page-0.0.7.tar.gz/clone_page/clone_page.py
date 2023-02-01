import os
import argparse
import subprocess
import datetime
import sys


def download_website(url):
    now = datetime.datetime.now()
    folder_name = "{0}_{1}_{2}".format(now.strftime(
        "%Y%m%d_%H%M%S"), url.split("//")[-1].replace("/", "_"), url)
    os.makedirs(folder_name, exist_ok=True)

    command = "wget --recursive --no-clobber --page-requisites --html-extension --convert-links -P {0} {1}".format(
        folder_name, url)
    try:
        process = subprocess.Popen(
            command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            line = process.stdout.readline().decode("utf-8").strip()
            if line:
                if "%" in line:
                    print(line)
            else:
                break
        output, error = process.communicate()

        with open("{0}/wget.txt".format(folder_name), "w") as f:
            f.write("wget version: {0}\n".format(
                output.decode("utf-8").strip()))
            f.write("Downloaded at: {0}".format(
                now.strftime("%Y-%m-%d %H:%M:%S")))

        print("\nSummary:")
        print("Folder name:", folder_name)
        print("Exit code:", process.returncode)
        print("Output:", output.decode("utf-8"))
        print("Error:", error.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    try:
        subprocess.call(["wget", "--version"])
    except FileNotFoundError:
        print("Error: wget is not installed.")
        print("Please install wget and try again.")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Download a website using wget")
    parser.add_argument("url", help="URL of the website to be downloaded")
    args = parser.parse_args()

    download_website(args.url)
