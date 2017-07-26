# GoatSummer

Gain a ton of contest entries. Use at your own risk. They might catch on and ban you from the contest. Not my fault.

# Requirements

* Python 2.7
* Requests (`pip install requests`)

# Usage

###### Clone the project
`~ git clone https://github.com/alxgmpr/GoatSummer.git`
###### Navigate to the project
`~ cd GoatSummer`
###### Configure goat.py
```
GOATUSER = 'fake@me.com'  # GOAT email here
GOATPASS = 'password123'  # GOAT password here
```
###### Execute
`~ python goat.py`

# Known Issues

* If you get 429 from login its because your temporarily banned
* Sleeps 1 second in between requests. Not sure if this is enough.