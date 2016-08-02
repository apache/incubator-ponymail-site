# Download Apache Pony Mail (Incubating)

The latest release of Pony Mail is 0.9, released on 2016-08-02. You can fetch it here:

[Download Apache Pony Mail (Incubating) 0.9 from a mirror](/dyn/closer.cgi/incubator/ponymail/apache-pony-mail-0.9.incubating.tar.gz)

## CHANGES in 0.9:

- Private lists can be hidden in the index from users without access
- Fixed an issue where LocalStorage limits would break the site
- Fixed an issue with gravatars not showing up
- UI can now auto-scale, allowing as many results per page as screen height will support
- Users can add favorite lists to their user menu (shortcuts)
- Reply-to and compose now works from the permalink page
- Archiver can now set an explicit List ID from command-line
- Archiver and importer can now do on-the-fly regex List ID replacement
- Increased import parsing timeout from 2 to 6 minutes per mbox file
- Private emails are now more clearly marked as such in the UI
- Logging in via OAuth now remembers where you left off
- Added support for Maildir imports
- Added three distinct Message-ID generators (short, medium, full)
- Fixed some issues with email association
- Added obfuscation mechanism to the list editor
- Added a dry-run feature to the list editor (no changes made)
- Added a single-message edit feature for the liste editor

