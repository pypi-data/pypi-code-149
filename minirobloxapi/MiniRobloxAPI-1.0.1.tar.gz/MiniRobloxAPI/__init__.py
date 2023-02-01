import requests

# Options get user
class OptionsGetUser:
    def __init__(self, data):
        self.data = data

    def name(self):
        return self.data["name"]
    def user_id(self):
        return self.data["id"]
    def description(self):
        if self.data["description"] == "":
            return None
        else:
            return self.data["description"]
    def created(self):
        return self.data["created"]
    def is_banned(self):
        return self.data["isBanned"]
    def has_verified_badge(self):
        return self.data["hasVerifiedBadge"]
    def display_name(self):
        return self.data["displayName"]
    def avatar_image(self):
        image = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={self.data['id']}&size=420x420&format=Png&isCircular=false")
        return image.json()["data"][0]["imageUrl"]
    
# Options get group
class OptionsGetGroup:
    def __init__(self, data):
        self.data = data
    
    def name(self):
        return self.data["data"][0]["name"]
    def group_id(self):
        return self.data["data"][0]["id"]
    def description(self):
        return self.data["data"][0]["description"]
    def icon_image(self):
        image = requests.get(f"https://thumbnails.roblox.com/v1/groups/icons?groupIds={self.data['data'][0]['id']}&size=420x420&format=Png&isCircular=false")
        return image.json()["data"][0]["imageUrl"]
    def created(self):
        return self.data["data"][0]["created"]
    def has_verified_badge(self):
        return self.data["data"][0]["hasVerifiedBadge"]
    def owner(self):
        user = self.data["data"][0]["owner"]["id"]
        data = requests.get(f"https://users.roblox.com/v1/users/{user}")
        return OptionsGetUser(data=data.json())
    
# Options get badge
class OptionsGetBadge:
    def __init__(self, data):
        self.data = data
    
    def name(self):
        return self.data["name"]
    def badge_id(self):
        return self.data["id"]
    def description(self):
        return self.data["description"]
    def created(self):
        return self.data["created"]
    def updated(self):
        return self.data["updated"]
    def past_day_awarded_count(self):
        return self.data["statistics"]["pastDayAwardedCount"]
    def awarded_count(self):
        return self.data["statistics"]["awardedCount"]
    def rarity(self):
        return self.data["statistics"]["winRatePercentage"]
    def icon_image(self):
        image = requests.get(f"https://thumbnails.roblox.com/v1/badges/icons?badgeIds={self.data['id']}&size=150x150&format=Png&isCircular=false")
        return image.json()["data"][0]["imageUrl"]

# RobloxAPI
class RobloxAPI:
    # get user by id
    def get_user_by_id(user_id):
        data = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        return OptionsGetUser(data=data.json())
    
    # get user by name
    def get_user_by_name(user_name):
        user_id = requests.get(F"https://api.roblox.com/users/get-by-username?username={user_name}").json()["Id"]
        data = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        return OptionsGetUser(data=data.json())
    
    # get group by id
    def get_group_by_id(group_id):
        data = requests.get(f"https://groups.roblox.com/v2/groups?groupIds={group_id}")
        return OptionsGetGroup(data=data.json())
    
    # get badge by id
    def get_badge_by_id(badge_id):
        data = requests.get(f"https://badges.roblox.com/v1/badges/{badge_id}")
        return OptionsGetBadge(data=data.json())