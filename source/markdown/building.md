# Building (and releasing) Apache Pony Mail (Incubating)

Release managers wanting to initiate a release of Pony Mail should follow these steps:

Assuming you wish to release version X.Y

- Create a new branch off master called X.Y (ideally, master is always releasable).
- Tarball the branch, sans the .git directory: `git archive --format=tar.gz -o ~/ponymail-X.Y.tar.gz HEAD`
- Create checksums of the archive (make sure your PGP key is in our [KEYS](https://dist.apache.org/repos/dist/dev/incubator/ponymail/KEYS) file!):
  - Make a checksum for the archive itself: `sha256sum ponymail-X.Y.tar.gz > ponymail-X.Y.tar.gz.sha256`
  - Sign the archive: `gpg --output ponymail-X.Y.tar.gz.asc --sign ponymail-X.Y.tar.gz` OR
  - Sign the checksum: `gpg --output ponymail-X.Y.tar.gz.sha256.asc --sign ponymail-X.Y.tar.gz.sha256`
- Push the artefacts to `https://dist.apache.org/repos/dist/dev/incubator/ponymail/` via subversion
- Initate a vote on the release on dev@ponymail.a.o. To make things easier, don't bother with RC1, RC2 etc. version numbers are cheap.
- Summarize the vote on the dev list after 72 hours.
- When/If the vote passes, you can then move the artefacts to `https://dist.apache.org/repos/dist/release/incubator/ponymail/` via `svn mv`
- Announce the new release :)


