# Github Price Checker
Using python, pytest, and github actions to create a recurring price checker.

# What it does
Using beautiful soup, I query Playstation.com and Apple.com for the price of games/apps I want to check the price of.  I assert that the price of the item is full price.  If it fails, it means there is a price change and I should go check it out.

# Running
Using Github Actions, the repo is set up to run every morning at 7am PT.

