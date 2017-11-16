#!/usr/bin/env python3
import sh
import argparse
import syslog
import sys
import datetime

#check if time to renew certificate
def check_cert_life():
	today = datetime.datetime.today().date()
	#returns: notAfter=Nov162018
	temp_date = sh.awk('{print $1,$2,$4}',sh.openssl('x509 -enddate -noout -in cert.pem'))
	temp_date = temp_date.split(' ')
	#gets rid of notafter
	tempt_date[0] = temp_date.split('=')[1]
	expirary_date = datetime.datetime.strptime(temp_date[1]+'/'+temp_date[0]+'/'+temp_date[2]
		,'%d/%b/%Y').date()
	print(expirary_date)
	#get date to replace_date
	#check if today is == or > if so return true if no return false
	result_date = expirary_date - datetime.timedelta(days=args.replace_date)


def renew_cert():


def main():
	#check is sscep is installed
	try:
		sh.sscep()
	except sh.ErrorReturnCode:
		syslog.syslog(syslog.LOG_ERR,'renew-cert.py failed: requires sscep')
		print('Install sscep package "yum install sscep"',file=sys.stderr)
		sys.exit(1)

	if check_cert_life():
		renew_cert()
	else:
		#report it as uneeded

