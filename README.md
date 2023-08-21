# PortScanner

This tool basically scans the given IP address for ports and reports back wheter the any port is open or not.

## Table of Contents

- [Installation]
    - [Python]
    - [PIP]
    - [requirements]
- [Usage]

## Installation

First of all make sure you have python and pip installed.

## Python 

As the tool is built up using python it requires python to make the code work.

## To install python in linux

```bash
sudo apt install python3
```

Run this command to install python in linux.

## To install PIP

__For windows__

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Use this command to get pip.

Once after running this install pip using the command below.

```bash
python get-pip.py
```
After installing pip make sure pip is installed in your system using the command below.

```bash
pip --version
```

## Installing requirements.txt:

This tool requires you to install colorama for the colours.

To use the tool more efficiently install the requirement's from the provided requirements.txt.

```bash
 pip install -r requirements.txt
```

After this step you are ready to run the program.

## Usage

Run the script using python

```bash
python portscanner.py
```

1. Enter the IP address you want to scan.
2. Give the starting port you want to scan from.
3. Give the end port for the tool to scan until it.

![portscan.py](https://github.com/Victorcreations/portscanner/blob/main/images/Screenshot%20from%202023-08-21%2022-30-06.png)

![portoutput](https://github.com/Victorcreations/portscanner/blob/main/images/portoutput.jpeg)
