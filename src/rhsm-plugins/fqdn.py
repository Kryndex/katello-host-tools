import socket

from subscription_manager.base_plugin import SubManPlugin

requires_api_version = "1.0"

class FactsPlugin(SubManPlugin):
    name = 'fqdn fact'

    def post_facts_collection_hook(self, conduit):
        if not conduit.facts.has_key('network.fqdn'):
            conduit.facts['network.fqdn'] = socket.getfqdn()

