"""
URL Builder for Client Details in the Meraki Dashboard
"""
import meraki
import os

class ClientDetailsURLBuilder():
    org = None
    base_url = None
    dashboard = None

    def __init__(self, api_key, network_id):
        self.network_id = network_id
        if ClientDetailsURLBuilder.dashboard == None: 
            ClientDetailsURLBuilder.dashboard = meraki.DashboardAPI(api_key=api_key, output_log=False)
        if ClientDetailsURLBuilder.org == None: 
            response = ClientDetailsURLBuilder.dashboard.organizations.getOrganizations() 
            ClientDetailsURLBuilder.org = response[0]['id'] 
        if ClientDetailsURLBuilder.base_url == None: 
            networks = ClientDetailsURLBuilder.dashboard.organizations.getOrganizationNetworks(ClientDetailsURLBuilder.org, total_pages='all') 
            found_network = next(filter(lambda d: d.get("id") == self.network_id, networks), None) 
            if found_network != None: 
                ClientDetailsURLBuilder.base_url = found_network['url'] 
    
    def get_meraki_client_id_for(self,ip):
        clients = ClientDetailsURLBuilder.dashboard.networks.getNetworkClients(self.network_id, perPage=100, total_pages='all')
        found_client = next(filter(lambda d: d.get("ip") == ip, clients), None) 
        if found_client != None:
            return found_client['id'] 
        else:
            return None

    def get_url_for(self,ip):
        meraki_client_id = self.get_meraki_client_id_for(ip)
        if meraki_client_id != None and ClientDetailsURLBuilder.base_url != None:
            url = f"{ClientDetailsURLBuilder.base_url}/overview#c={meraki_client_id}"
            return url
        else:
            return None

