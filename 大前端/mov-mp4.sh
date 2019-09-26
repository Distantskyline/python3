#!/usr/bin/env bash
#
#
#
pgerp ffmpeg
if [ $(echo $?) -eq 1 ];then
    yum install epel-release
    rpm -v --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
    rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
    yum install ffmpeg ffmpeg-devel
fi

#SOURCE=/tmp/SourceVideo
SOURCE=/root
TARGET=/root/mp4

#mkkdir -p SOURCE

cd /

find $SOURCE -iname *.mov > /root/mov.txt

File=$(tail -1 /root/mov.txt)

ffmpeg -i $File $TARGET $File.mp4
rm -rf $File



