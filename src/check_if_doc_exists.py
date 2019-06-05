import requests
import jsonschema
import sanic
from src.utils.config import init_config

_CONFIG = init_config()

schema = {
    'type': 'object',
    'properties': {
        'doc_id': {'type': 'string'},
        'index': {'type': 'string'},
        'es_datatype': {'type': 'string'}
    }
}


def check_if_doc_exists(params, headers):
    """
    Given
    params:
        doc_id - in format "DataSource:workspace_id:object_id"
        index - elasticsearch index to search (required)
        es_datatype - elasticsearch document data type
    """
    # verify inputs
    jsonschema.validate(instance=params, schema=schema)
    index = _CONFIG['index_prefix'] + '.' + params['index']

    resp = requests.head(
        _CONFIG['elasticsearch_url'] + '/' + index + '/' + params.get('es_datatype', 'data') + '/' + params['doc_id']
    )
    if resp.status_code == 200:
        return resp
    if resp.status_code == 404:
        raise sanic.exceptions.NotFound(f"Document with ID '{params['doc_id']}' does not exist.")
    else:
        # error we are not interested in...
        raise RuntimeError(resp.text)
