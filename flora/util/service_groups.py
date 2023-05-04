from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "flora_harvester",
        "flora_timelord_launcher",
        "flora_timelord",
        "flora_farmer",
        "flora_full_node",
        "flora_wallet",
        "flora_data_layer",
        "flora_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["flora_wallet", "flora_data_layer"],
    "data_layer_http": ["flora_data_layer_http"],
    "node": ["flora_full_node"],
    "harvester": ["flora_harvester"],
    "farmer": ["flora_harvester", "flora_farmer", "flora_full_node", "flora_wallet"],
    "farmer-no-wallet": ["flora_harvester", "flora_farmer", "flora_full_node"],
    "farmer-only": ["flora_farmer"],
    "timelord": ["flora_timelord_launcher", "flora_timelord", "flora_full_node"],
    "timelord-only": ["flora_timelord"],
    "timelord-launcher-only": ["flora_timelord_launcher"],
    "wallet": ["flora_wallet"],
    "introducer": ["flora_introducer"],
    "simulator": ["flora_full_node_simulator"],
    "crawler": ["flora_crawler"],
    "seeder": ["flora_crawler", "flora_seeder"],
    "seeder-only": ["flora_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
