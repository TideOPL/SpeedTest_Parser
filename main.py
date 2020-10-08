import time
from time import sleep
import speedtest

debug = input("Debug? \n> ")
length = float(input("How log should the intervals for the speed test be?\n> "))
time_seconds = length * 60
unlimited = input("Would you like this process to run in the background 24/7? \n> ")
sfg = int(input("What is your guaranteed speed? \n> "))

if unlimited == "no" or unlimited == "No":
    times = int(input("How many times would you like to run the test for?\n> "))


def speed():
    if debug == "No":
        servers = []

        threads = None

        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)  # Gets the download speed
        s.upload(threads=threads)  # Gets the upload speed

        results_download = s.results.download
        results_upload = s.results.upload

    if debug == "Yes":
        results_upload = 23819292  # Debugging
        results_download = 23819292  # Debugging

    upload_speed = results_upload / 1000000  # Converts Bits into MegaBytes
    download_speed = results_download / 1000000  # Converts Bits into MegaBytes
    upload_speed = round(upload_speed)  # Rounds the big number to a simple 2 digit number
    download_speed = round(download_speed)  # Rounds the big number to a simple 2 digit number
    print(upload_speed)  # Debugging
    print(download_speed)  # Debugging

    upload_speed = str(upload_speed)  # Converts the number into a string so it fits into the file correctly
    download_speed = str(download_speed)  # Converts the number into a string so it fits into the file correctly

    f = open("speeds.txt", "a")  # Opens the file and is set to append
    f.write(
        "Upload: " + upload_speed + " Mbp/s" + " | " + "Download: " + download_speed + " Mbp/s\n")  # Writes the data
    f.close()  # Closes the file after completing

    inuploadspeed = int(upload_speed)
    if inuploadspeed < sfg:
        localtime = time.asctime(time.localtime(time.time()))
        write = open("stayfast.txt", "a")
        write.write(localtime + " :: " + upload_speed + "Mbps" + " Dropped below your stay fast guarantee \n")
        write.close()


if unlimited == "No" or unlimited == "no":
    speed()  # Does the initial run
    repeat = times  # Gets the user input of how many time it should run
    while repeat > 0:  # If the times is great than 0 keep running
        sleep(time_seconds)  # Stop running for this amount of time as per user input
        speed()  # Run the function to get the speed
        repeat = repeat - 1  # Take one away from the amount of times it should run

if unlimited == "Yes" or unlimited == "yes":
    speed()  # Does the initial run
    repeat = True  # Gets the user input of how many time it should run
    while repeat:  # If the times is great than 0 keep running
        sleep(time_seconds)  # Stop running for this amount of time as per user input
        speed()  # Run the function to get the speed
