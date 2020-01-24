from active_users.keys import ActiveUserEntry

class PykafeActiveUserEntry(ActiveUserEntry):

    fields = ('service_id',) + ActiveUserEntry.fields

    @classmethod
    def create_from_request(cls, request):
        instance = super(PykafeActiveUserEntry, cls).create_from_request(request)
        instance.app_id = request.META.get('HTTP_SERVICE_ID', u'')
        return instance
