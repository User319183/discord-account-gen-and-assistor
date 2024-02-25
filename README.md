# Discord Account Generator/Assistant

# PATCHED - https://discord.com/invite/p3xxVhyb65 for the unpatched version
This project is a Discord account generator and assistant, designed to automate the process of creating and managing Discord accounts. It is a bypass to older browser generators and was created for fun and learning purposes. 

## Prerequisites

What things you need to run the software:

- Python 3.x
- Selenium WebDriver
- undetected_chromedriver
- pyperclip

## Usage

To generate accounts, you will need use a proxy/VPN service. The script will not work well without proxies/VPN IPs.

To generate unclaimed Discord accounts, run the following command:

```bash
python3 unclaimedgen.py

```

To generate claimed Discord accounts, run the following command:

```bash
python3 claimedgen.py

```

If you are generating claimed accounts, you will need to enter a email service provider (e.g. temp-mail.org) and a domain (e.g. @supenc.com). The script will generate a random email address using the email service provider and domain you entered. You will need to verify the email address to claim the account.

The script performs the following steps:

1. Opens Discord in a new browser window.
2. Generates random credentials.
4. Submits the credentials.
5. Waits for user input. If the user enters '1', the script logs the account's token and copies it to the clipboard.

Please note that this script may not work 100% of the time and requires good and supported proxies/VPN IPs. 

## Recommendations

While this project simulates a browser to generate accounts, it is highly recommended to use requests instead for more reliable and efficient account generation. However, be aware that Discord flags fingerprints, and this method is slightly less flagged/detected than a requests generator.

You can install a Chrome extension with Selenium CRX for hCaptcha solving, but hsw for hCaptcha solvers are outdated and flagged, so solving hCaptcha manually is recommended for more reliable and efficient account generation.

## Project Status

This project is not complete and needs work. It was created for fun and learning, and is not intended for serious use.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
