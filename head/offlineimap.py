#!/usr/bin/python2.2 -i

# Copyright (C) 2002 John Goerzen
# <jgoerzen@complete.org>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from imapsync import imaplib, imaputil, imapserver, repository, folder
import re
import getpass

host = raw_input('Host: ')
user = raw_input('Username: ')
passwd = getpass.getpass('Password: ')

server = imapserver.IMAPServer(user, passwd, host, ssl = 1)
imapobj = server.makeconnection()
delim, root = imaputil.imapsplit(imapobj.list('""', '""')[1][0])[1:]

repos = repository.IMAP.IMAPRepository(server)