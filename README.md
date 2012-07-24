Tescohdear
==========

Firstly, see the *important notice* at the bottom of this file, and
the extra conditions in the licence.

So as
[you'll have already heard](http://mtdevans.com/projects/barcode/),
Tesco may have implemented a very simple system for adding offers to
products with barcodes.

I wanted to try it out so I wrote a little Python script to calculate
the new barcode with the checksum etc.

## usage

    usage: python tescohdear.py [-h] barcode price

e.g.

    python tescohdear.py 5000221503354 7

The price is given in pence.

## Mystery digit

Currently the "mystery digit" is just a random integer until someone
works out what it's for. See
[the original source](http://mtdevans.com/projects/barcode/) for more
information.

IMPORTANT
---------

You may only use this script if you don't break the law by doing
so. Please see this as an oppurtunity to make donations to the poor IT
department at Tesco by paying extra money for your pack of peanuts.
