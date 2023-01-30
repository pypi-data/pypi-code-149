# -*- encoding: utf-8 -*-
# FeedCrawler
# Projekt von https://github.com/rix1337
# Dieses Modul stellt die API von MyJDownloader in Form eines Python-Moduls zur Verfügung.
#
# Enthält Code von:
# https://github.com/mmarquezs/My.Jdownloader-API-Python-Library/
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Marc Marquez Santamaria
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import base64
import hashlib
import hmac
import json
import time
from urllib.error import URLError
from urllib.parse import quote

from Cryptodome.Cipher import AES

from feedcrawler.providers.http_requests.request_handler import request

BS = 16


class MYJDException(BaseException):
    pass


class TokenExpiredException(BaseException):
    pass


class RequestTimeoutException(BaseException):
    pass


def pad(s):
    return s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()


def unpad(s):
    return s[0:-s[-1]]


class System:
    """
    Class that represents the system-functionality of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = '/system'

    def exit_jd(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/exitJD")
        return resp

    def restart_jd(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/restartJD")
        return resp

    def hibernate_os(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/hibernateOS")
        return resp

    def shutdown_os(self, force):
        """

        :param force:  Force Shutdown of OS
        :return:
        """
        params = force
        resp = self.device.action(self.url + "/shutdownOS", params)
        return resp

    def standby_os(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/standbyOS")
        return resp

    def get_storage_info(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/getStorageInfos?path")
        return resp


class Update:
    """
    Class that represents the update-functionality of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = '/update'

    def restart_and_update(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/restartAndUpdate")
        return resp

    def run_update_check(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/runUpdateCheck")
        return resp

    def is_update_available(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/isUpdateAvailable")
        return resp

    def update_available(self):
        self.run_update_check()
        resp = self.is_update_available()
        return resp


class Config:
    """
    Class that represents the Config of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = '/config'

    def list(self):
        """
        :return:  List<AdvancedConfigAPIEntry>
        """
        resp = self.device.action(self.url + "/list")
        return resp

    def get(self, interface_name, storage, key):
        """
        :param interfaceName: a valid interface name from List<AdvancedConfigAPIEntry>
        :type: str:
        :param storage: 'null' to use default or 'cfg/' + interfaceName
        :type: str:
        :param key: a valid key from from List<AdvancedConfigAPIEntry>
        :type: str:
        """
        params = [interface_name, storage, key]
        resp = self.device.action(self.url + "/get", params)
        return resp

    def set(self, interface_name, storage, key, value):
        """
        :param interfaceName:  a valid interface name from List<AdvancedConfigAPIEntry>
        :type: str:
        :param storage: 'null' to use default or 'cfg/' + interfaceName
        :type: str:
        :param key: a valid key from from List<AdvancedConfigAPIEntry>
        :type: str:
        :param value: a valid value for the given key (see type value from List<AdvancedConfigAPIEntry>)
        :type: Object:
        """
        params = [interface_name, storage, key, value]
        resp = self.device.action(self.url + "/set", params)
        return resp


class DownloadController:
    """
    Class that represents the download-controller of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = '/downloadcontroller'

    def start_downloads(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/start")
        return resp

    def stop_downloads(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/stop")
        return resp

    def pause_downloads(self, value):
        """

        :param value:
        :return:
        """
        params = [value]
        resp = self.device.action(self.url + "/pause", params)
        return resp

    def get_speed_in_bytes(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/getSpeedInBps")
        return resp

    def force_download(self, link_ids, package_ids):
        """
        :param link_ids:
        :param package_ids:
        :return:
        """
        params = [link_ids, package_ids]
        resp = self.device.action(self.url + "/forceDownload", params)
        return resp

    def get_current_state(self):
        """

        :return:
        """
        resp = self.device.action(self.url + "/getCurrentState")
        return resp


class Linkgrabber:
    """
    Class that represents the linkgrabber of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = '/linkgrabberv2'

    def clear_list(self):
        """
        Clears Linkgrabbers list
        """
        resp = self.device.action(self.url + "/clearList", http_action="POST")
        return resp

    def move_to_downloadlist(self, links_ids, packages_ids):
        """
        Moves packages and/or links to download list.

        :param links_ids:
        :param packages_ids:
        :type: list of strings.
        """
        params = [links_ids, packages_ids]
        resp = self.device.action(self.url + "/moveToDownloadlist", params)
        return resp

    def query_links(self,
                    params=[{
                        "bytesTotal": True,
                        "comment": True,
                        "status": True,
                        "enabled": True,
                        "maxResults": -1,
                        "startAt": 0,
                        "hosts": True,
                        "url": True,
                        "availability": True,
                        "variantIcon": True,
                        "variantName": True,
                        "variantID": True,
                        "variants": True,
                        "priority": True
                    }]):
        """

        Get the links in the linkcollector/linkgrabber

        :param params: A dictionary with options. The default dictionary is
        configured so it returns you all the downloads with all details, but you
        can put your own with your options. All the options available are this
        ones:
        {
        "bytesTotal"    : false,
        "comment"       : false,
        "status"        : false,
        "enabled"       : false,
        "maxResults"    : -1,
        "startAt"       : 0,
        "packageUUIDs"  : null,
        "hosts"         : false,
        "url"           : false,
        "availability"  : false,
        "variantIcon"   : false,
        "variantName"   : false,
        "variantID"     : false,
        "variants"      : false,
        "priority"      : false
        }
        :type: Dictionary
        :rtype: List of dictionaries of this style, with more or less detail based on your options.

        [   {   'availability': 'ONLINE',
            'bytesTotal': 68548274,
            'enabled': True,
            'name': 'The Rick And Morty Theory - The Original        Morty_ - '
                    'Cartoon Conspiracy (Ep. 74) @ChannelFred (192kbit).m4a',
            'packageUUID': 1450430888524,
            'url': 'youtubev2://DEMUX_M4A_192_720P_V4/d1NZf1w2BxQ/',
            'uuid': 1450430889576,
            'variant': {   'id': 'DEMUX_M4A_192_720P_V4',
                        'name': '192kbit/s M4A-Audio'},
            'variants': True
            }, ... ]
        """
        resp = self.device.action(self.url + "/queryLinks", params)
        return resp

    def cleanup(self,
                action,
                mode,
                selection_type,
                links_ids=[],
                packages_ids=[]):
        """
        Clean packages and/or links of the linkgrabber list.
        Requires at least a packages_ids or links_ids list, or both.

        :param packages_ids: Packages UUID.
        :type: list of strings.
        :param links_ids: Links UUID.
        :type: list of strings
        :param action: Action to be done. Actions: DELETE_ALL, DELETE_DISABLED, DELETE_FAILED, DELETE_FINISHED, DELETE_OFFLINE, DELETE_DUPE, DELETE_MODE
        :type: str:
        :param mode: Mode to use. Modes: REMOVE_LINKS_AND_DELETE_FILES, REMOVE_LINKS_AND_RECYCLE_FILES, REMOVE_LINKS_ONLY
        :type: str:
        :param selection_type: Type of selection to use. Types: SELECTED, UNSELECTED, ALL, NONE
        :type: str:
        """
        params = [links_ids, packages_ids]
        params += [action, mode, selection_type]
        resp = self.device.action(self.url + "/cleanup", params)
        return resp

    def add_container(self, type_, content):
        """
        Adds a container to Linkgrabber.

        :param type_: Type of container.
        :type: string.
        :param content: The container.
        :type: string.

        """
        params = [type_, content]
        resp = self.device.action(self.url + "/addContainer", params)
        return resp

    def get_download_urls(self, links_ids, packages_ids, url_display_type):
        """
        Gets download urls from Linkgrabber.

        :param links_ids:
        :param packages_ids: Packages UUID.
        :type: List of strings.
        :type: List of strings
        :param url_display_type: No clue. Not documented
        :type: Dictionary
        """
        params = [packages_ids, links_ids, url_display_type]
        resp = self.device.action(self.url + "/getDownloadUrls", params)
        return resp

    def set_priority(self, priority, links_ids, packages_ids):
        """
        Sets the priority of links or packages.

        :param packages_ids: Packages UUID.
        :type: list of strings.
        :param links_ids: Links UUID.
        :type: list of strings
        :param priority: Priority to set. Priorities: HIGHEST, HIGHER, HIGH, DEFAULT, LOWER;
        :type: str:
        """
        params = [priority, links_ids, packages_ids]
        resp = self.device.action(self.url + "/setPriority", params)
        return resp

    def set_enabled(self, enable, links_ids, packages_ids):
        """
        Enable or disable packages.

        :param enable: Enable or disable package.
        :type: boolean
        :param links_ids: Links UUID.
        :type: list of strings
        :param packages_ids: Packages UUID.
        :type: list of strings.
        """
        params = [enable, links_ids, packages_ids]
        resp = self.device.action(self.url + "/setEnabled", params)
        return resp

    def get_variants(self, params):
        """
        Gets the variants of a url/download (not package), for example a youtube
        link gives you a package with three downloads, the audio, the video and
        a picture, and each of those downloads have different variants (audio
        quality, video quality, and picture quality).

        :param params: List with the UUID of the download you want the variants. Ex: [232434]
        :type: List
        :rtype: Variants in a list with dictionaries like this one: [{'id':
        'M4A_256', 'name': '256kbit/s M4A-Audio'}, {'id': 'AAC_256', 'name':
        '256kbit/s AAC-Audio'},.......]
        """
        resp = self.device.action(self.url + "/getVariants", params)
        return resp

    def add_links(self,
                  params=[{
                      "autostart": False,
                      "links": None,
                      "packageName": None,
                      "extractPassword": None,
                      "priority": "DEFAULT",
                      "downloadPassword": None,
                      "destinationFolder": None,
                      "overwritePackagizerRules": False
                  }]):
        """
        Add links to the linkcollector

        {
        "autostart" : false,
        "links" : null,
        "packageName" : null,
        "extractPassword" : null,
        "priority" : "DEFAULT",
        "downloadPassword" : null,
        "destinationFolder" : null
        }
        """
        resp = self.device.action("/linkgrabberv2/addLinks", params)
        return resp

    def get_childrenchanged(self):
        """
        no idea what parameters i have to pass and/or i don't know what it does.
        if i find out i will implement it :p
        """
        pass

    def remove_links(self, links_ids, packages_ids):
        params = [links_ids, packages_ids]
        resp = self.device.action(self.url + "/removeLinks", params)
        return resp

    def get_downfolderhistoryselectbase(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def help(self):
        """
        It returns the API help.
        """
        resp = self.device.action("/linkgrabberv2/help", http_action="GET")
        return resp

    def rename_link(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def move_links(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def move_to_new_package(self, links_ids, packages_ids, new_pkg_name, download_path):
        params = links_ids, packages_ids, new_pkg_name, download_path
        resp = self.device.action(self.url + "/movetoNewPackage", params)
        return resp

    def set_variant(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def get_package_count(self):
        resp = self.device.action("/linkgrabberv2/getPackageCount")
        return resp

    def is_collecting(self):
        resp = self.device.action("/linkgrabberv2/isCollecting")
        return resp

    def rename_package(self, package_id, new_name):
        params = package_id, new_name
        resp = self.device.action(self.url + "/renamePackage", params)
        return resp

    def query_packages(self, params=[
        {
            "availableOfflineCount": True,
            "availableOnlineCount": True,
            "availableTempUnknownCount": True,
            "availableUnknownCount": True,
            "bytesTotal": True,
            "childCount": True,
            "comment": True,
            "enabled": True,
            "hosts": True,
            "maxResults": -1,
            "packageUUIDs": [],
            "priority": True,
            "saveTo": True,
            "startAt": 0,
            "status": True
        }
    ]):
        """
        Get the links in the linkgrabber list
        """
        resp = self.device.action("/linkgrabberv2/queryPackages", params)
        return resp

    def move_packages(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def add_variant_copy(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass


class Toolbar:
    """
    Class that represents the toolbar of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = "/toolbar"

    def get_status(self):
        resp = self.device.action(self.url + "/getStatus")
        return resp

    def status_downloadspeedlimit(self):
        self.status = self.get_status()
        if self.status['limit']:
            return 1
        else:
            return 0

    def enable_downloadspeedlimit(self):
        self.limit_enabled = self.status_downloadspeedlimit()
        if not self.limit_enabled:
            self.device.action(self.url + "/toggleDownloadSpeedLimit")

    def disable_downloadspeedlimit(self):
        self.limit_enabled = self.status_downloadspeedlimit()
        if self.limit_enabled:
            self.device.action(self.url + "/toggleDownloadSpeedLimit")


class Downloads:
    """
    Class that represents the downloads list of a Device
    """

    def __init__(self, device):
        self.device = device
        self.url = "/downloadsV2"

    def query_links(self,
                    params=[{
                        "bytesTotal": True,
                        "comment": True,
                        "status": True,
                        "enabled": True,
                        "maxResults": -1,
                        "startAt": 0,
                        "packageUUIDs": [],
                        "host": True,
                        "url": True,
                        "bytesloaded": True,
                        "speed": True,
                        "eta": True,
                        "finished": True,
                        "priority": True,
                        "running": True,
                        "skipped": True,
                        "extractionStatus": True
                    }]):
        """
        Get the links in the download list
        """
        resp = self.device.action(self.url + "/queryLinks", params)
        return resp

    def query_packages(self,
                       params=[{
                           "bytesLoaded": True,
                           "bytesTotal": True,
                           "comment": True,
                           "enabled": True,
                           "eta": True,
                           "priority": True,
                           "finished": True,
                           "running": True,
                           "speed": True,
                           "status": True,
                           "childCount": True,
                           "hosts": True,
                           "saveTo": True,
                           "maxResults": -1,
                           "packageUUIDs": [],
                           "startAt": 0,
                       }]):
        """
        Get the packages in the download list
        """
        resp = self.device.action(self.url + "/queryPackages", params)
        return resp

    def cleanup(self,
                action,
                mode,
                selection_type,
                links_ids=[],
                packages_ids=[]):
        """
        Clean packages and/or links of the linkgrabber list.
        Requires at least a packages_ids or links_ids list, or both.

        :param packages_ids: Packages UUID.
        :type: list of strings.
        :param links_ids: Links UUID.
        :type: list of strings
        :param action: Action to be done. Actions: DELETE_ALL, DELETE_DISABLED, DELETE_FAILED, DELETE_FINISHED, DELETE_OFFLINE, DELETE_DUPE, DELETE_MODE
        :type: str:
        :param mode: Mode to use. Modes: REMOVE_LINKS_AND_DELETE_FILES, REMOVE_LINKS_AND_RECYCLE_FILES, REMOVE_LINKS_ONLY
        :type: str:
        :param selection_type: Type of selection to use. Types: SELECTED, UNSELECTED, ALL, NONE
        :type: str:
        """
        params = [links_ids, packages_ids]
        params += [action, mode, selection_type]
        resp = self.device.action(self.url + "/cleanup", params)
        return resp

    def set_enabled(self, enable, links_ids, packages_ids):
        """
        Enable or disable packages.

        :param enable: Enable or disable package.
        :type: boolean
        :param links_ids: Links UUID.
        :type: list of strings
        :param packages_ids: Packages UUID.
        :type: list of strings.
        """
        params = [enable, links_ids, packages_ids]
        resp = self.device.action(self.url + "/setEnabled", params)
        return resp

    def move_to_new_package(self, links_ids, packages_ids, new_pkg_name, download_path):
        params = links_ids, packages_ids, new_pkg_name, download_path
        resp = self.device.action(self.url + "/movetoNewPackage", params)
        return resp

    def remove_links(self, links_ids, packages_ids):
        params = [links_ids, packages_ids]
        resp = self.device.action(self.url + "/removeLinks", params)
        return resp

    def reset_links(self, links_ids, packages_ids):
        params = [links_ids, packages_ids]
        resp = self.device.action(self.url + "/resetLinks", params)
        return resp


class Jddevice:
    """
    Class that represents a JDownloader device and it's functions
    """

    def __init__(self, jd, device_dict):
        """ This functions initializates the device instance.
        It uses the provided dictionary to create the device.

        :param device_dict: Device dictionary
        """
        self.name = device_dict["name"]
        self.device_id = device_dict["id"]
        self.device_type = device_dict["type"]
        self.myjd = jd
        self.config = Config(self)
        self.linkgrabber = Linkgrabber(self)
        self.downloads = Downloads(self)
        self.toolbar = Toolbar(self)
        self.downloadcontroller = DownloadController(self)
        self.update = Update(self)
        self.system = System(self)
        self.__direct_connection_info = None
        self.__refresh_direct_connections()
        self.__direct_connection_enabled = True
        self.__direct_connection_cooldown = 0
        self.__direct_connection_consecutive_failures = 0

    def __refresh_direct_connections(self):
        response = self.myjd.request_api("/device/getDirectConnectionInfos",
                                         "POST", None, self.__action_url())
        if response is not None \
                and 'data' in response \
                and 'infos' in response["data"] \
                and len(response["data"]["infos"]) != 0:
            self.__update_direct_connections(response["data"]["infos"])

    def __update_direct_connections(self, direct_info):
        """
        Updates the direct_connections info keeping the order.
        """
        tmp = []
        if self.__direct_connection_info is None:
            for conn in direct_info:
                tmp.append({'conn': conn, 'cooldown': 0})
            self.__direct_connection_info = tmp
            return
        #  We remove old connections not available anymore.
        for i in self.__direct_connection_info:
            if i['conn'] not in direct_info:
                tmp.remove(i)
            else:
                direct_info.remove(i['conn'])
        # We add new connections
        for conn in direct_info:
            tmp.append({'conn': conn, 'cooldown': 0})
        self.__direct_connection_info = tmp

    def enable_direct_connection(self):
        self.__direct_connection_enabled = True
        self.__refresh_direct_connections()

    def disable_direct_connection(self):
        self.__direct_connection_enabled = False
        self.__direct_connection_info = None

    def action(self, path, params=(), http_action="POST"):
        """Execute any action in the device using the postparams and params.
        All the info of which params are required and what are they default value, type,etc
        can be found in the MY.Jdownloader API Specifications ( https://goo.gl/pkJ9d1 ).

        :param path:
        :param http_action:
        :param params: Params in the url, in a list of tuples. Example:
        /example?param1=ex&param2=ex2 [("param1","ex"),("param2","ex2")]
        """
        action_url = self.__action_url()
        if not self.__direct_connection_enabled or self.__direct_connection_info is None \
                or time.time() < self.__direct_connection_cooldown:
            # No direct connection available, we use My.JDownloader api.
            response = self.myjd.request_api(path, http_action, params,
                                             action_url)
            if response is None:
                # My.JDownloader Api failed too.
                return False
            else:
                # My.JDownloader Api worked, lets refresh the direct connections and return
                # the response.
                if self.__direct_connection_enabled \
                        and time.time() >= self.__direct_connection_cooldown:
                    self.__refresh_direct_connections()
                return response['data']
        else:
            # Direct connection info available, we try to use it.
            for conn in self.__direct_connection_info:
                connection_ip = conn['conn']['ip']
                # prevent connection to internal docker ip
                if time.time() > conn['cooldown']:
                    # We can use the connection
                    connection = conn['conn']
                    api = "http://" + connection_ip + ":" + str(
                        connection["port"])
                    try:
                        response = self.myjd.request_api(path, http_action, params,
                                                         action_url, api, timeout=3, output_errors=False)
                    except (TokenExpiredException, RequestTimeoutException, MYJDException):
                        response = None
                    if response is not None:
                        # This connection worked so we push it to the top of the list.
                        self.__direct_connection_info.remove(conn)
                        self.__direct_connection_info.insert(0, conn)
                        self.__direct_connection_consecutive_failures = 0
                        return response['data']
                    else:
                        # We don't try to use this connection for a minute.
                        conn['cooldown'] = time.time() + 60
            # None of the direct connections worked, we set a cooldown for direct connections
            self.__direct_connection_consecutive_failures += 1
            self.__direct_connection_cooldown = time.time() + (60 * self.__direct_connection_consecutive_failures)
            # None of the direct connections worked, we use the My.JDownloader api
            response = self.myjd.request_api(path, http_action, params,
                                             action_url)
            if response is None:
                # My.JDownloader Api failed too.
                return False
            # My.JDownloader Api worked, lets refresh the direct connections and return
            # the response.
            self.__refresh_direct_connections()
            return response['data']

    def __action_url(self):
        return "/t_" + self.myjd.get_session_token() + "_" + self.device_id


class Myjdapi:
    """
    Main class for connecting to JD API.

    """

    def __init__(self):
        """
        This functions initializates the myjd_api object.

        """
        self.__request_id = int(time.time() * 1000)
        self.__api_url = "https://api.jdownloader.org"
        self.__app_key = "http://git.io/vmcsk"
        self.__api_version = 1
        self.__devices = None
        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None
        self.__connected = False

    def get_session_token(self):
        return self.__session_token

    def is_connected(self):
        """
        Indicates if there is a connection established.
        """
        return self.__connected

    def set_app_key(self, app_key):
        """
        Sets the APP Key.
        """
        self.__app_key = app_key

    def __secret_create(self, email, password, domain):
        """
        Calculates the login_secret and device_secret

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :param domain: The domain , if is for Server (login_secret) or Device (device_secret)
        :return: secret hash

        """
        secret_hash = hashlib.sha256()
        secret_hash.update(email.lower().encode('utf-8')
                           + password.encode('utf-8')
                           + domain.lower().encode('utf-8'))
        return secret_hash.digest()

    def __update_encryption_tokens(self):
        """
        Updates the server_encryption_token and device_encryption_token

        """
        if self.__server_encryption_token is None:
            old_token = self.__login_secret
        else:
            old_token = self.__server_encryption_token
        new_token = hashlib.sha256()
        new_token.update(old_token + bytearray.fromhex(self.__session_token))
        self.__server_encryption_token = new_token.digest()
        new_token = hashlib.sha256()
        new_token.update(self.__device_secret +
                         bytearray.fromhex(self.__session_token))
        self.__device_encryption_token = new_token.digest()

    def __signature_create(self, key, data):
        """
        Calculates the signature for the data given a key.

        :param key:
        :param data:
        """
        signature = hmac.new(key, data.encode('utf-8'), hashlib.sha256)
        return signature.hexdigest()

    def __decrypt(self, secret_token, data):
        """
        Decrypts the data from the server using the provided token

        :param secret_token:
        :param data:
        """
        init_vector = secret_token[:len(secret_token) // 2]
        key = secret_token[len(secret_token) // 2:]
        decryptor = AES.new(key, AES.MODE_CBC, init_vector)
        decrypted_data = unpad(decryptor.decrypt(base64.b64decode(data)))
        return decrypted_data

    def __encrypt(self, secret_token, data):
        """
        Encrypts the data from the server using the provided token

        :param secret_token:
        :param data:
        """
        data = pad(data.encode('utf-8'))
        init_vector = secret_token[:len(secret_token) // 2]
        key = secret_token[len(secret_token) // 2:]
        encryptor = AES.new(key, AES.MODE_CBC, init_vector)
        encrypted_data = base64.b64encode(encryptor.encrypt(data))
        return encrypted_data.decode('utf-8')

    def update_request_id(self):
        """
        Updates Request_Id
        """
        self.__request_id = int(time.time())

    def connect(self, email, password):
        """Establish connection to api

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :returns: boolean -- True if succesful, False if there was any error.

        """
        self.update_request_id()
        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None
        self.__devices = None
        self.__connected = False

        self.__login_secret = self.__secret_create(email, password, "server")
        self.__device_secret = self.__secret_create(email, password, "device")
        response = self.request_api("/my/connect", "GET", [("email", email),
                                                           ("appkey",
                                                            self.__app_key)])
        self.__connected = True
        self.update_request_id()
        self.__session_token = response["sessiontoken"]
        self.__regain_token = response["regaintoken"]
        self.__update_encryption_tokens()
        self.update_devices()
        return response

    def reconnect(self):
        """
        Reestablish connection to API.

        :returns: boolean -- True if successful, False if there was any error.

        """
        response = self.request_api("/my/reconnect", "GET",
                                    [("sessiontoken", self.__session_token),
                                     ("regaintoken", self.__regain_token)])
        self.update_request_id()
        self.__session_token = response["sessiontoken"]
        self.__regain_token = response["regaintoken"]
        self.__update_encryption_tokens()
        return response

    def disconnect(self):
        """
        Disconnects from  API

        :returns: boolean -- True if successful, False if there was any error.

        """
        response = self.request_api("/my/disconnect", "GET",
                                    [("sessiontoken", self.__session_token)])
        self.update_request_id()
        self.__login_secret = None
        self.__device_secret = None
        self.__session_token = None
        self.__regain_token = None
        self.__server_encryption_token = None
        self.__device_encryption_token = None
        self.__devices = None
        self.__connected = False
        return response

    def update_devices(self):
        """
        Updates available devices. Use list_devices() to get the devices list.

        :returns: boolean -- True if successful, False if there was any error.
        """
        response = self.request_api("/my/listdevices", "GET",
                                    [("sessiontoken", self.__session_token)])
        self.update_request_id()
        self.__devices = response["list"]

    def list_devices(self):
        """
        Returns available devices. Use getDevices() to update the devices list.
        Each device in the list is a dictionary like this example:

        {
            'name': 'Device',
            'id': 'af9d03a21ddb917492dc1af8a6427f11',
            'type': 'jd'
        }

        :returns: list -- list of devices.
        """
        return self.__devices

    def get_device(self, device_name=None, device_id=None):
        """
        Returns a jddevice instance of the device
        :param device_name:
        :param device_id:

        """
        if not self.is_connected():
            raise (MYJDException("No connection established\n"))
        if device_id is not None:
            for device in self.__devices:
                if device["id"] == device_id:
                    return Jddevice(self, device)
        elif device_name is not None:
            for device in self.__devices:
                if device["name"] == device_name:
                    return Jddevice(self, device)
        raise (MYJDException("Device not found\n"))

    def request_api(self,
                    path,
                    http_method="GET",
                    params=None,
                    action=None,
                    api=None,
                    timeout=30,
                    output_errors=True):
        """
        Makes a request to the API to the 'path' using the 'http_method' with parameters,'params'.
        Ex:
        http_method=GET
        params={"test":"test"}
        post_params={"test2":"test2"}
        action=True
        This would make a request to "https://api.jdownloader.org"
        """
        if not api:
            api = self.__api_url
        data = None
        if not self.is_connected() and path != "/my/connect":
            raise (MYJDException("No connection established\n"))
        if http_method == "GET":
            query = [path + "?"]
            if params is not None:
                for param in params:
                    if param[0] != "encryptedLoginSecret":
                        query += ["%s=%s" % (param[0], quote(param[1]))]
                    else:
                        query += ["&%s=%s" % (param[0], param[1])]
            query += ["rid=" + str(self.__request_id)]
            if self.__server_encryption_token is None:
                query += [
                    "signature="
                    + str(self.__signature_create(self.__login_secret,
                                                  query[0] + "&".join(query[1:])))
                ]
            else:
                query += [
                    "signature="
                    + str(self.__signature_create(self.__server_encryption_token,
                                                  query[0] + "&".join(query[1:])))
                ]
            query = query[0] + "&".join(query[1:])
            try:
                encrypted_response = request(api + query, timeout=timeout, output_errors=output_errors)
            except URLError:
                encrypted_response = request(api + query, timeout=timeout, output_errors=output_errors, verify=False)
                print(u"Die sichere Verbindung zu MyJDownloader konnte nicht verifiziert werden.")
        else:
            params_request = []
            if params is not None:
                for param in params:
                    if not isinstance(param, list):
                        params_request += [json.dumps(param)]
                    else:
                        params_request += [param]
            params_request = {
                "apiVer": self.__api_version,
                "url": path,
                "params": params_request,
                "rid": self.__request_id
            }
            data = json.dumps(params_request)
            # Removing quotes around null elements.
            data = data.replace('"null"', "null")
            data = data.replace("'null'", "null")
            encrypted_data = self.__encrypt(self.__device_encryption_token,
                                            data)
            if action is not None:
                request_url = api + action + path
            else:
                request_url = api + path
            try:
                encrypted_response = request(
                    request_url,
                    headers={
                        "Content-Type": "application/aesjson-jd; charset=utf-8"
                    },
                    data=encrypted_data,
                    method="POST",
                    timeout=timeout,
                    output_errors=output_errors)
            except URLError:
                try:
                    encrypted_response = request(
                        request_url,
                        headers={
                            "Content-Type": "application/aesjson-jd; charset=utf-8"
                        },
                        data=encrypted_data,
                        method="POST",
                        timeout=timeout,
                        output_errors=output_errors,
                        verify=False)
                    print(u"Die sichere Verbindung zu MyJDownloader konnte nicht verifiziert werden.")
                except URLError:
                    return None
        if encrypted_response.status_code == 403:
            raise TokenExpiredException
        if encrypted_response.status_code == 503:
            raise RequestTimeoutException
        if encrypted_response.status_code != 200:
            try:
                error_msg = json.loads(encrypted_response.text)
            except:
                try:
                    error_msg = json.loads(self.__decrypt(self.__device_encryption_token, encrypted_response.text))
                except:
                    raise MYJDException("Failed to decode response: {}", encrypted_response.text)
            msg = "\n\tSOURCE: " + error_msg["src"] + "\n\tTYPE: " + \
                  error_msg["type"] + "\n------\nREQUEST_URL: " + \
                  api + path
            if http_method == "GET":
                msg += query
            msg += "\n"
            if data is not None:
                msg += "DATA:\n" + data
            raise (MYJDException(msg))
        if action is None:
            if not self.__server_encryption_token:
                response = self.__decrypt(self.__login_secret,
                                          encrypted_response.text)
            else:
                response = self.__decrypt(self.__server_encryption_token,
                                          encrypted_response.text)
        else:
            response = self.__decrypt(self.__device_encryption_token,
                                      encrypted_response.text)
        jsondata = json.loads(response.decode('utf-8'))
        if jsondata['rid'] != self.__request_id:
            self.update_request_id()
            return None
        self.update_request_id()
        return jsondata
