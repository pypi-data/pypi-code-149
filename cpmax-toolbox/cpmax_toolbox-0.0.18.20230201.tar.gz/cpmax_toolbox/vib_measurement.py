import requests
import pytz

import warnings
import json
import threading
import time
from pathlib import Path

import datetime


def check_dict_scheme(d, s, return_bool=False):
    result = True
    for k, v in d.items():
        if isinstance(v, dict):
            if s[k] and isinstance(s[k], dict):
                if return_bool:
                    result &= check_dict_scheme(v, s[k], True)
                else:
                    check_dict_scheme(v, s[k], False)
            elif not isinstance(s[k], dict):
                if return_bool:
                    result = False
                else:
                    raise ValueError(f"Wrong Scheme! {k} is dict instead of {s[k][0]}")
        else:
            if k not in s:
                raise ValueError(f"{k} not found in schmeme, check spelling")
            tuple_comp = s[k]
            if not isinstance(v, tuple_comp[0]):
                if return_bool:
                    return False
                raise ValueError(
                    f"wrong type given for {k}: {type(v)} instead of {tuple_comp[0]}"
                )

            if tuple_comp[0] in (int, float):
                if not (tuple_comp[1] <= v <= tuple_comp[2]):
                    if return_bool:
                        return False
                    raise ValueError(
                        f"Value {k} not within limits ({tuple_comp[1]}, {tuple_comp[2]})"
                    )
            elif tuple_comp[0] in (str,):
                if not (tuple_comp[1] <= len(v) <= tuple_comp[2]):
                    if return_bool:
                        return False
                    raise ValueError(
                        f"length of str {k} not within limits ({tuple_comp[1]}, {tuple_comp[2]})"
                    )
            elif tuple_comp[0] in (bool,):
                pass
    if return_bool:
        return result


def wait_until(next_time, delta):

    while next_time - time.time() > 0:
        time.sleep(0.75 * (next_time - time.time()))

    return next_time + delta


class NanoVib:
    def __init__(self) -> None:
        self._base_url = "http://192.168.4.1"
        self._ensure_connection()
        self.settings = requests.get(self._base_url + "/settings").json()
        self._settings_scheme = {
            "sensor": {
                "srd": (int, 1, 20),
                "acc_range": (int, 2, 16),
                "bandwidth": (int, 5, 300),
                "calibration": {
                    "sx": (float, 0, 20),
                    "sy": (float, 0, 20),
                    "sz": (float, 0, 20),
                    "bx": (float, -20, 20),
                    "by": (float, -20, 20),
                    "bz": (float, -20, 20),
                },
            },
            "measurement": {
                "max_revolutions": (int, 0, 2e32),
                "rpm_min": (float, 0, 2e32),
                "rpm_max": (float, 0, 2e32),
                "measurement_time": (int, 1000, 300),
                "folder": "Test_Background_App",
                "parted": (bool,),
                "part_size": (int, 1024 * 1024, 2e32),
                "vibA_compatibility": (bool,),
            },
            "system": {"ssid": (str, 3, 254), "password": (str, 8, 254)},
        }
        self._status_scheme = {
            "system": {
                "epoch": (int, 946681200, 4102441200),
            },
            "measurement": {"recording": (bool,)},
        }
        self._update_time()
        self.status = requests.get(self._base_url + "/status").json()
        self.measurements = requests.get(self._base_url + "/measurements").json()
        self.status_thread = threading.Thread(target=self._refresh_status, daemon=True)
        self.status_thread.start()

    def _ensure_connection(self):
        connected = False
        for _ in range(10):
            try:
                self.status = requests.get(self._base_url + "/status", timeout=3).json()
                connected = True
                break
            except Exception as e:
                warnings.warn("Connection takes longer than expected")

        if not connected:
            raise ConnectionError(
                "Could not connect to NanoVib, ensure Wifi Connection to NanoVib and try again"
            )

    def _update_time(self):
        tz = pytz.timezone("Europe/Berlin")
        now = datetime.datetime.now().astimezone(tz)
        patch_dict = {
            "system": {
                "epoch": int(now.timestamp()) + int(now.utcoffset().total_seconds())
            }
        }
        self._update_status(patch_dict)

    def _refresh_status(self):
        t_next = int(time.time()) + 2
        while True:
            try:
                self.status = requests.get(self._base_url + "/status", timeout=1).json()
            except Exception as e:
                print(e)

            t_next = wait_until(t_next, 2)

    def _update_status(self, patch_dict):
        check_dict_scheme(patch_dict, self._status_scheme)
        self.status = requests.patch(
            self._base_url + "/status", data=json.dumps(patch_dict)
        ).json()

    def start_measurement(self, max_revs=None, measurement_time_min=None):
        settings_dict = {
            "measurement": {
                "max_revolutions": (2e32 if max_revs == None else int(max_revs)),
                "measurement_time": (
                    2e32
                    if measurement_time_min == None
                    else int(measurement_time_min * 60000)
                ),
            }
        }
        self.update_settings(settings_dict)

        patch_dict = {"measurement": {"recording": True}}
        self._update_status(patch_dict)

    def stop_measurement(self):
        patch_dict = {"measurement": {"recording": False}}
        self._update_status(patch_dict)

    def list_measurements(self):
        if self.status["measurement"]["recording"]:
            return (False, self.measurements)
        else:
            return (True, requests.get(self._base_url + "/measurements").json())

    def get_measurement(self, project=None, measurement_tag=None, generator=False):
        self._ensure_connection()

        """ determine wether live measurement -> live download or project and measurement are given -> only if not measuring """
        """ -> creates meas_base {project}/{measurement_tag}{ext}"""

        if (
            self.status["measurement"]["recording"]
            and not project
            and not measurement_tag
        ):
            meas_base = requests.get(self._base_url + "/measurements").json()[-1][
                "name"
            ]
        else:
            if self.status["measurement"]["recording"]:
                warnings.warn("measurements active! Download of measurement during another active measurement is not recommended!")
            if project:
                patch_dict = {"measurement": {"folder": project}}
                self.update_settings(patch_dict)
            measurements = requests.get(self._base_url + "/measurements").json()
            found = False
            for m in measurements:
                if measurement_tag in m["name"]:
                    found = True
                    break
            if not found:
                raise ValueError("Measurement not found")
            meas_base = m["name"]



        if meas_base.endswith(".txt") or meas_base.endswith(".csv"):
            """not parted -> download and if generator yield else return"""
            pass

        else:
            project_name = meas_base.split("/")[1]
            meas_tag = meas_base.split("/")[-1]

            ext = (
                ".txt" if self.settings["measurement"]["vibA_compatibility"] else ".csv"
            )

            dl_path = Path().home() / "Downloads" / project_name
            combined_file = dl_path / (meas_tag + "_combined" + ext)

            last_yielded_at_part = 0

            while True:

                """ find highest found partnumber """
                part_found_max = 0
                for p in [p for p in dl_path.iterdir() if meas_tag in p.name]:
                    if p.stem.startswith(meas_tag):
                        try:
                            part_found_max = max(
                                (int(p.stem.split("_")[-1]), part_found_max)
                            )
                        except ValueError:
                            pass

                """ generate url and path of parted file """
                part_url = (
                    self._base_url + meas_base +"/"+ str(part_found_max + 1).zfill(4) + ext
                )
                part_file = dl_path / (
                    meas_tag + "_" + str(part_found_max + 1).zfill(4) + ext
                )

                """ get file from device """
                try:
                    resp = requests.get(part_url, timeout=60)
                except Exception as e:
                    print(e)
                    time.sleep(5)
                    continue

                

                if resp.status_code == 200:
                    with open(part_file, "wb") as f:
                        f.write(resp.content)

                    with open(combined_file, "ab") as f:
                        f.write(resp.content)

                if resp.status_code == 409:
                    if generator and last_yielded_at_part != part_found_max:
                        last_yielded_at_part = part_found_max
                        yield combined_file
                    else:
                        time.sleep(5)

                if resp.status_code == 404:
                    if generator and last_yielded_at_part != part_found_max:
                        last_yielded_at_part = part_found_max
                        yield combined_file
                    break

    def update_settings(self, patch_dict: dict, check_scheme: bool = True):
        self._ensure_connection()
        if not check_scheme:
            check_dict_scheme(patch_dict, self._settings_scheme)
        settings_old = self.settings
        resp = requests.patch(
            self._base_url + "/settings", data=json.dumps(patch_dict), timeout=1
        )
        if resp.status_code != 200:
            warnings.warn(resp.status_code)
        else:
            self.settings = resp.json()

        if (
            settings_old["measurement"]["folder"]
            != self.settings["measurement"]["folder"]
        ):
            self.measurements = requests.get(self._base_url + "/measurements").json()


if __name__ == "__main__":
    nano = NanoVib()

    nano.start_measurement(measurement_time_min=20)

    for updated_file in nano.get_measurement(generator=True):
        print(updated_file.stat().st_size)

    nano.stop_measurement()
