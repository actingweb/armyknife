=========
CHANGELOG
=========

Nov 6, 2021
-----------
- Fix stripe key error in from
- Add support for beta and paid flags in featureToggles to avoid disabling
- Assorted linting
- Add support for admin /set_toggles command
- Improve formatting of admin /account command

Apr 24, 2021
------------
- Update to actingweb 2.4.5 and latest libs
- Upgrade serverless and update serverless.yml
- Upgrade to python3.7

Apr 14, 2020
------------
- Add Stripe payment support

Jan 29, 2019
------------
- Improve fargate detection code, add fargate_disabled(), add default debug logging
- Fix handling of account creation and compare just lower() of emails
- Add admin /imp command: /imp <email> /command (only /me supported now)
- Add fargate to /deletemember and add a new /fargate command to force using fargate
- Use new 2.5.1 of actingweb lib

Nov 23, 2018
------------
- New version of actingweb, move to python3
- Support lambda and fargate
- Add /app and /noapp to support apps.actingweb.io apps
- Fix box bug when box folder does not exist and service is removed
- Support actingweb 2.5.0 with actor.store and actor.property

May 17, 2018
------------
- Add support for /deletemember <email> FORCE count to remove user from all shared rooms

May 5, 2018
------------
- Fix bug in /todo and /topofmind where items with " would make the list impossible to load (json error)

Apr 29, 2018
------------
- Re-branded from Cisco Webex Teams to just Army Knife

Apr 22, 2018
------------
- Added notification invalid token in retrieval of message to catch apparently valid tokens that are not

Apr 21, 2018
------------
- Rebranded from Spark to Cisco Webex Teams
- Improved visuals on welcome page
- Added disabling of notifications when app is in /disable

Feb 7, 2018
------------
- Add /team link team_name to link team_name to the always current members of the room

Jan 30, 2018
------------
- Add support for /topofmind reminder on HH:MM to explicitly set the UTC time for the reminder
- Add new /todo command with aliases /followup and /fu with reminder support
- Add support for hidden /me full command

Jan 16, 2018
------------
- Full update to support new actingweb 2.3.0 API
- Many smaller tweaks to texts and responses to improve user experience
- Renaming /myurl to /me and update with more info, both from Army Knife account and from Cisco Webex Teams account
- Automatically print out new top of mind list after a change
- Cleaned up messaging to always use bot as sender unless there is a need to send a message into a non-bot room
- Added a series of tests to as early as possible drop messages that should not be processed
- Added support for more than 100 members in /listroom, /copyroom, and /team commands
- Fixed bug in /cleanwebhooks command that disabled the bot


Dec 16, 2017
------------

- Lots of changes, ready for production?

Nov 29, 2017
-----------

- Forked from actingwebdemo app for aws


