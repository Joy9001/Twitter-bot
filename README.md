# Internet Speed Twitter Bot

This is a Python script that automates the process of checking your internet speed using Speedtest.net and tweeting your internet service provider about any discrepancies between the promised and actual internet speeds.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your machine
- Chrome web browser installed
- ChromeDriver executable file compatible with your Chrome version
- Twitter account credentials (email, password, and username)

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages by running the following command:
    ```
    pip install -r requirements.txt
    ```
3. Set the following environment variables:
    - `CHROME_DRIVER_PATH`: Path to the ChromeDriver executable file.
    - `TWITTER_EMAIL`: Your Twitter account email.
    - `TWITTER_PASSWORD`: Your Twitter account password.
    - `TWITTER_USERNAME`: Your Twitter account username.

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to start the script:
    ```
    python main.py
    ```
3. The script will open a Chrome browser window and perform the following steps:
    - Accept the privacy policy on Speedtest.net.
    - Start the internet speed test and retrieve the download and upload speeds.
    - Log in to your Twitter account (if not already logged in).
    - Compose a tweet mentioning your internet service provider and the speed discrepancy.
    - Save the tweet as a draft.

## Customization

You can customize the following variables in the `main.py` file according to your needs:

- `PROMISED_DOWN`: The promised download speed from your internet service provider.
- `PROMISED_UP`: The promised upload speed from your internet service provider.
