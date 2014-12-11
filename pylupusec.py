import json
import string
import requests


class LupusecAPI():
    """Interface to Lupusec Webservices."""
    type_mapping = {
        '{D_TYPE_4}': "is_reedswitch",
        '{D_TYPE_9}': "is_motionsensor",
    }

    def __init__(self, hostname, username, password):
        """LupsecAPI constructor requires hostname and credentials to the
         Lupusec Webinterface.
        """
        self.s = requests.Session()
        self.s.auth = (username, password)
        self.api_url = "http://{}/action/".format(hostname)

    def _apiget(self, action):
        return self.s.get(self.api_url + action)

    def _apipost(self, action, params={}):
        return self.s.post(self.api_url + action, data=params)

    def _cleaned_json(self, textdata):
        filtered_response = filter(
            lambda x: x in string.printable and x != "\t", textdata
        )
        return json.loads(filtered_response)

    def devicelist(self):
        response = self._apiget("deviceListGet")
        device_data = self._cleaned_json(response.text)

        for row in device_data['senrows']:
            key = LupusecAPI.type_mapping.get(row['type_f'], "is_unknown")
            row[key] = True

            if row.get('is_reedswitch', False):
                row['is_alarm'] = row['status'] == "{WEB_MSG_DC_OPEN}"

        return device_data

    def arealist(self):
        return self._apiget("areaListGet").json()

    def _mode_area(self, area, mode):
        r = self._apipost(
            "panelCondPost",
            {
                'area': area,
                'mode': mode,
            }
        )
        response_json = self._cleaned_json(r.text)
        return response_json.get('message', None) == "{WEB_MSG_SUBMIT_SUCCESS}"

    def arm_area(self, area):
        return self._mode_area(area, 1)

    def disarm_area(self, area):
        return self._mode_area(area, 0)

    def for_allareas(self, func):
        success = True
        for area in self.arealist()['arearows']:
            success = success and func(area)
        return success

    def arm_allareas(self):
        return self.for_allareas(self.arm_area)

    def disarm_allareas(self):
        return self.for_allareas(self.disarm_area)
