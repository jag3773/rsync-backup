#!/usr/bin/env python
# -*- coding: utf8 -*-

#Copyright (c) 2010 Jesse Griffin
#http://creativecommons.org/licenses/MIT/
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import os, time, restformat

#Variables
backupruntime = time.strftime("%Y %b %d %T")
backuplogfile = '/opt/backup/backuplogs/rsync-backup-' + time.strftime("%y-%b",) + '.log'
sourcedir = "/home/jkag/"
backupdir = "/opt/backup/jkag"
incrementsdir = '/opt/backup/increments/' + backupruntime
mystats = ''

#Mount drive as rw
os.system('mount -o remount,rw /opt/backup')
time.sleep(2)

#Logging
backuplog = open(backuplogfile, 'a')
print >> backuplog, (restformat.title(backupruntime))
print >> backuplog, ('Making increments directory: "' + incrementsdir + '"\n')

#Make incrementsdir
os.mkdir(incrementsdir)

#Logging
print >> backuplog, (restformat.subtitle('BEGIN BACKUP'))
backuplog.close()

#Run rsync backup command using increment directories
os.system('rsync -avbxth --delete --exclude ".mozilla/firefox-3.5" --exclude ".gvfs" --exclude ".cache" --exclude ".thumbnails" --exclude ".local/share/Trash" --backup-dir=' + '"' + incrementsdir + '" ' + sourcedir + ' ' + backupdir + ' >> ' + backuplogfile)

#Logging
backuplog = open(backuplogfile, 'a')
print >> backuplog, (restformat.subtitle('END BACKUP'))
print >> backuplog, ('\n\n')
backuplog.close()
os.system('du -hs "' + incrementsdir + '" >> /opt/backup/quickstats')

#Mount drive as read only
time.sleep(5)
os.system('mount -o remount,ro /opt/backup')
