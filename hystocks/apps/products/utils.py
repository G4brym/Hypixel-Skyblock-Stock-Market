def get_name_from_asset_id(asset_id):
    return str(asset_id.replace(":", "-")).replace("_", " ").capitalize()
