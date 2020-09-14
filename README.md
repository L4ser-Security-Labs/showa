# Showa

```txt
────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████████─██████──────────██████─██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██──██░░██─██░░██████░░██─██░░██──────────██░░██─██░░██████░░██─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██──██░░██─
─██░░██████████─██░░██████░░██─██░░██──██░░██─██░░██──██████──██░░██─██░░██████░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████░░██─
─────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██████░░██████░░██─██░░██──██░░██─
─██████████░░██─██░░██──██░░██─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██──██░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░██████░░██████░░██─██░░██──██░░██─
─██████████████─██████──██████─██████████████─██████──██████──██████─██████──██████─
────────────────────────────────────────────────────────────────────────────────────
                                              External Resource Monitor
                                              By L4ser Security Labs
                                              Beta - v1.0.0
```

- - -
Automate external resources and assets monitoring.

Showa allows you to automate the monitoring of external resources and assets during active red teaming assessments.
Once a resource is down, you get an email notification notifying you of the status of the resources or assets.


## Install on Linux, Mac OS, Windows

```bash
git clone https://github.com/L4ser-Security-Labs/showa.git
cd showa
pip3 install -r requirements.txt
```

## Configuration

You can use any email provider of your choice but Showa supports only Gmail out of the box in this version.

### Using Gmail

To allow Showa to send you email notifications, [enable less secure apps from your Gmail account](https://myaccount.google.com/lesssecureapps?pli=1).
If you don't allow you'll get an authentication error from Showa.

Create a `.env` file and add your Gmail credentials.

```txt
SENDER="youremail@gmail.com"
PASSWORD="Y0urP@S$wOrD"
```

## Adding Resources

Add each resource or asset you'll like to monitor on a new line

```txt
https://google.com
https://twitter.com
```

## Cronjob

Depending on how frequesnt you want to run your cronjob, modify the cron entry below:

```txt
MAILTO=youremail@gmail.com
*/5 * * * * cd /path/to/showa && /path/to/python3 showa.py -r resources.showa -e youremail@gmail.com >> cron.log
```

To stop receiving notifications

```sh
crontab -e
```

Go ahead to delete the lines created above.

## Usage

```txt
usage: showa.py [-h] [-r R] [-e E]

External Resource Monitor

optional arguments:
  -h, --help  Shows this message and exits
  -r R        Path to resources.showa file
  -e E        Email address to receive notifications
```

## Showa in action

```bash
# one-time check status of resources
# If any resource or asset from the list is not available, you'll get an email notification

python3 showa.py -r resources.showa -e youremail@gmail.com
```

![Imgur](https://i.imgur.com/V8H3pOJ.png)

![Imgur](https://i.imgur.com/qVJ37QN.jpg)

