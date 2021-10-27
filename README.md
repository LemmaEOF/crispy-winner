# crispy-winner
Mitigate discord phishing attacks by spamming their webhooks

## What it does

The PirateStealer phishing malware sends its ill-gotten gains (including tokens, passwords, and *credit card info*) to Discord webhooks. This project takes a list of webhooks extracted from malware payloads and spams the pig poop balls to them with an @\everyone ping. Doing this fast enough can result in hitting the webhook's rate limit, shutting that webhook down and preventing other payloads from transmitting.

## How to run

1. install Python (preferrably >3.0)
2. run `pip install crispy-winner` in the terminal
3. run `crispy-winner` in the terminal
4. profit

## Contributing

This project is under the Fuck Around and Find Out License. It is to be used for Good, not Evil. **THIS PROJECT MAY ONLY BE USED TO PING-SPAM WEBHOOKS BELONGING TO PHISHERS AND FASCISTS. DO NOT USE IT TO SPAM ANYONE ELSE.**

If you encounter any other phishing malware with other webhooks, please write a PR to add them to `webhooks.txt`. In the future I may write a tool to automatically extract the webhook from malware EXEs.

If you want to help in other ways, report [this project](https://github.com/bytixo/PirateStealer) to GitHub using the [Report Content](https://github.com/contact/report-content) form. Some versions of the payload pull the raw code from this repo in order to function, so getting it removed will shut down numerous branches.