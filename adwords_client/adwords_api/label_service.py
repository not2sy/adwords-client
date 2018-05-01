from . import common as cm


class LabelService(cm.BaseService):
    def __init__(self, client):
        super().__init__(client, 'LabelService')

    def custom_get(self, internal_operation):
        fields = ['LabelId', 'LabelName']
        self.prepare_get()
        client_id = internal_operation.get('client_id')
        for predicate_item in internal_operation.get('predicate', []):
            self.helper.add_predicate(predicate_item['field'], predicate_item['operator'], predicate_item['values'])
        fields = set(fields).union(internal_operation.get('fields', []))
        self.helper.add_fields(*fields)
        return self.get(client_id)
