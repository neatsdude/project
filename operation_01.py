#!/usr/bin/python3

import os
import request
import string
import json
import mysql
import mysql.connector






#cat /var/script/Base_new.txt | while  read line

mysql.connector.connect(host = '10.110.83.20', database = 'rbt', user = 'root', password = 'onmobile')
msisdn = os.popen('cut -d, -f1 Base_new.txt').readlines()
clipid = os.popen('cut -d, -f2 Base_new.txt').readlines()

ACTIVE=`mysql -uroot -ponmobile rbt -h 10.110.83.20 -e "select count(*)
 from rbt_subscriber where subscriber_id='$MSISDN' and subscription_yes in ('B','Z','G','A','N','D','P')" | grep -v count`
if [[ "${ACTIVE}" == 0 ]]
then



url = '''http://10.110.83.20:8080/rbt/rbt_promotion.jsp?MSISDN=%s&TONE_ID=%s&REQUEST=SELECTION&SUB_TYPE=Prepaid&SELECTED_BY=CCC&CATEGORY_ID=3&ISACTIVATE=TRUE&USE_UI_CHARGE_CLASS=TRUE&SUBSCRIPTION_CLASS=DEFAULT&CHARGE_CLASS=FREE_CHURN&IN_LOOP=TRUE''' % (msisdn, clipid)



echo "$MSISDN,$CLIP_ID,$URL_RESPONCE,http://10.110.83.20:8080/rbt/rbt_promotion.jsp?MSISDN=$MSISDN&TONE_ID=$CLIP_ID&REQUEST=SELECTION&SUB_TYPE=Prepaid&SELECTED_BY=CCC&CATEGORY_ID=3&ISACTIVATE=TRUE&USE_UI_CHARGE_CLASS=TRUE&SUBSCRIPTION_CLASS=DEFAULT&CHARGE_CLASS=FREE_CHURN&IN_LOOP=TRUE"  >> /var/script/ACTIVATION_REPORT.txt
else
echo "$MSISDN,ACTIVENUMBER"  >> /var/script/ACTIVATION_REPORT.txt
fi
done



url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	})

	print 'sending username %s and password %s' % (username, password)



#-----Boiler Plate-----
if __name__=='__main__':
    main()
