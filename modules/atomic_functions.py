
from typing import Dict, Any

def get_data_features_from_config(
    config_data: Dict[str, Any],
    config_key: str = 'DATA_FEATURES'
):
    """
    function to return data features required for extraction.
    """
    data_features_config = config_data[config_key]

    return {
        "main_features": data_features_config['main_features_set'],
        'aux_features': data_features_config['aux_features_set']
    }
