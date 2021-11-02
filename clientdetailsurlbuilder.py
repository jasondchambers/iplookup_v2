"""
URL Builder for Client Details in the Meraki Dashboard
"""
import meraki
import os

class ClientDetailsURLBuilder():
    org = None
    base_url = None

    def __init__(self, api_key, network_id):
        self.api_key = api_key
        self.network_id = network_id
        self.dashboard = meraki.DashboardAPI(
            api_key=api_key,
            output_log=False)
    
    def get_org(self):
        if ClientDetailsURLBuilder.org == None: 
            response = self.dashboard.organizations.getOrganizations() 
            ClientDetailsURLBuilder.org = response[0]['id'] 
        return ClientDetailsURLBuilder.org 
    
    def get_base_url(self):
        if ClientDetailsURLBuilder.base_url == None: 
            org = self.get_org() 
            networks = self.dashboard.organizations.getOrganizationNetworks(org, total_pages='all') 
            found_network = next(filter(lambda d: d.get("id") == self.network_id, networks), None) 
            if found_network != None: 
                ClientDetailsURLBuilder.base_url = found_network['url'] 
        return ClientDetailsURLBuilder.base_url
    
    def get_meraki_client_id_for(self,ip):
        clients = self.dashboard.networks.getNetworkClients(self.network_id, total_pages='all')
        found_client = next(filter(lambda d: d.get("ip") == ip, clients), None) 
        if found_client != None:
            return found_client['id'] 
        else:
            return None

    def get_url_for(self,ip):
        meraki_client_id = self.get_meraki_client_id_for(ip)
        base_url = self.get_base_url()
        if meraki_client_id != None and base_url != None:
            url = f"{base_url}/overview#c={meraki_client_id}"
            return url
        else:
            return None

