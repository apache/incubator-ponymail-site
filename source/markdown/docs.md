### Getting started ###
(Optionally see the [detailed installation instructions](/docs/installing.html) for more information)

#### Supported Linux Distributions ####
For a quick guide to installing Apache Pony Mail, please see the guides for:

*  [Debian (Jessie) Installation Instructions](/docs/install.debian.html)
*  [Ubuntu (14.04) Installation Instructions](/docs/install.ubuntu.html)
*  [CentOS (7.1) Installation Instructions](/docs/install.centos.html)
*  [Fedora (22) Installation Instructions](/docs/install.fedora.html)


#### Generic installation instructions ####

1. Install Apache httpd + mod_lua and the lua libs (see http://modlua.org/gs/installing if need be)
2. Install ElasticSearch
3. go to tools/ and run python setup.py - follow the instructions and enter info
4. You may need to adjust site/js/config.js
5. Add Pony Mail as an archiver for your lists. [see this doc](/docs/archiving.html).
6. import mbox data with import-mbox.py if need be (see [this doc](/docs/importing.html) for details)
7. All done :) But please see the [detailed installation instructions](/docs/installing.html) for more details

### API ###

There is a page which [describes the API](/docs/api.html)

