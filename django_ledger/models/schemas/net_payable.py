"""
Django Ledger created by Miguel Sanda <msanda@arrobalytics.com>.
CopyrightÂ© EDMA Group Inc licensed under the GPLv3 Agreement.

Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
"""

SCHEMA_NET_PAYABLES_DATA = {
    'type': 'object',
    'properties': {
        'net_0': {
            'type': 'number'
        },
        'net_30': {
            'type': 'number'
        },
        'net_60': {
            'type': 'number'
        },
        'net_90': {
            'type': 'number'
        },
        'net_90+': {
            'type': 'number'
        },
    },
    'required': [
        'net_0',
        'net_30',
        'net_60',
        'net_90',
        'net_90+'
    ]
}

SCHEMA_NET_PAYABLES = {
    'type': 'object',
    'properties': {
        'entity_slug': {
            'type': 'string'
        },
        'entity_name': {
            'type': 'string'
        },
        'net_payable_data': SCHEMA_NET_PAYABLES_DATA
    }
}
