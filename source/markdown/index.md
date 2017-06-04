Apache Pony Mail (Incubating) is a web-based mail archive browser
built to scale to millions of archived messages with hundreds of requests
per second.  It allows you to browse, search, and interact with mailing lists
including creating replies to mailing list threads.

Apache Pony Mail uses OAuth2 (Google, GitHub,
Facebook etc) for authentication to allow viewing private lists, and uses
ElasticSearch for storage and searching.  Licensed under the Apache License 2.0
and undergoing Incubation at the Apache Software Foundation (ASF).

### Sample Screenshot ###
![Ponies](images/demo.png)

### Pony Mail includes rich visualizations ###

![Trends](images/demo_trends.png)

### You can also run simple n-gram analyses of list content ###

![N-grams](images/demo_ngrams.png)

See [https://lists.apache.org.org](https://lists.apache.org) for a live demo;
Pony Mail is currently running on the full mail archives of all Apache projects.

Pony Mail works in both public, private and mixed-mode, allowing you
to have one unified place for all your communication, both public and
private.


### Features include: ###

* Importing from standard mbox files, maildir directory, Pipermail or an mod_mbox-driven site
* Public and private list viewing based on auth
* Cross-list threading
* OpenSearch support for browsers (can add as search engine)
* In-browser reply to mailing lists
* Fast and intuitive searching
* Threaded, flat and tree view modes
* Notifications of replies to emails sent via Pony Mail
* Email and list statistics
* Multi-site, multi-list handling
* Word clouds
* Fuzzy-logic email grouping/threading (based in part on JWZ's ideas)
* Supports both custom OAuth, Google Auth and more.
* Atom feeds for all lists (including private ones!)
* Source view and custom range mbox export
* Customized trend analysis and n-grams


### Requirements: ###

* Linux operating system (tested on Ubuntu, Debian, Fedora and CentOS - Windows or OS/X may work)
* ElasticSearch backend
* Apache HTTP Server frontend with mod_lua loaded OR
    * Nginx with nginx-extras (ng-lua module) AND lua-apr installed
* Python 3.x for importing (with elasticsearch and formatflowed via pip)
* A mailing list system:
    * MailMan3 if you fancy that (we have a python3 archive plugin)
    * OR any mailing list system of your choice (use archiver plugin with stdin)
* Lua >=5.1 + lua-cjson, luasec and luasocket



### Development Benchmarking ###
Pony Mail has been built for and tested with the mail archives of the Apache
Software Foundation, which span more than 15 million emails sent across more
than 20 years. To put things into perspective, importing all this on a modern
machine (2xSSD with 64GB RAM) took around 12 hours and resulted in a performance
at around 100 archive search requests per second per ES node, depending on mailing
list size and available bandwidth.

### TODO: ###
This is a list of what we would love to get done:

* Start on the [project's documentation](https://github.com/apache/incubator-ponymail-site) (WIP)
* Rework JS, turn those ugly innerHTML hacks into proper DOM handling
* Set up notification system (depends on reply system) (works, but still *WIP!*)
* Have it work with ES with auth mode or via HTTPS
