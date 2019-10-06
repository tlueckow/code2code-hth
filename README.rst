========
c2chth
========

A code transformation tool.
Apply a pattern to list of similar shaped code blocks.

In a first step every input code block will be tokenized.
The result is a list of token lists.

In a second step a transformation pattern will be applied to each token list.

A token can be referenced in a transformation pattern by '%'
followed by a transformation operation and a token index.
So '%cc2' will be replaced by the camel case version of the second token.

Each applied pattern results in a line in the output text.

Example
-----

Given the following input file

::

    private String firstName;
    private Address deliveryAddress;

will be tokenized to a list of token lists

::

    [["private", "String", "firstName"]
    ["private", "Address", "deliveryAddress"]]

and this transformation

::

    c2chth -p "obj.set%pc3();" input.txt

will result in following output

::

    obj.setFirstName();
    obj.setDeliveryAddress();

Usage
-----
::

    usage: c2chth.py [-h] [-V] [-p PATTERN] [-v] [-o FILE] file

    Code to Code transfomer - Hope This Helps

    positional arguments:
    file                  file name to process

    optional arguments:
    -h, --help            show this help message and exit
    -V, --version         show program's version number and exit
    -p PATTERN, --pattern PATTERN
                            pattern will be applied to all input code blocks
    -v, --verbose         increases log verbosity (can be specified multiple
                            times)
    -o FILE, --output FILE
                            redirect output to a file

Following transformation operations are supported:

::

    id      identity        <unchanged>
    uc      upper case      FIRSTNAME
    lc      lower case      firstname
    cc      camel case      firstName
    pc      pascal case     FirstName
    sc      snake case      first_name
    cn      const case      FIRST_NAME
