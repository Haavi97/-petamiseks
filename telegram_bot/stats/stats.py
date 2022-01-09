from utils.abi import get_json, dump_json

general = get_json('general_stats.json', script=__file__)


def register_user(kasutaja):
    current = kasutaja['username'], kasutaja['id'], kasutaja['first_name'], kasutaja['last_name']
    if current not in general['kasutajad']:
        general['kasutajad'] = general['kasutajad'] + [current]
        general['kogu_kasutajad'] = general['kogu_kasutajad'] + 1
    dump_json(general, 'general_stats.json', script=__file__)
