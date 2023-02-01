import requests


class ComputeClient:
    def __init__(self, api_key, base_url="https://api.lumaserv.com/compute"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        })


    def request(self, method, path, params={}, body={}):
        r = self.session.request(method, self.base_url + path, data=body, params=params)
        if r.status_code < 200 or (r.status_code >= 300 and r.status_code < 400):
            raise Exception("Status code is " + r.status_code + "!")
        return r.json()


    def create_ssh_key(self, body, query_params={}):
        return self.request("POST", "/ssh-keys", query_params, body)


    def get_ssh_keys(self, query_params={}):
        return self.request("GET", "/ssh-keys", query_params)


    def create_server_price_range(self, body, query_params={}):
        return self.request("POST", "/server-price-ranges", query_params, body)


    def get_server_price_ranges(self, query_params={}):
        return self.request("GET", "/server-price-ranges", query_params)


    def start_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/start".format(id=id), query_params)


    def create_availability_zone(self, body, query_params={}):
        return self.request("POST", "/availability-zones", query_params, body)


    def get_availability_zones(self, query_params={}):
        return self.request("GET", "/availability-zones", query_params)


    def get_server_template(self, id, query_params={}):
        return self.request("GET", "/server-templates/{id}".format(id=id), query_params)


    def shutdown_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/shutdown".format(id=id), query_params)


    def get_server_firewall(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}".format(id=id), query_params)


    def delete_server_firewall(self, id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}".format(id=id), query_params)


    def get_server(self, id, query_params={}):
        return self.request("GET", "/servers/{id}".format(id=id), query_params)


    def delete_server(self, id, query_params={}):
        return self.request("DELETE", "/servers/{id}".format(id=id), query_params)


    def update_server(self, id, body, query_params={}):
        return self.request("PUT", "/servers/{id}".format(id=id), query_params, body)


    def get_server_actions(self, query_params={}):
        return self.request("GET", "/server-actions", query_params)


    def get_server_storage_class(self, id, query_params={}):
        return self.request("GET", "/server-storage-classes/{id}".format(id=id), query_params)


    def restart_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/restart".format(id=id), query_params)


    def mount_server_media(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/mount".format(id=id), query_params, body)


    def unmount_server_media(self, id, query_params={}):
        return self.request("DELETE", "/servers/{id}/mount".format(id=id), query_params)


    def restore_server(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/restore".format(id=id), query_params, body)


    def get_server_graph(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/graph".format(id=id), query_params)


    def recreate_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/recreate".format(id=id), query_params)


    def create_server_firewall(self, body, query_params={}):
        return self.request("POST", "/server-firewalls", query_params, body)


    def get_server_firewalls(self, query_params={}):
        return self.request("GET", "/server-firewalls", query_params)


    def get_server_firewall_rule(self, id, rule_id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), query_params)


    def delete_server_firewall_rule(self, id, rule_id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), query_params)


    def update_server_firewall_rule(self, id, rule_id, body, query_params={}):
        return self.request("PUT", "/server-firewalls/{id}/rules/{rule_id}".format(id=id, rule_id=rule_id), query_params, body)


    def create_server_host(self, body, query_params={}):
        return self.request("POST", "/server-hosts", query_params, body)


    def get_server_hosts(self, query_params={}):
        return self.request("GET", "/server-hosts", query_params)


    def create_server(self, body, query_params={}):
        return self.request("POST", "/servers", query_params, body)


    def get_servers(self, query_params={}):
        return self.request("GET", "/servers", query_params)


    def delete_server_network(self, id, network_id, query_params={}):
        return self.request("DELETE", "/servers/{id}/networks/{network_id}".format(id=id, network_id=network_id), query_params)


    def get_availability_zone(self, id, query_params={}):
        return self.request("GET", "/availability-zones/{id}".format(id=id), query_params)


    def update_availability_zone(self, id, body, query_params={}):
        return self.request("PUT", "/availability-zones/{id}".format(id=id), query_params, body)


    def create_server_backup(self, body, query_params={}):
        return self.request("POST", "/server-backups", query_params, body)


    def get_server_backups(self, query_params={}):
        return self.request("GET", "/server-backups", query_params)


    def create_subnet(self, body, query_params={}):
        return self.request("POST", "/subnets", query_params, body)


    def get_subnets(self, query_params={}):
        return self.request("GET", "/subnets", query_params)


    def create_server_volume(self, body, query_params={}):
        return self.request("POST", "/server-volumes", query_params, body)


    def get_server_volumes(self, query_params={}):
        return self.request("GET", "/server-volumes", query_params)


    def create_server_storage_class(self, body, query_params={}):
        return self.request("POST", "/server-storage-classes", query_params, body)


    def get_server_storage_classes(self, query_params={}):
        return self.request("GET", "/server-storage-classes", query_params)


    def get_server_firewall_member(self, id, member_id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), query_params)


    def delete_server_firewall_member(self, id, member_id, query_params={}):
        return self.request("DELETE", "/server-firewalls/{id}/members/{member_id}".format(id=id, member_id=member_id), query_params)


    def search(self, query_params={}):
        return self.request("GET", "/search", query_params)


    def get_scheduled_server_action(self, id, action_id, query_params={}):
        return self.request("GET", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), query_params)


    def delete_scheduled_server_action(self, id, action_id, query_params={}):
        return self.request("DELETE", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), query_params)


    def update_scheduled_server_action(self, id, action_id, body, query_params={}):
        return self.request("PUT", "/servers/{id}/scheduled-actions/{action_id}".format(id=id, action_id=action_id), query_params, body)


    def create_s3_bucket(self, body, query_params={}):
        return self.request("POST", "/storage/s3/buckets", query_params, body)


    def get_s3_buckets(self, query_params={}):
        return self.request("GET", "/storage/s3/buckets", query_params)


    def get_server_status(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/status".format(id=id), query_params)


    def create_server_firewall_member(self, id, body, query_params={}):
        return self.request("POST", "/server-firewalls/{id}/members".format(id=id), query_params, body)


    def get_server_firewall_members(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/members".format(id=id), query_params)


    def get_server_price_range(self, id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}".format(id=id), query_params)


    def get_server_action(self, id, query_params={}):
        return self.request("GET", "/server-actions/{id}".format(id=id), query_params)


    def get_server_variant_price(self, id, variant_id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params)


    def delete_server_variant_price(self, id, variant_id, query_params={}):
        return self.request("DELETE", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params)


    def update_server_variant_price(self, id, variant_id, body, query_params={}):
        return self.request("PUT", "/server-price-ranges/{id}/variant-prices/{variant_id}".format(id=id, variant_id=variant_id), query_params, body)


    def create_server_template(self, body, query_params={}):
        return self.request("POST", "/server-templates", query_params, body)


    def get_server_templates(self, query_params={}):
        return self.request("GET", "/server-templates", query_params)


    def get_server_host(self, id, query_params={}):
        return self.request("GET", "/server-hosts/{id}".format(id=id), query_params)


    def update_server_host(self, id, body, query_params={}):
        return self.request("PUT", "/server-hosts/{id}".format(id=id), query_params, body)


    def create_server_firewall_rule(self, id, body, query_params={}):
        return self.request("POST", "/server-firewalls/{id}/rules".format(id=id), query_params, body)


    def get_server_firewall_rules(self, id, query_params={}):
        return self.request("GET", "/server-firewalls/{id}/rules".format(id=id), query_params)


    def create_scheduled_server_action(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/scheduled-actions".format(id=id), query_params, body)


    def get_scheduled_server_actions(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/scheduled-actions".format(id=id), query_params)


    def stop_server(self, id, query_params={}):
        return self.request("POST", "/servers/{id}/stop".format(id=id), query_params)


    def get_server_volume(self, id, query_params={}):
        return self.request("GET", "/server-volumes/{id}".format(id=id), query_params)


    def delete_server_volume(self, id, query_params={}):
        return self.request("DELETE", "/server-volumes/{id}".format(id=id), query_params)


    def update_server_volume(self, id, body, query_params={}):
        return self.request("PUT", "/server-volumes/{id}".format(id=id), query_params, body)


    def create_server_network(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/networks".format(id=id), query_params, body)


    def get_server_networks(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/networks".format(id=id), query_params)


    def create_server_variant(self, body, query_params={}):
        return self.request("POST", "/server-variants", query_params, body)


    def get_server_variants(self, query_params={}):
        return self.request("GET", "/server-variants", query_params)


    def get_server_storage(self, id, query_params={}):
        return self.request("GET", "/server-storages/{id}".format(id=id), query_params)


    def get_ssh_key(self, id, query_params={}):
        return self.request("GET", "/ssh-keys/{id}".format(id=id), query_params)


    def delete_ssh_key(self, id, query_params={}):
        return self.request("DELETE", "/ssh-keys/{id}".format(id=id), query_params)


    def update_ssh_key(self, id, body, query_params={}):
        return self.request("PUT", "/ssh-keys/{id}".format(id=id), query_params, body)


    def create_server_price_range_assignment(self, body, query_params={}):
        return self.request("POST", "/server-price-range-assignments", query_params, body)


    def get_server_price_range_assignments(self, query_params={}):
        return self.request("GET", "/server-price-range-assignments", query_params)


    def get_addresses(self, query_params={}):
        return self.request("GET", "/addresses", query_params)


    def get_server_variant(self, id, query_params={}):
        return self.request("GET", "/server-variants/{id}".format(id=id), query_params)


    def delete_server_variant(self, id, query_params={}):
        return self.request("DELETE", "/server-variants/{id}".format(id=id), query_params)


    def delete_s3_access_key_grant(self, access_key_id, id, query_params={}):
        return self.request("DELETE", "/storage/s3/access-keys/{access_key_id}/grants/{id}".format(access_key_id=access_key_id, id=id), query_params)


    def create_server_media(self, body, query_params={}):
        return self.request("POST", "/server-medias", query_params, body)


    def get_server_medias(self, query_params={}):
        return self.request("GET", "/server-medias", query_params)


    def get_subnet(self, id, query_params={}):
        return self.request("GET", "/subnets/{id}".format(id=id), query_params)


    def delete_subnet(self, id, query_params={}):
        return self.request("DELETE", "/subnets/{id}".format(id=id), query_params)


    def attach_server_volume(self, id, body, query_params={}):
        return self.request("POST", "/server-volumes/{id}/attach".format(id=id), query_params, body)


    def get_s3_access_key(self, id, query_params={}):
        return self.request("GET", "/storage/s3/access-keys/{id}".format(id=id), query_params)


    def delete_s3_access_key(self, id, query_params={}):
        return self.request("DELETE", "/storage/s3/access-keys/{id}".format(id=id), query_params)


    def create_s3_access_key(self, body, query_params={}):
        return self.request("POST", "/storage/s3/access-keys", query_params, body)


    def get_s3_access_keys(self, query_params={}):
        return self.request("GET", "/storage/s3/access-keys", query_params)


    def get_address(self, id, query_params={}):
        return self.request("GET", "/addresses/{id}".format(id=id), query_params)


    def get_server_backup(self, id, query_params={}):
        return self.request("GET", "/server-backups/{id}".format(id=id), query_params)


    def delete_server_backup(self, id, query_params={}):
        return self.request("DELETE", "/server-backups/{id}".format(id=id), query_params)


    def update_server_backup(self, id, body, query_params={}):
        return self.request("PUT", "/server-backups/{id}".format(id=id), query_params, body)


    def create_network(self, body, query_params={}):
        return self.request("POST", "/networks", query_params, body)


    def get_networks(self, query_params={}):
        return self.request("GET", "/networks", query_params)


    def create_server_storage(self, body, query_params={}):
        return self.request("POST", "/server-storages", query_params, body)


    def get_server_storages(self, query_params={}):
        return self.request("GET", "/server-storages", query_params)


    def resize_server(self, id, body, query_params={}):
        return self.request("POST", "/servers/{id}/resize".format(id=id), query_params, body)


    def get_server_media(self, id, query_params={}):
        return self.request("GET", "/server-medias/{id}".format(id=id), query_params)


    def delete_server_media(self, id, query_params={}):
        return self.request("DELETE", "/server-medias/{id}".format(id=id), query_params)


    def create_s3_access_key_grant(self, access_key_id, body, query_params={}):
        return self.request("POST", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), query_params, body)


    def get_s3_access_key_grants(self, access_key_id, query_params={}):
        return self.request("GET", "/storage/s3/access-keys/{access_key_id}/grants".format(access_key_id=access_key_id), query_params)


    def get_server_price_range_assignment(self, id, query_params={}):
        return self.request("GET", "/server-price-range-assignments/{id}".format(id=id), query_params)


    def delete_server_price_range_assignment(self, id, query_params={}):
        return self.request("DELETE", "/server-price-range-assignments/{id}".format(id=id), query_params)


    def update_server_price_range_assignment(self, id, body, query_params={}):
        return self.request("PUT", "/server-price-range-assignments/{id}".format(id=id), query_params, body)


    def get_server_vnc(self, id, query_params={}):
        return self.request("GET", "/servers/{id}/vnc".format(id=id), query_params)


    def cancel_server_action(self, id, query_params={}):
        return self.request("POST", "/server-actions/{id}/cancel".format(id=id), query_params)


    def get_network(self, id, query_params={}):
        return self.request("GET", "/networks/{id}".format(id=id), query_params)


    def update_network(self, id, body, query_params={}):
        return self.request("PUT", "/networks/{id}".format(id=id), query_params, body)


    def get_labels(self, query_params={}):
        return self.request("GET", "/labels", query_params)


    def resize_server_volume(self, id, body, query_params={}):
        return self.request("POST", "/server-volumes/{id}/resize".format(id=id), query_params, body)


    def get_s3_bucket(self, id, query_params={}):
        return self.request("GET", "/storage/s3/buckets/{id}".format(id=id), query_params)


    def delete_s3_bucket(self, id, query_params={}):
        return self.request("DELETE", "/storage/s3/buckets/{id}".format(id=id), query_params)


    def detach_server_volume(self, id, query_params={}):
        return self.request("POST", "/server-volumes/{id}/detach".format(id=id), query_params)


    def create_server_variant_price(self, id, body, query_params={}):
        return self.request("POST", "/server-price-ranges/{id}/variant-prices".format(id=id), query_params, body)


    def get_server_variant_prices(self, id, query_params={}):
        return self.request("GET", "/server-price-ranges/{id}/variant-prices".format(id=id), query_params)


