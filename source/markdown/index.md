<img src="images/ponymail.svg" style="width: 200px; margin-left: -150px; margin-right: 20px; height: auto;" align="left"/><br/><br/>
Apache Pony Mail (Incubating) is a web-based mail archive browser
licensed under the Apache License v/2.0 and built to scale 
to millions of archived messages with hundreds of requests 
per second.

Pony Mail allows you to browse and interact with mailing lists 
using Mozilla Persona or OAuth2 (Google, GitHub, Facebook etc) for authentication.

![Ponies](images/demo.png)

![Trends](images/demo_trends.png)

![N-grams](images/demo_ngrams.png)

See [https://lists.apache.org.org](https://lists.apache.org) for a demo.

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
* Supports both custom OAuth, Google Auth, OAuth.online and Mozilla Persona
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

* Start on documentation (WIP)
* Rework JS, turn those ugly innerHTML hacks into proper DOM handling
* Set up notification system (depends on reply system) (works, but still *WIP!*)
* Have it work with ES with auth mode or via HTTPS

