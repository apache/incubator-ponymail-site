# Importing Data to Pony Mail #
Pony Mail supports many ways of importing your old mail archives via the
`import-mbox.py` script. For command line argument tips, run `python3
import-mbox.py --help`.

Imports are digested equally every time (*), so you can
import from the same source multiple times without creating duplicate emails in
the archive. Both the archiver and the importer use the same digest method, so
they can overlap. Usually, you'll want to set up the archiver first, and when
emails start flowing through it, you'll use the importer to import older emails.

## Importing from mod_mbox

### Warning ###

Pony Mail relies on the mail headers to determine the correct list name for each email.

If in any doubt, import a single list at a time and use the --lid flag to specify the correct list name.

### Importing a single domain
Provided you have the main mod_mbox page at https://your.tld/mod_mbox/ and your (sub)domain resources at
https://your.tld/mod_mbox/$list-yourdomain/, you can import all lists from that domain using:

`python3 import-mbox.py --source https://your.tld/mod_mbox/ --mod-mbox --project yourdomain`

For a quick update, which only imports the last 2 months of mail, append the `--quick` flag.

You can also import just a single list by specifying that list ID:

`python3 import-mbox.py --source https://your.tld/mod_mbox/ --mod-mbox --project listname-yourdomain`

### Importing an entire archive (multiple domains)
To import an entire site, use the same command as above, but omit the `--project` flag

`python3 import-mbox.py --source https://your.tld/mod_mbox/ --mod-mbox`

### Setting the domain or list id properly in case of variance
If your old archive varies in terms of list IDs across time, you can force harmonization by using the `--lid` or `--domain` flags:

`python3 import-mbox.py --source https://your.tld/mod_mbox/ --mod-mbox --project listid-yourdomain --lid "<listid.yourdomain.tld>"`

This should only be done one list at a time.

## Importing from Pipermail
To import from pipermail, you will have to run the import one list at a time. As with mod_mbox imports, you must specify a source, but use `--pipermail` instead of `--mod-mbox`:

`python3 import-mbox.py --source https://your.tld/pipermail/foolist/ --pipermail`

### Pipermail and html-only emails
While you can convert HTML-only emails to text using `--html2text`, Pipermail has some peculiarities
where it adds a text/plain message to these emails, thus preventing html2text from working. You can
circumvent this by using the `--ignorebody "foo"` arg to ignore all text/plain bodies containing `foo`.

While the `project` flag is not needed here, you may wish to specify the list ID for the import.

## Importing from locally stored mbox files
To import from one or more local mbox files, specify a filesystem path as the source:

`python3 import-mbox.py --source /tmp/mylists/`

This will recursively import all files with the extension '.mbox'.

You can change the extension as follows:

`python3 import-mbox.py --source /tmp/mylists/ --ext .mbx`

To match all files with any non-empty extension:

`python3 import-mbox.py --source /tmp/mylists/ --ext '.*'`

To match files regardless of extension:

`python3 import-mbox.py --source /tmp/mylists/ --ext ''`

Or you can import a single file:

`python3 import-mbox.py --source 2016-11.mbox`

(This is supported in versions after 0.9)

## Test archives
We have a few test archives for those that wish to test large imports.
They can be found in gzip format at [http://ponymail.info/mboxes/](http://ponymail.info/mboxes/)

(*) The digest depends on the [archiver] generator setting in ponymail.cfg
If that varies between imports, then duplicates will occur
