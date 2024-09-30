## Installation

Make sure you have virtualenv installed, then activate the environment and install the package dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Drop one set of photos into `photos1` and the other set into `photos2`.

## Running the script

Run with:

`python compare.py`

You'll get an output similar to:

```
** FOUND A MATCH - 2024-08-17 21:39:08, 1.4600890849281376 miles, 3:42:06 hours
  File: photos1/bluecar.jpg
  File: photos2/whitecar.jpg
** FOUND A MATCH - 2024-08-17 21:38:17, 1.4610075137758833 miles, 3:42:57 hours
  File: photos1/bluecar2.jpg
  File: photos2/whitecar.jpg
```
