#!/usr/bin/env bash
#
#Source: https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/
< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;
