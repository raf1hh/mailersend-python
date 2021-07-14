import requests
from mailersend.endpoints import base


class NewActivity(base.NewAPIClient):
    def __init__(self):
        baseObj = base.NewAPIClient()
        super(NewActivity, self).__init__(
            baseObj.api_base,
            baseObj.headers_default,
            baseObj.headers_auth,
            baseObj.mailersend_api_key,
        )

    def getActivityByDate(self, domainId, dateFrom, dateTo, groupBy, event):
        self.domainId = domainId
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.groupBy = groupBy
        self.event = event

        _data = {
            "date_from": dateFrom,
            "date_to": dateTo,
            "event": event,
        }

        if domainId is not None:
            _data["domain_id"] = domainId

        if groupBy is not None:
            _data["group_by"] = groupBy

        request = requests.get(
            f"{self.api_base}/analytics/date", headers=self.headers_default, json=_data
        )

        return request.text

    def getDomainActivity(
        self, domainId, page=None, limit=None, dateFrom=None, dateTo=None, event=None
    ):
        self.domainId = domainId
        self.page = page
        self.limit = limit
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.event = event

        _data = {
            "page": page or None,
            "limit": limit or None,
            "dateFrom": dateFrom or None,
            "dateTo": dateTo or None,
            "event": event or None,
        }

        request = requests.get(
            f"{self.api_base}/activity/{domainId}",
            headers=self.headers_default,
            json=_data,
        )
        return request.text
