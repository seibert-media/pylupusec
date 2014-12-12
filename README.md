pylupusec
=========
Python lib to control [Lupusecs' Alarm systems](http://www.lupus-electronics.de/LUPUSEC-IP-Alarmanlage).

## usage

create api object:

    >>> from pylupusec import LupusecAPI
    >>> l=LupusecAPI("10.1.123.123", "admin", "admin1234")

list areas of alarm system:

    >>> l.arealist()
    {u'arearows': {u'1': u'1', u'2': u'2'}}

arm and disarm specific area of alarm system:

    >>> l.arm_area(1)
    True
    >>> l.disarm_area(1)
    True

arm and disarm all areas:

    >>> l.arm_allareas()
    True
    >>> l.disarm_allareas()
    True

get list of all registered devices:

    >>> l.devicelist()
		{
		  u'senrows': [
		    {
		      u'status': u'', 
		      u'resp_mode': [0, 5, 0, 0, 0, 0], 
		      u'status_ex': u'0', 
		      u'name': u'Bewegung 1', 
		      u'zone': 3, 
		      u'area': 1, 
		      u'battery': u'', 
		      u'tamper': u'', 
		      u'cond_ok': u'1', 
		      u'sid': u'RF:07fc0130', 
		      u'su': 1, 
		      u'cond': u'', 
		      u'bypass': u'{WEB_MSG_NO}', 
		      u'tamper_ok': u'1', 
		      u'rssi': u'{WEB_MSG_STRONG}9', 
		      u'alarm_status': u'', 
		      u'is_motionsensor': True, 
		      u'type': 9, 
		      u'battery_ok': u'1', 
		      u'type_f': u'{D_TYPE_9}'
		    }, 
		    {
		      u'status': u'{WEB_MSG_DC_CLOSE}', 
		      u'resp_mode': [3, 1, 1, 1, 1, 0], 
		      u'is_reedswitch': True, 
		      u'status_ex': u'0', 
		      u'name': u'Aufenthalt2', 
		      u'zone': 2, 
		      u'area': 1, 
		      u'battery': u'', 
		      u'tamper': u'{WEB_MSG_TAMPER}', 
		      u'cond_ok': u'1', 
		      u'sid': u'RF:2eaaa110', 
		      u'su': 1, 
		      u'is_alarm': False, 
		      u'cond': u'', 
		      u'bypass': u'{WEB_MSG_NO}', 
		      u'tamper_ok': u'0', 
		      u'rssi': u'{WEB_MSG_STRONG}6', 
		      u'alarm_status': u'', 
		      u'type': 4, 
		      u'battery_ok': u'1', 
		      u'type_f': u'{D_TYPE_4}'
		    }
		  ]
		}
