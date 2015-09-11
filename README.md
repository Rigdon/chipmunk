# Chipmunk
[![Build Status](https://travis-ci.org/Rigdon/chipmunk.svg?branch=develop)](https://travis-ci.org/Rigdon/chipmunk)

##### A very small and simple usage mechanism for Python threadlocals.

This is an abstraction on type of `threading.local` that attempts to simply usage a bit and combat the common
problem of accidentally overwriting values that may have been added by other portions of code. It also implements the
`in` operator to test for inclusion and the bool() method to test whether the Chipmunk is holding anything.


## Example Usage

### Instantiating

The `Chipmunk` object is a sort of singleton that is instantiated upon import.

```
from chipmunk import Chipmunk #  Ready for use
```

### Storing Data

Asking the `Chipmunk` to hold something can be done in one of three ways:

Setting Attributes Directly

```
Chipmunk.acorn = "Acorn"
Chipmunk.acorn_count = 5
```

With the `store_data` method

 ```
 Chipmunk.store_data("acorn", "Acorn")
 Chipmunk.store_data("acorn_count", 5)
 ```

And with a context manager for short-term storage that removes the need for checking whether it is already holding
something with the given name.

```
Chipmunk.nut = "acorn"

with Chipmunk.hold_this("nut", "walnut"):
    do_something_with_Chipmunk()

return Chipmunk.nut #  Returns "acorn"
```

If the `Chipmunk` is already holding something and you ask it to hold something else with the same name it will raise
an AttributeError. If you want to replace an object permanently you must call either the `delete_data` or `clear`
methods or use `del Chipmunk.attr`.

```
Chipmunk.nut = "acorn"
Chipmunk.nut = "walnut" #  AttributeError thrown

Chipmunk.nut = "acorn"
del Chipmunk.nut
Chipmunk.nut = "walnut" #  OK

Chipmunk.nut = "acorn"
Chipmunk.delete_data("nut")
Chipmunk.nut = "walnut" #  OK
```

### Retrieving Data

When retrieving data from the `Chipmunk` a `bool()` check will tell you if it's holding anything at all.

```
from chipmunk import Chipmunk
if Chipmunk: #  Conditional fails
    return "Not Empty"

Chipmunk.nut = "acorn"
if Chipmunk: #  Conditional succeeds
    return "Not Empty"
```

Testing whether the `Chipmunk` is holding something with a given name is as simple as an `in` check.

```
Chipmunk.nut = "acorn"
"nut" in Chipmunk #  True
```

Data can be accessed by doing an attribute lookup directly, using the `get_data` method, or `getattr`.

```
Chipmunk.nut = "acorn"

# These all return "acorn"
Chipmunk.nut
Chipmunk.get_data("nut")
getattr(Chipmunk, "nut")
```
