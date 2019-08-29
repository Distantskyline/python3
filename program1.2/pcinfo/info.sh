#!/usr/bin/env bash



US = $(vmstat | awk 'BEGIN{ FS ==" "}NR==3{print $13}')
SY = $(vmstat | awk 'BEGIN{ FS ==" "}NR==3{print $14}')
USE = $(free -mw | awk 'BEGIN{ FS ==" "}NR==2{print $3}')
CACHE = $(free -mw | awk 'BEGIN{ FS == " "}NR==2{print $7}')
TOTAL = $(free -mw | awk 'NR==2{print $2}')
MEMRATE = $(echo "((${USE}+${CACHE})/${TOTAL})*100" | bc -ql)
DISKRATE = $(df -Th | awk 'BEGIN{FS == " "}NR==2{print $6}')

fileSize = $(du -sh /var/log/monitor.log | awk '{print $1}')
if [ ${fileSize} == '2M' ] ; then
  mv /var/log/monitor.{log,log.bak-$(date +%Y%m%d%H%M%S)}
  touch /var/log/monitor.log
else
  echo "$(date +%Y%m%d%H%M%S)-$(hostname)-{\'cpu\':
                        {\'user\': ${US},\'sys\': ${SY},\'rate\': ${US}+${SY}},
                                          \'memory\': {\'memrate\': ${MEMRATE}},
                                          \'disk\': {\'diskrate\': ${DISKRATE}}
                        }">>/var/log/monitor/monitor.log
fi