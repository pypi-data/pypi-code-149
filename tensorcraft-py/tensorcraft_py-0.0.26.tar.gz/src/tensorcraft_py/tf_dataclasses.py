import typing
from dataclasses import dataclass, field
from datetime import datetime
from datetime import timedelta
from enum import Enum
from random import randint
import jwt
import logging
import google.cloud.logging
from dataclasses_json import DataClassJsonMixin



client = google.cloud.logging.Client()
client.setup_logging()

class JobType(str, Enum):
  TEXT_2_IMAGE = "text2image"
  IMAGE_2_IMAGE = "image2image"


class JobState(str, Enum):
  UNKNOWN = "unknown"
  SUBMITTED = "submitted"
  ACCEPTED = "accepted"
  WORKING = "working"
  FINISHED = "finished"
  ERROR = "error"

class SubscriptionStatus(str, Enum):
  UNKNOWN = "unknown"
  PENDING = "pending"
  ACTIVE = "active"
  CANCELED = "canceled"
  ERROR = "error"

@dataclass
class BoundingBox (DataClassJsonMixin):
  left: int
  top: int
  right: int
  bottom: int

  def width(self):
    return self.right - self.left
  
  def height(self):
    return self.bottom - self.top
    
@dataclass
class Service(DataClassJsonMixin):
  id: str
  name: str
  version: str
  billing_subscription_id: str


@dataclass
class Subscription(DataClassJsonMixin):

  service_id: str
  status: SubscriptionStatus
  billing_customer_id: typing.Optional[str] = None
  billing_subscription_id: typing.Optional[str] = None
  billing_subscription_item_id: typing.Optional[str] = None

  def is_active(self) -> bool:
    return self.status == SubscriptionStatus.ACTIVE

@dataclass
class SubscriptionUsageSummary(DataClassJsonMixin):
  service_id: str
  amount: float
  start_time: typing.Optional[datetime] = None
  end_time: typing.Optional[datetime] = None

@dataclass
class ServiceUsage(DataClassJsonMixin):
  id: str
  user_secret_id: str
  service_id: str
  amount: float
  date: datetime
  ip_address: typing.Optional[str] = None


@dataclass
class Text2ImageParams(DataClassJsonMixin):
  seed: int = randint(0, 1000000)


@dataclass
class ImageSize(DataClassJsonMixin):
  width: int
  height: int


@dataclass
class ImageData(DataClassJsonMixin):
  id: str

  size: ImageSize

  uri: typing.Optional[str] = None
  reported: bool = False

  user_secret_id: typing.Optional[str] = None
  prompt: typing.Optional[str] = None
  seed: typing.Optional[int] = None
  source_image_id: typing.Optional[str] = None
  job_id: typing.Optional[str] = None
  image_bytes: typing.Optional[bytearray] = None
  creation_time: datetime = datetime.utcnow()
  is_protected: typing.Optional[bool] = None

  interrogated_description: typing.Optional[str] = None
  nsfw: bool = False

@dataclass
class ImageDataPublic(DataClassJsonMixin):
  id: str
  size: ImageSize
  uri: typing.Optional[str] = None
  nsfw: bool = False
  reported: bool = False

  def __init__(self, image_data: ImageData):
    self.id = image_data.id
    self.size = image_data.size
    self.nsfw = image_data.nsfw

    self.uri = None if image_data.nsfw else image_data.uri
    self.reported = image_data.reported

@dataclass
class JobStatus(DataClassJsonMixin):
  job_id: str
  job_state: JobState
  progress_pct: float
  images: list[ImageData] = field(default_factory=list)
  image_uris: list[str] = field(default_factory=list)
  error: bool = False


@dataclass
class Image2ImageParams(DataClassJsonMixin):
  source_image_id: str
  strength: float = 0.5
  seeds: typing.Optional[list[int]] = None


@dataclass
class Job(DataClassJsonMixin):
  id: str
  user_secret_id: str
  job_type: JobType
  prompt: str
  batch_size: int = 5
  size: ImageSize = ImageSize(512, 512)

  ddim_steps: int = 50
  scale: float = 7.5

  user_original_prompt: typing.Optional[str] = None
  negative_prompt: typing.Optional[str] = None
  text2image_params: typing.Optional[Text2ImageParams] = None
  image2image_params: typing.Optional[Image2ImageParams] = None
  checkpoint: typing.Optional[
      str] = None  # the stable diffusion checkpoint to use ex "protogen_anime.ckpt [b5c0b653]"
  fix_faces: typing.Optional[bool] = False

  creation_time: datetime = datetime.utcnow()
  reported: bool = False
  status: typing.Optional[JobStatus] = None

  rating: typing.Optional[int] = None
  ip_address: typing.Optional[str] = None

  app_version: typing.Optional[str] = None
  device: typing.Optional[str] = None
  device_os: typing.Optional[str] = None

  nsfw: bool = False
  def is_done(self):
    return self.status is not None and (self.status.job_state
                                        == JobState.FINISHED or
                                        self.status.job_state == JobState.ERROR)
  

@dataclass
class FilterExample(DataClassJsonMixin):
  # primary key is filter_id + tags
  image_data: ImageData
  filter_id: typing.Optional[str] = None
  source_image_data: typing.Optional[ImageData] = None
  strength: float = 1.0
  tags: list[str] = field(default_factory=list)
  example_group: typing.Optional[str] = None  # deprecated

  def id(self):
    assert self.filter_id is not None
    return f"{self.filter_id}_{'_'.join(self.tags)}"


@dataclass
class Filter(DataClassJsonMixin):
  id: str
  name: str
  description: str
  prompt: str

  ddim_steps: int
  scale: float
  strength: float
  is_premium: bool = False
  negative_prompt: typing.Optional[str] = None
  user_secret_id: typing.Optional[str] = None
  creation_time: datetime = datetime.utcnow()
  examples: typing.Optional[list[FilterExample]] = None

  text_compatible: bool = False
  face_specific: bool = False
  human_specific: bool = False
  checkpoint: typing.Optional[
      str] = None  # the stable diffusion checkpoint to use ex "protogen_anime.ckpt [b5c0b653]"
  thumbnail_uri: typing.Optional[str] = None  #deprecated
  fix_faces: typing.Optional[bool] = False


@dataclass
class AppFilters(DataClassJsonMixin):
  app_id: str
  filters: list[Filter]


@dataclass
class Ban(DataClassJsonMixin):
  ip_address: str
  ban_level: int
  expiration_time: datetime
  creation_time: datetime = datetime.utcnow()


@dataclass
class User(DataClassJsonMixin):
  secret_id: str
  public_id: str
  password_hash_hex: typing.Optional[str] = None
  password_salt_hex: typing.Optional[str] = None
  is_admin: bool = False
  is_blocked: bool = False
  ip_address: typing.Optional[str] = None
  billing_customer_id: typing.Optional[str] = None
  email: typing.Optional[str] = None
  billing_email: typing.Optional[str] = None
  name: typing.Optional[str] = None
  subscriptions: dict[str, Subscription] = field(default_factory=lambda: {}) 

  # subscription_active: typing.Optional[bool] = False
  # billing_subscription_id: typing.Optional[str] = None # deprecated
  # billing_subscription_item_id: typing.Optional[str] = None # deprecated

  def encode_auth_token(self, secret_key) -> str:
    """
    Generates the Auth Token
    :return: string
    """

    payload = {
        'exp': datetime.utcnow() + timedelta(weeks=500),
        'iat': datetime.utcnow(),
        'sub': self.secret_id
    }
    result = jwt.encode(payload, secret_key, algorithm='HS256')

    return result

  @staticmethod
  def decode_auth_token(auth_token, secret_key):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
      payload = jwt.decode(auth_token, secret_key, algorithms=['HS256'])
      return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please log in again.'

  def has_active_subscription(self, service_id: str):

    return service_id in self.subscriptions and self.subscriptions[
        service_id].status == SubscriptionStatus.ACTIVE

  def has_subscription(self, service_id: str):

    return service_id in self.subscriptions

  def billing_subscription_item_id(self, service_id: str):
    return self.subscriptions[service_id].billing_subscription_item_id
    
  def add_inactive_subscription(self, service_id: str, billing_subscription_id: str,
                            billing_subscription_item_id: str):
    if self.has_subscription(service_id):
      subscription = self.subscriptions[service_id]

      if subscription.billing_subscription_id != billing_subscription_id or subscription.billing_subscription_item_id != billing_subscription_item_id:
        logging.error("add_inactive_subscription: User has subscription to service but billing_subscription_item_id does not match")
        
        raise Exception("User already has subscription to service")
      return
    else:
      self.subscriptions[service_id] = Subscription(
          service_id=service_id,
          status=SubscriptionStatus.PENDING,
          billing_subscription_id=billing_subscription_id,
          billing_subscription_item_id=billing_subscription_item_id)
  def activate_subscription(self, service_id: str, billing_subscription_id: str,
                            billing_subscription_item_id: str):
    if self.has_subscription(service_id):
      subscription = self.subscriptions[service_id]

      if subscription.billing_subscription_id != billing_subscription_id or subscription.billing_subscription_item_id != billing_subscription_item_id:
        logging.error("User has subscription to service but billing_subscription_item_id does not match")
        
        raise Exception("User already has subscription to service")
      subscription.status = SubscriptionStatus.ACTIVE
    else:
      self.subscriptions[service_id] = Subscription(
          service_id=service_id,
          status=SubscriptionStatus.ACTIVE,
          billing_subscription_id=billing_subscription_id,
          billing_subscription_item_id=billing_subscription_item_id)


  def add_pending_subscription(self, service_id: str, billing_subscription_id: str,
                            billing_subscription_item_id: str):
    subscription = None                       
    if self.has_active_subscription(service_id):
     
        logging.warn("add_pending_subscription: User already has active subscription")
        
      
      
    else:
      subscription = Subscription(
          service_id=service_id,
          status=SubscriptionStatus.PENDING,
          billing_subscription_id=billing_subscription_id,
          billing_subscription_item_id=billing_subscription_item_id)

      self.subscriptions[service_id] = subscription
    
 
  def deactivate_subscription(self, service_id: str,billing_subscription_item_id):
    if self.has_subscription(service_id):
      subscription = self.subscriptions[service_id]
      if subscription.billing_subscription_item_id != billing_subscription_item_id:
        logging.warning("deactivate_subscription called  but billing_subscription_item_id does not match")
        return
      subscription.status = SubscriptionStatus.CANCELED
  
