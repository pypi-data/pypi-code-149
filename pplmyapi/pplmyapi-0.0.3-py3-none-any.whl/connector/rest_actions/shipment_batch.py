import logging
from time import sleep
from pplmyapi.models.package import Package
from pplmyapi.conf import (LabelReturnChanel, LabelSettingModel, ImportStatus, LABEL_SERVICES )
import requests
import json
import base64

class RESTActionShipmentBatch:
    
    url = 'https://api.dhl.com/ecs/ppl/myapi2/shipment/batch'

    def keep_or_remove_services(self, package: Package):
        svc = package.package_services

        if svc is None or len(svc) == 0:
            return
        
        new_svc = []
        for s in svc:
            # validate service code againts LABEL_SERVICES list of enum item
            if s.get_type() in LABEL_SERVICES:
                # remove service from package
                new_svc.append(s)
        package.package_services = new_svc
        return package


    def validate_package(self, package: Package):
        return self.keep_or_remove_services(package)


    def __init__(self, 
        token: str = None,
        packages: list[Package] = [], 
        return_chanel_type: LabelReturnChanel = LabelReturnChanel.HTTP,
        return_chanel_address: str = None,
        return_chanel_format: LabelSettingModel = LabelSettingModel.PDF,
        return_chanel_dpi: int = 300,
        session = None,
    ):
        self.packages = packages
        self.return_chanel_type = return_chanel_type
        self.return_chanel_address = return_chanel_address
        self.return_chanel_format = return_chanel_format
        self.return_chanel_dpi = return_chanel_dpi
        
        for package in self.packages:
            package = self.validate_package(package)

        if token is None:
            raise Exception('Token is required')

        if session is None and token is not None:
            self.session = requests.Session()
            self.session.headers.update({'Authorization': f'Bearer {self.token}'})
        else:
            self.session = session

        self.label_settings = {
            "format": return_chanel_format.value,
            "dpi": return_chanel_dpi,
            "completeLabelSettings": {
                "isCompleteLabelRequested": True,
                "pageSize": "A4",
                "position": 1
            }
        }
        # return chanel
        if return_chanel_type != LabelReturnChanel.HTTP:
            if not return_chanel_address:
                raise Exception('return_chanel_address is required')
            self.label_settings['returnChanel'] = {
                "type": return_chanel_type.value,
                "address": return_chanel_address,
            }

    def get_labels_from_url(self, label_urls):
        # get labels for packages - call api
        labels = []
        for label_url in label_urls:
            response = self.session.get(label_url)
            if response.status_code != 200:
                raise Exception(f'Error while getting labels: {response.text}')
            labels.append(base64.b64encode(response.content).decode('utf-8'))
        return labels


    def control_parcel_status(self, response):
        # check if all parcels have Complete status
        # if not, return None
        # if yes, return list of label URLs
        waiting = False
        if 'items' in response:
            for item in response['items']:
                status = self.parse_control_parcel_status(item)
                # check if all items have Complete status
                if status == ImportStatus.ERROR:
                    continue
                if status == ImportStatus.ACCEPTED:
                    waiting = True
                if status == ImportStatus.INPROCESS:
                    waiting = True
                if status == ImportStatus.COMPLETE:
                    continue
        return waiting
    
    def parse_control_parcel_status(self, parcel):
        if parcel['importState'] == 'Error':
            return ImportStatus.ERROR
        if parcel['importState'] == 'Accepted':
            return ImportStatus.ACCEPTED
        if parcel['importState'] == 'InProcess':
            return ImportStatus.INPROCESS
        if parcel['importState'] == 'Complete':
            return ImportStatus.COMPLETE

    def parse_data(self, response):
        """
        Method used to fetch base64 encoded labels from response
        and return list of packages with their shipmentNumber and labels
        """
        label_urls = None
        if 'labelUrls' in response:
            label_urls = response['labelUrls']
        if 'completeLabel' in response:
            if 'labelUrls' in response['completeLabel']:
                label_urls = response['completeLabel']['labelUrls']
        if label_urls is None:
            raise Exception('No label URLs found in response')
        labels = self.get_labels_from_url(label_urls)
        # iterate over response, get shipmentNumber and label
        for item in response['items']:
            for package in self.packages:
                if package.reference_id == item['referenceId']:
                    package.shipment_number = item['shipmentNumber']
                    package.import_state = self.parse_control_parcel_status(item)
        
        return {
            'labels': labels,
            'packages': self.packages
        }

    def get_shipments_from_response(self, response_url):
        """
            Get shipments from async response URL
            wait until all shipments are Complete or Error
            and then return main label url, shipment label urls and shipmentNumber for each referenceId
        """
        waiting = True
        response = None
        while waiting:
            response = self.session.get(response_url)
            if response.status_code != 200:
                raise Exception(f'Error while getting shipments: {response.text}')
            response = response.json()
            logging.debug(f'Shipment status: {response}')
            # iterate over response and check if all shipments have Complete status
            # if not, return None
            # if yes, return list of label URLs

            # check if all parcels have Complete status
            # if not, continue waiting but sleep 2 seconds so that we don't spam the API
            waiting = self.control_parcel_status(response)
            if waiting:
                sleep(2)
                continue
        
        # looks like all items have Complete or Error status
        # get labels and shipmentNumbers
        return self.parse_data(response)
                
    def __call__(self):
        # POST data to the self.url
        # obtain response, get label url from response (Location header)
        # if return_chanel_type == LabelReturnChanel.HTTP:
        #   fetch label url and return base64
        # else:
        #   return response (status)

        # get labels for packages - call api

        print('packages', [package.to_json() for package in self.packages])

        response = self.session.post(
            self.url,
            json = {
                "labelSettings": self.label_settings,
                "shipments": [package.to_json() for package in self.packages],
            }
        )
        if response.status_code != 201:
            # try to get error message in response
            error = None
            try:
                error = response.json()
            except:
                raise Exception(f'Error while posting shipments: {response.text}')
            
            if 'errors' in error:
                raise Exception(f'Error while posting shipments: {error["errors"]}')
            else:
                raise Exception(f'Error while posting shipments: {error}')

        # response was success
        # get Location from headers and fetch it
        if not 'Location' in response.headers or response.headers['Location'] == '':
            raise Exception(f'Error while getting labels: Location header not found in response')

        # get parcels from response
        return self.get_shipments_from_response(response.headers['Location'])