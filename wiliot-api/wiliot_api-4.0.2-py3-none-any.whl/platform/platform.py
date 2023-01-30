"""
  Copyright (c) 2016- 2021, Wiliot Ltd. All rights reserved.

  Redistribution and use of the Software in source and binary forms, with or without modification,
   are permitted provided that the following conditions are met:

     1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

     2. Redistributions in binary form, except as used in conjunction with
     Wiliot's Pixel in a product or a Software update for such product, must reproduce
     the above copyright notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the distribution.

     3. Neither the name nor logo of Wiliot, nor the names of the Software's contributors,
     may be used to endorse or promote products or services derived from this Software,
     without specific prior written permission.

     4. This Software, with or without modification, must only be used in conjunction
     with Wiliot's Pixel or with Wiliot's cloud service.

     5. If any Software is provided in binary form under this license, you must not
     do any of the following:
     (a) modify, adapt, translate, or create a derivative work of the Software; or
     (b) reverse engineer, decompile, disassemble, decrypt, or otherwise attempt to
     discover the source code or non-literal aspects (such as the underlying structure,
     sequence, organization, ideas, or algorithms) of the Software.

     6. If you create a derivative work and/or improvement of any Software, you hereby
     irrevocably grant each of Wiliot and its corporate affiliates a worldwide, non-exclusive,
     royalty-free, fully paid-up, perpetual, irrevocable, assignable, sublicensable
     right and license to reproduce, use, make, have made, import, distribute, sell,
     offer for sale, create derivative works of, modify, translate, publicly perform
     and display, and otherwise commercially exploit such derivative works and improvements
     (as applicable) in conjunction with Wiliot's products and services.

     7. You represent and warrant that you are not a resident of (and will not use the
     Software in) a country that the U.S. government has embargoed for use of the Software,
     nor are you named on the U.S. Treasury Department’s list of Specially Designated
     Nationals or any other applicable trade sanctioning regulations of any jurisdiction.
     You must not transfer, export, re-export, import, re-import or divert the Software
     in violation of any export or re-export control laws and regulations (such as the
     United States' ITAR, EAR, and OFAC regulations), as well as any applicable import
     and use restrictions, all as then in effect

   THIS SOFTWARE IS PROVIDED BY WILIOT "AS IS" AND "AS AVAILABLE", AND ANY EXPRESS
   OR IMPLIED WARRANTIES OR CONDITIONS, INCLUDING, BUT NOT LIMITED TO, ANY IMPLIED
   WARRANTIES OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, NONINFRINGEMENT,
   QUIET POSSESSION, FITNESS FOR A PARTICULAR PURPOSE, AND TITLE, ARE DISCLAIMED.
   IN NO EVENT SHALL WILIOT, ANY OF ITS CORPORATE AFFILIATES OR LICENSORS, AND/OR
   ANY CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
   OR CONSEQUENTIAL DAMAGES, FOR THE COST OF PROCURING SUBSTITUTE GOODS OR SERVICES,
   FOR ANY LOSS OF USE OR DATA OR BUSINESS INTERRUPTION, AND/OR FOR ANY ECONOMIC LOSS
   (SUCH AS LOST PROFITS, REVENUE, ANTICIPATED SAVINGS). THE FOREGOING SHALL APPLY:
   (A) HOWEVER CAUSED AND REGARDLESS OF THE THEORY OR BASIS LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE);
   (B) EVEN IF ANYONE IS ADVISED OF THE POSSIBILITY OF ANY DAMAGES, LOSSES, OR COSTS; AND
   (C) EVEN IF ANY REMEDY FAILS OF ITS ESSENTIAL PURPOSE.
"""
import json
from enum import Enum
from wiliot_api.api_client import Client, WiliotCloudError


class AssetNotFound(Exception):
    pass


class CategoryNotFound(Exception):
    pass


class LocationNotFound(Exception):
    pass


class ZoneNotFound(Exception):
    pass


class TagRole(Enum):
    DEFAULT = 'DEFAULT'
    REFERENCE = 'REFERENCE'


class Event(Enum):
    LOCATION = 'location'
    TEMPERATURE = 'temperature'
    ACTIVE = 'active'
    GEOLOCATION = 'geolocation'


class LocationType(Enum):
    SITE = 'SITE'
    TRANSPORTER = 'TRANSPORTER'


class ZoneAssociationType(Enum):
    BRIDGE = 'bridge'


class LocationAssociationType(Enum):
    BRIDGE = 'bridge'


class PlatformClient(Client):
    def __init__(self, api_key, owner_id, env='', log_file=None, logger_=None):
        self.client_path = "traceability/owner/{owner_id}/".format(owner_id=owner_id)
        self.owner_id = owner_id
        super().__init__(api_key=api_key, env=env, log_file=log_file, logger_=logger_)

    # Tag calls

    def get_pixels(self, limit=None, next=None):
        """
        Get an owner's pixels
        :param limit: Optional integer - limit the number of pixels to return (default: 50)
        :param next: Optional string - the page to start from (obtained from the last call to this function)
        :return: A tuple containing the list of pixels and the ID of the next page (or None if the last page was returned)
        """
        path = "tag"
        params = {
            'limit': limit,
            'next': next
        }
        res = self._get(path, params=params, override_client_path="owner/{owner_id}/".format(owner_id=self.owner_id))
        return res['data'], res.get("next", None)

    # Asset calls

    def get_assets(self):
        """
        Get all assets for a project
        :return: A list of asset dictionaries
        """
        path = "/asset"
        res = self._get(path, override_api_version="v2")
        return res["data"]

    def get_asset(self, asset_id):
        """
        Get a single assets for a project
        :param asset_id: string
        :return: a dictionary with asset properties
        :raises: An AssetNotFound exception if an asset with the
        provided ID cannot be found
        """
        path = "/asset/{}".format(asset_id)
        res = self._get(path, override_api_version="v2")
        if len(res.get('data', [])) == 0:
            raise AssetNotFound
        return res.get('data', [])

    def create_asset(self,
                     name, category_id, asset_id=None,
                     pixels=[], status=None):
        """
        Create an asset, and optionally assign pixels
        :param name: String - required - A name for the asset (required)
        :param category_id: String - required - the type of asset
        :param asset_id: String - optional. If not provided an asset ID will be generated automatically
        :param pixels: List - optional - of dictionaries for asset pixels. Each item should be a dictionary with the
        following keys:
         > tagId: string
         > role: Enum: TagRole
        :param status: String - optional - A status
        :return: The created asset if successful
        """
        assert isinstance(pixels, list), "Expecting a list of strings for pixels_ids"
        path = "/asset"
        payload = {
            "id": asset_id,
            "name": name,
            "categoryId": category_id,
            "tags": [{
                'tagId': t['tagId'],
                'role': t['role'].value
            } for t in pixels],
            "status": status
        }
        try:
            res = self._post(path, payload, override_api_version="v2")
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create asset")
            raise e

    def update_asset(self, asset):
        """
        Update an asset. The following asset properties can be updated:
        * Category
        * Name
        :param asset: Dictionary describing the new asset properties
        :return: The updated asset if successful
        """
        path = "/asset/{}".format(asset["id"])
        payload = {
            "name": asset["name"],
            "categoryId": asset.get("assetTypeId", None),
            "status": asset.get("status", None)
        }
        try:
            res = self._put(path, payload, override_api_version="v2")
            return res['data']
        except WiliotCloudError as e:
            print("Failed to update asset")
            raise e

    def delete_asset(self, asset_id):
        """
        Delete an asset by its ID
        :param asset_id: String - required - the ID of the asset to delete
        :return: True if the asset was deleted
        """
        path = "/asset/{}".format(asset_id)
        try:
            res = self._delete(path, override_api_version="v2")
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete asset")
            raise e
        
    def associate_pixel_to_asset(self, asset_id, pixel_id):
        """
        Associate a pixel to an existing asset
        :param asset_id: String - required - the ID of the asset to associate the pixel with
        :param pixel_id: String - required - the ID of the pixel to associate with the asset
        :return: True if association was successful.
        """
        path = f"asset/{asset_id}/tag/{pixel_id}"
        try:
            res = self._post(path, payload={}, override_api_version="v2")
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to associate pixel to asset")
            raise e

    def disassociate_pixel_from_asset(self, asset_id, pixel_id):
        """
        Disassociate a pixel from an asset
        :param asset_id: String - required - the ID of the asset to disassociate the pixel from
        :param pixel_id: String - required - the ID of the pixel to disassociate from the asset
        :return: True if disassociation was successful.
        """
        path = f"asset/{asset_id}/tag/{pixel_id}"
        try:
            res = self._delete(path, payload={}, override_api_version="v2")
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to associate pixel to asset")
            raise e

    # Asset Label calls

    # def get_asset_labels(self, project_id, asset_id):
    #     """
    #     Get all labels for an asset by its ID
    #     :param project_id:
    #     :param asset_id:
    #     :return: list of labels
    #     """
    #     path = "/project/{}/asset/{}/label".format(project_id, asset_id)
    #     res = self._get(path)
    #     return res.get("data", [])
    #
    # def create_asset_label(self, project_id, asset_id, label):
    #     """
    #     Create a label for an asset
    #     :param project_id: String - required
    #     :param asset_id: String - required - the asset to create the label for
    #     :param label: String - the label to create
    #     :return: True if label created
    #     """
    #     path = "/project/{}/asset/{}/label".format(project_id, asset_id)
    #     payload = {"label": label}
    #     res = self._post(path, payload)
    #     return res
    #
    # def delete_asset_labels(self, project_id, asset_id):
    #     """
    #     Create all labels for an asset identified by an ID
    #     :param project_id: String - required
    #     :param asset_id: String - required - The ID of the asset for which labels should be deleted
    #     :return: True if successful
    #     """
    #     path = "/project/{}/asset/{}/label".format(project_id, asset_id)
    #     try:
    #         res = self._delete(path)
    #         return res['message'].lower().find("success") != -1
    #     except WiliotCloudError as e:
    #         print("Failed to delete POI label")
    #         raise e
    #
    # def delete_asset_label(self, project_id, asset_id, label):
    #     """
    #     Create all labels for an asset identified by an ID
    #     :param project_id: String - required
    #     :param asset_id: String - required - The ID of the asset for which labels should be deleted
    #     :return: True if successful
    #     """
    #     path = "/project/{}/asset/{}/label/{}".format(project_id, asset_id, label)
    #     try:
    #         res = self._delete(path)
    #         return res['message'].lower().find("success") != -1
    #     except WiliotCloudError as e:
    #         print("Failed to delete POI label")
    #         raise e

    # Category calls

    def get_categories(self):
        """
        Get all asset categories
        :return: a list of dictionaries with categories
        """
        path = "/category"
        res = self._get(path)
        return res.get('data', [])

    def get_category(self, category_id):
        """
        Get a single asset type for a project
        :param category_id: string
        :return: a dictionary with asset type properties
        :raises: An AssetTypeNotFound exception if an asset with the
        provided ID cannot be found
        """
        path = "/asset/type/{}".format(category_id)
        res = self._get(path)
        if len(res.get('data', [])) == 0:
            raise CategoryNotFound
        return res.get('data', [])

    def create_category(self, name, asset_type_id, events, category_id=None, sku=None, description=None):
        """
        Create a category
        :param name: String - required - A unique name for the category
        :param asset_type_id: Int - required - the base asset type for this category (obtained from the list of
        available asset types)
        :param events: List of EVENTS to enable for assets of this category
        :param category_id: String - optional - If not provided an asset ID will be generated automatically
        :param sku: String - optional - A SKU/UPC to link the category to
        :param description: String - optional - A description for the category
        :return: The created asset if successful
        """
        # Make sure events is a list of Events
        assert isinstance(events, list) and all(isinstance(element, Event) for element in events), "events argument must be a list of Event(s)"
        path = "/category"
        payload = {
            "assetType": {
                "events": [
                    {
                        "selected": True,
                        "eventName": e.value
                    } for e in events
                ],
                "id": asset_type_id
            },
            "id": category_id,
            "name": name,
            "description": description,
            "sku_upc": sku
        }
        print(payload)
        print(json.dumps(payload, indent=2))
        try:
            res = self._post(path, payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create category")
            raise e

    def update_category(self, category):
        """
        Update a category
        :param category: Dictionary describing the category
        :return: The updated category if successful
        """
        path = "/asset/type/{}".format(category['id'])
        try:
            res = self._put(path, category)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to update asset type")
            raise e

    def delete_category(self, category_id):
        """
        Delete a category by its ID
        :param category_id: String - required - the ID of the category to delete
        :return: True if the asset was deleted
        """
        path = "/category/{}".format(category_id)
        try:
            res = self._delete(path)
            print(res['message'])
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete category")
            raise e

    # Asset types
    def get_asset_types(self):
        """
        Get all asset types
        :return: a list of dictionaries with asset types
        """
        path = "/asset-type"
        res = self._get(path)
        return res.get('data', [])

    # Locations
    def get_locations(self):
        """
        Get all locations
        :return: A list of dictionaries representing locations
        """
        path = "/location"
        res = self._get(path)
        return res.get('data', [])

    def get_location(self, location_id):
        """
        Get one location
        :param location_id: String - required - the ID of the location to return
        :return: A dictionary representing the location
        :raise: A LocationNotFound if a location with the provided ID does not exist
        """
        path = f"/location/{location_id}"
        res = self._get(path)
        if len(res.get('data', [])) == 0:
            raise LocationNotFound
        return res.get('data', [])

    def create_location(self, location_type, name=None, location_id=None, lat=None, lng=None,
                        address=None, city=None, country=None):
        """
        Create a new location
        :param location_type: LocationType Enum - Required - the type of location
        :param name: String - optional - A name for the location
        :param location_id: String - optional - A unique ID for the new location. A unique ID will be auto generated
        if one is not provided
        :param lat: Float - Optional - The latitude value for the location - required only for location type SITE
        :param lng: Float - Optional - The longitude value for the location - required only for location type SITE
        :param address: String - Optional - A street address for the location
        :param city: String - Optional - The location's city
        :param country: String - Optional - the location's country
        :return: The created location if successful
        """
        path = "/location"
        payload = {
            'locationType': location_type.value,
            'id': location_id,
            'name': name,
            'lat': lat,
            'lng': lng,
            'address': address,
            'city': city,
            'country': country
        }
        try:
            res = self._post(path, payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create location")
            raise e

    def update_location(self, location):
        """
        Update a location
        :param location: Dictionary - Required - The updated location dictionary. All location properties, except for
        location ID can be updated
        :return: The updated location if successful
        :raise: LocationNotFound if the requested location does not exit
        """
        path = f"/location/{location['id']}"
        payload = {
            'locationType': location['locationType'].value if isinstance(location, LocationType) else location['locationType'],
            'name': location.get('name', None),
            'lat': location.get('lat', None),
            'lng': location.get('lng', None),
            'address': location.get('address', None),
            'city': location.get('city', None),
            'country': location.get('country', None)
        }
        try:
            res = self._put(path, payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to update location")
            raise e

    def delete_location(self, location_id):
        """
        Delete a location
        :param location_id: String - Required - The ID of the location to delete
        :return: True if the location was deleted
        """
        path = f"/location/{location_id}"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete location")
            raise e

    # Associations
    def get_location_associations(self, location_id):
        """
        Get all associations for a given location
        :param location_id: String - Required - The location ID to return associations for
        :return: A list of associations
        """
        path = f"/location/{location_id}/association"
        res = self._get(path)
        return res.get('data', [])

    def create_location_association(self, location_id, association_type, association_value):
        """
        Create a new association for a location
        :param location_id: String - Required - The ID of the location to create the association for
        :param association_type: LocationAssociationType - Required - The type of association
        :param association_value: String - Required - The value of the association (the bridge ID in case of a bridge
         association)
        :return: The new association that was created
        """
        path = f"/location/{location_id}/association"
        payload = {
            'associationValue': association_value,
            'associationType': association_type.value
        }
        try:
            res = self._post(path, payload=payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create location association")
            raise e

    def delete_location_association(self, location_id, association_value):
        """
        Delete one location association
        :param location_id: String - Required - The ID of the location to delete associations for
        :param association_value: String - Required - Provide a value to delete only one association
        value.
        :return: True if successful
        """
        path = f"/location/{location_id}/association/{association_value}"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete a location association")
            raise e

    def delete_location_associations(self, location_id):
        """
        Delete all location associations
        :param location_id: String - Required - The ID of the location to delete associations for
        value.
        :return: True if successful
        """
        path = f"/location/{location_id}/association"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete location associations")
            raise e

    def get_zone_associations(self, location_id, zone_id):
        """
        Get all associations for a given zone
        :param location_id: String - Required - The location ID the zone belongs to
        :return: A list of associations
        """
        path = f"/location/{location_id}/zone/{zone_id}/association"
        res = self._get(path)
        return res.get('data', [])

    def create_zone_association(self, location_id, zone_id, association_type, association_value):
        """
        Create a new association for a location
        :param location_id: String - Required - The ID of the location to create the association for
        :param zone_id: String - Required -  The ID of the zone to create the association for
        :param association_type: ZoneAssociationType - Required - The type of association
        :param association_value: String - Required - The value of the association (bridge ID in case of bridge)
        :return: The new association that was created
        """
        path = f"/location/{location_id}/zone/{zone_id}/association"
        payload = {
            'associationValue': association_value,
            'associationType': association_type.value
        }
        try:
            res = self._post(path, payload=payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create location association")
            raise e

    def delete_zone_association(self, location_id, zone_id, association_value):
        """
        Delete one zone association
        :param location_id: String - Required - The ID of the location the zone belongs to
        :param zone_id: String - Required - The ID of the zone to delete the association from
        :param association_value: String - Required - Provide a value to delete only one association
        value.
        :return: True if successful
        """
        path = f"/location/{location_id}/zone/{zone_id}/association/{association_value}"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete a zone association")
            raise e

    def delete_zone_associations(self, location_id, zone_id):
        """
        Delete all zone associations
        :param location_id: String - Required - The ID of the location the zone belongs to
        :param zone_id: String - Required - The ID of the zone to delete the associations from
        :return: True if successful
        """
        path = f"/location/{location_id}/zone/{zone_id}/association"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete zone associations")

    # Zones
    def get_zones(self, location_id):
        """
        Get all zones under a location
        :param location_id: The ID of the location to return zones belonging to
        :return: A list of zones
        """
        path = f"/location/{location_id}/zone"
        res = self._get(path)
        return res.get('data', [])

    def get_zone(self, location_id, zone_id):
        """
        Get all zones under a location
        :param location_id: The ID of the location the zone belongs to
        :param zone_id: The ID of the zone to return
        :return: A list of zones
        :raise: A ZoneNotFound exception if a zone with the requested ID does not exist
        """
        path = f"/location/{location_id}/zone/{zone_id}"
        res = self._get(path)
        if len(res.get('data', [])) == 0:
            raise ZoneNotFound
        return res.get('data', [])

    def create_zone(self, name, location_id, zone_id=None):
        """
        Create a new zone
        :param name: String - Required - A human-readable name for the zone
        :param location_id: String - Required - The ID the zone will belong to
        :param zone_id: String - optional - The ID to give to the zone.
        If none is provided an ID will be automatically generated
        :return: The created zone
        """
        path = f"/location/{location_id}/zone"
        payload = {
            'name': name,
            'id': zone_id
        }
        try:
            res = self._post(path, payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to create zone")
            raise e

    def update_zone(self, location_id, zone):
        """
        Update a zone
        :param location_id: String - Required - The ID of the location the zone belongs to
        :param zone: Dictionary - Required - The updated zone dictionary. All location properties, except for
        zone ID can be updated
        :return: The updated zone if successful
        """
        path = f"/location/{location_id}/zone/{zone['id']}"
        payload = {
            'name': zone['name'],
            'id': zone['id'],
            'locationId': zone['locationId']
        }
        try:
            res = self._put(path, payload)
            return res['data']
        except WiliotCloudError as e:
            print("Failed to update zone")
            raise e

    def delete_zone(self, location_id, zone_id):
        """
        Delete a zone
        :param location_id: String - Required - The ID of the location the zone belongs to
        :param zone_id: String - Required - The ID of the location to delete
        :return: True if the location was deleted
        """
        path = f"/location/{location_id}/zone/{zone_id}"
        try:
            res = self._delete(path)
            return res['message'].lower().find("success") != -1
        except WiliotCloudError as e:
            print("Failed to delete zone")
            raise e
