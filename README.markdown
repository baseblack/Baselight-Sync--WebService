Baselight-Sync: Webservice
==========================

I got infuriated needing to either use the Baselight file transfer ui, or fl-cp
to copy files onto the Baselight's local filesystem.

So I decided to throw together this webservice.

Usage, run the webservice and expose it on your baselight. Then access it via
a simple http call:

http://baselight-1/?/path/to/the/frames/on/shared/storage

The service clomps off the first bit of the path "/mnt/muxfs" which in my case it the mount point
for the shared storage and sticks the local path /mnt/disk1/images1 in its place.

The two are then passed to fl-cp with the -sync command and it does it mojo.

