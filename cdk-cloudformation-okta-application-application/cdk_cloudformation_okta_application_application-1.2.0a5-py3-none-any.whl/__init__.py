'''
# okta-application-application

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Okta::Application::Application` v1.2.0.

## Description

Manage an Application in Okta.

## References

* [Documentation](https://github.com/aws-ia/cloudformation-okta-resource-providers)
* [Source](https://github.com/aws-ia/cloudformation-okta-resource-providers.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Okta::Application::Application \
  --publisher-id c830e97710da0c9954d80ba8df021e5439e7134b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/c830e97710da0c9954d80ba8df021e5439e7134b/Okta-Application-Application \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Okta::Application::Application`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fokta-application-application+v1.2.0).
* Issues related to `Okta::Application::Application` should be reported to the [publisher](https://github.com/aws-ia/cloudformation-okta-resource-providers).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.Accessibility",
    jsii_struct_bases=[],
    name_mapping={
        "error_redirect_url": "errorRedirectUrl",
        "self_service": "selfService",
    },
)
class Accessibility:
    def __init__(
        self,
        *,
        error_redirect_url: typing.Optional[builtins.str] = None,
        self_service: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Specifies access settings for the application.

        :param error_redirect_url: Custom error page for this application.
        :param self_service: Enable self-service application assignment.

        :schema: Accessibility
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5e0d6b7af284a665c31eeebbb361188c32c3645bfd9aaa922408da68f43f87)
            check_type(argname="argument error_redirect_url", value=error_redirect_url, expected_type=type_hints["error_redirect_url"])
            check_type(argname="argument self_service", value=self_service, expected_type=type_hints["self_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if error_redirect_url is not None:
            self._values["error_redirect_url"] = error_redirect_url
        if self_service is not None:
            self._values["self_service"] = self_service

    @builtins.property
    def error_redirect_url(self) -> typing.Optional[builtins.str]:
        '''Custom error page for this application.

        :schema: Accessibility#ErrorRedirectUrl
        '''
        result = self._values.get("error_redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self_service(self) -> typing.Optional[builtins.bool]:
        '''Enable self-service application assignment.

        :schema: Accessibility#SelfService
        '''
        result = self._values.get("self_service")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Accessibility(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.ApplicationCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "oauth_client": "oauthClient",
        "password": "password",
        "reveal_password": "revealPassword",
        "scheme": "scheme",
        "signing": "signing",
        "user_name": "userName",
        "user_name_template": "userNameTemplate",
    },
)
class ApplicationCredentials:
    def __init__(
        self,
        *,
        oauth_client: typing.Optional[typing.Union["OauthCredential", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        reveal_password: typing.Optional[builtins.bool] = None,
        scheme: typing.Optional["AuthenticationScheme"] = None,
        signing: typing.Optional[typing.Union["SigningCredential", typing.Dict[builtins.str, typing.Any]]] = None,
        user_name: typing.Optional[builtins.str] = None,
        user_name_template: typing.Optional[typing.Union["UserNameTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Specifies credentials and scheme for the application's signOnMode.

        :param oauth_client: 
        :param password: 
        :param reveal_password: Whether to reveal the credential password.
        :param scheme: 
        :param signing: 
        :param user_name: Shared username for app.
        :param user_name_template: 

        :schema: ApplicationCredentials
        '''
        if isinstance(oauth_client, dict):
            oauth_client = OauthCredential(**oauth_client)
        if isinstance(signing, dict):
            signing = SigningCredential(**signing)
        if isinstance(user_name_template, dict):
            user_name_template = UserNameTemplate(**user_name_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50510ea9d0bfd70909b4eda07a3236948ed596ef6b4accc9a338841047d40b17)
            check_type(argname="argument oauth_client", value=oauth_client, expected_type=type_hints["oauth_client"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument reveal_password", value=reveal_password, expected_type=type_hints["reveal_password"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument signing", value=signing, expected_type=type_hints["signing"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument user_name_template", value=user_name_template, expected_type=type_hints["user_name_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if oauth_client is not None:
            self._values["oauth_client"] = oauth_client
        if password is not None:
            self._values["password"] = password
        if reveal_password is not None:
            self._values["reveal_password"] = reveal_password
        if scheme is not None:
            self._values["scheme"] = scheme
        if signing is not None:
            self._values["signing"] = signing
        if user_name is not None:
            self._values["user_name"] = user_name
        if user_name_template is not None:
            self._values["user_name_template"] = user_name_template

    @builtins.property
    def oauth_client(self) -> typing.Optional["OauthCredential"]:
        '''
        :schema: ApplicationCredentials#OauthClient
        '''
        result = self._values.get("oauth_client")
        return typing.cast(typing.Optional["OauthCredential"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ApplicationCredentials#Password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reveal_password(self) -> typing.Optional[builtins.bool]:
        '''Whether to reveal the credential password.

        :schema: ApplicationCredentials#RevealPassword
        '''
        result = self._values.get("reveal_password")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scheme(self) -> typing.Optional["AuthenticationScheme"]:
        '''
        :schema: ApplicationCredentials#Scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional["AuthenticationScheme"], result)

    @builtins.property
    def signing(self) -> typing.Optional["SigningCredential"]:
        '''
        :schema: ApplicationCredentials#Signing
        '''
        result = self._values.get("signing")
        return typing.cast(typing.Optional["SigningCredential"], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Shared username for app.

        :schema: ApplicationCredentials#UserName
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name_template(self) -> typing.Optional["UserNameTemplate"]:
        '''
        :schema: ApplicationCredentials#UserNameTemplate
        '''
        result = self._values.get("user_name_template")
        return typing.cast(typing.Optional["UserNameTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/okta-application-application.AuthenticationScheme"
)
class AuthenticationScheme(enum.Enum):
    '''Authentication Scheme.

    :schema: AuthenticationScheme
    '''

    ADMIN_SETS_CREDENTIALS = "ADMIN_SETS_CREDENTIALS"
    '''ADMIN_SETS_CREDENTIALS.'''
    EDIT_PASSWORD_ONLY = "EDIT_PASSWORD_ONLY"
    '''EDIT_PASSWORD_ONLY.'''
    EDIT_USERNAME_AND_PASSWORD = "EDIT_USERNAME_AND_PASSWORD"
    '''EDIT_USERNAME_AND_PASSWORD.'''
    EXTERNAL_PASSWORD_SYNC = "EXTERNAL_PASSWORD_SYNC"
    '''EXTERNAL_PASSWORD_SYNC.'''
    SHARED_USERNAME_AND_PASSWORD = "SHARED_USERNAME_AND_PASSWORD"
    '''SHARED_USERNAME_AND_PASSWORD.'''


class CfnApplication(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/okta-application-application.CfnApplication",
):
    '''A CloudFormation ``Okta::Application::Application``.

    :cloudformationResource: Okta::Application::Application
    :link: https://github.com/aws-ia/cloudformation-okta-resource-providers.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        label: builtins.str,
        sign_on_mode: "SignOnMode",
        accessibility: typing.Optional[typing.Union[Accessibility, typing.Dict[builtins.str, typing.Any]]] = None,
        credentials: typing.Optional[typing.Union[ApplicationCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        request_object_signing_alg: typing.Optional["CfnApplicationPropsRequestObjectSigningAlg"] = None,
        settings: typing.Optional[typing.Union["CfnApplicationPropsSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        visibility: typing.Optional[typing.Union["Visibility", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Okta::Application::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param label: User-defined display name for app.
        :param sign_on_mode: 
        :param accessibility: 
        :param credentials: 
        :param name: Unique key for app definition.
        :param request_object_signing_alg: The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request object.
        :param settings: 
        :param visibility: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e14307e4ae5cd49316c1e4ceff89d997fd1557b77c834eeaaa0ab72e392cdc0f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            label=label,
            sign_on_mode=sign_on_mode,
            accessibility=accessibility,
            credentials=credentials,
            name=name,
            request_object_signing_alg=request_object_signing_alg,
            settings=settings,
            visibility=visibility,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Okta::Application::Application.Id``.

        :link: https://github.com/aws-ia/cloudformation-okta-resource-providers.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnApplicationProps":
        '''Resource props.'''
        return typing.cast("CfnApplicationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "label": "label",
        "sign_on_mode": "signOnMode",
        "accessibility": "accessibility",
        "credentials": "credentials",
        "name": "name",
        "request_object_signing_alg": "requestObjectSigningAlg",
        "settings": "settings",
        "visibility": "visibility",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        label: builtins.str,
        sign_on_mode: "SignOnMode",
        accessibility: typing.Optional[typing.Union[Accessibility, typing.Dict[builtins.str, typing.Any]]] = None,
        credentials: typing.Optional[typing.Union[ApplicationCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        request_object_signing_alg: typing.Optional["CfnApplicationPropsRequestObjectSigningAlg"] = None,
        settings: typing.Optional[typing.Union["CfnApplicationPropsSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        visibility: typing.Optional[typing.Union["Visibility", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Manage an Application in Okta.

        :param label: User-defined display name for app.
        :param sign_on_mode: 
        :param accessibility: 
        :param credentials: 
        :param name: Unique key for app definition.
        :param request_object_signing_alg: The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request object.
        :param settings: 
        :param visibility: 

        :schema: CfnApplicationProps
        '''
        if isinstance(accessibility, dict):
            accessibility = Accessibility(**accessibility)
        if isinstance(credentials, dict):
            credentials = ApplicationCredentials(**credentials)
        if isinstance(settings, dict):
            settings = CfnApplicationPropsSettings(**settings)
        if isinstance(visibility, dict):
            visibility = Visibility(**visibility)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c5575a18819e112143c64a476cc3f11a0f8d61a205c79acb8c0725760ab7f5)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument sign_on_mode", value=sign_on_mode, expected_type=type_hints["sign_on_mode"])
            check_type(argname="argument accessibility", value=accessibility, expected_type=type_hints["accessibility"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request_object_signing_alg", value=request_object_signing_alg, expected_type=type_hints["request_object_signing_alg"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "sign_on_mode": sign_on_mode,
        }
        if accessibility is not None:
            self._values["accessibility"] = accessibility
        if credentials is not None:
            self._values["credentials"] = credentials
        if name is not None:
            self._values["name"] = name
        if request_object_signing_alg is not None:
            self._values["request_object_signing_alg"] = request_object_signing_alg
        if settings is not None:
            self._values["settings"] = settings
        if visibility is not None:
            self._values["visibility"] = visibility

    @builtins.property
    def label(self) -> builtins.str:
        '''User-defined display name for app.

        :schema: CfnApplicationProps#Label
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sign_on_mode(self) -> "SignOnMode":
        '''
        :schema: CfnApplicationProps#SignOnMode
        '''
        result = self._values.get("sign_on_mode")
        assert result is not None, "Required property 'sign_on_mode' is missing"
        return typing.cast("SignOnMode", result)

    @builtins.property
    def accessibility(self) -> typing.Optional[Accessibility]:
        '''
        :schema: CfnApplicationProps#Accessibility
        '''
        result = self._values.get("accessibility")
        return typing.cast(typing.Optional[Accessibility], result)

    @builtins.property
    def credentials(self) -> typing.Optional[ApplicationCredentials]:
        '''
        :schema: CfnApplicationProps#Credentials
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[ApplicationCredentials], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Unique key for app definition.

        :schema: CfnApplicationProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_object_signing_alg(
        self,
    ) -> typing.Optional["CfnApplicationPropsRequestObjectSigningAlg"]:
        '''The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request object.

        :schema: CfnApplicationProps#RequestObjectSigningAlg
        '''
        result = self._values.get("request_object_signing_alg")
        return typing.cast(typing.Optional["CfnApplicationPropsRequestObjectSigningAlg"], result)

    @builtins.property
    def settings(self) -> typing.Optional["CfnApplicationPropsSettings"]:
        '''
        :schema: CfnApplicationProps#Settings
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional["CfnApplicationPropsSettings"], result)

    @builtins.property
    def visibility(self) -> typing.Optional["Visibility"]:
        '''
        :schema: CfnApplicationProps#Visibility
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional["Visibility"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/okta-application-application.CfnApplicationPropsRequestObjectSigningAlg"
)
class CfnApplicationPropsRequestObjectSigningAlg(enum.Enum):
    '''The type of JSON Web Key Set (JWKS) algorithm that must be used for signing request object.

    :schema: CfnApplicationPropsRequestObjectSigningAlg
    '''

    HS256 = "HS256"
    '''HS256.'''
    HS384 = "HS384"
    '''HS384.'''
    HS512 = "HS512"
    '''HS512.'''
    RS256 = "RS256"
    '''RS256.'''
    RS384 = "RS384"
    '''RS384.'''
    RS512 = "RS512"
    '''RS512.'''
    ES256 = "ES256"
    '''ES256.'''
    ES384 = "ES384"
    '''ES384.'''
    ES512 = "ES512"
    '''ES512.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.CfnApplicationPropsSettings",
    jsii_struct_bases=[],
    name_mapping={"app": "app"},
)
class CfnApplicationPropsSettings:
    def __init__(
        self,
        *,
        app: typing.Optional[typing.Union["CfnApplicationPropsSettingsApp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param app: 

        :schema: CfnApplicationPropsSettings
        '''
        if isinstance(app, dict):
            app = CfnApplicationPropsSettingsApp(**app)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb947efcfb36748963768f0e74ef6612962e651de9ac3d8fe211581897cc0c5e)
            check_type(argname="argument app", value=app, expected_type=type_hints["app"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app is not None:
            self._values["app"] = app

    @builtins.property
    def app(self) -> typing.Optional["CfnApplicationPropsSettingsApp"]:
        '''
        :schema: CfnApplicationPropsSettings#App
        '''
        result = self._values.get("app")
        return typing.cast(typing.Optional["CfnApplicationPropsSettingsApp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationPropsSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.CfnApplicationPropsSettingsApp",
    jsii_struct_bases=[],
    name_mapping={"auth_url": "authUrl", "site_url": "siteUrl", "url": "url"},
)
class CfnApplicationPropsSettingsApp:
    def __init__(
        self,
        *,
        auth_url: typing.Optional[builtins.str] = None,
        site_url: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_url: 
        :param site_url: 
        :param url: 

        :schema: CfnApplicationPropsSettingsApp
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a46ce325b9bc68b1b495c38e220df317d4624e6f12babc6403d58075a9468ed9)
            check_type(argname="argument auth_url", value=auth_url, expected_type=type_hints["auth_url"])
            check_type(argname="argument site_url", value=site_url, expected_type=type_hints["site_url"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_url is not None:
            self._values["auth_url"] = auth_url
        if site_url is not None:
            self._values["site_url"] = site_url
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def auth_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApplicationPropsSettingsApp#AuthURL
        '''
        result = self._values.get("auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def site_url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApplicationPropsSettingsApp#SiteURL
        '''
        result = self._values.get("site_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApplicationPropsSettingsApp#Url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationPropsSettingsApp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.Hide",
    jsii_struct_bases=[],
    name_mapping={"ios": "ios", "web": "web"},
)
class Hide:
    def __init__(self, *, ios: builtins.bool, web: builtins.bool) -> None:
        '''Hides this app for specific end-user apps.

        :param ios: Okta Mobile for iOS or Android (pre-dates Android).
        :param web: Okta Web Browser Home Page.

        :schema: Hide
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883582e449d78067e082daab9e55ac04d6c30e78324339d92d273e7b1eb1c761)
            check_type(argname="argument ios", value=ios, expected_type=type_hints["ios"])
            check_type(argname="argument web", value=web, expected_type=type_hints["web"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ios": ios,
            "web": web,
        }

    @builtins.property
    def ios(self) -> builtins.bool:
        '''Okta Mobile for iOS or Android (pre-dates Android).

        :schema: Hide#IOS
        '''
        result = self._values.get("ios")
        assert result is not None, "Required property 'ios' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def web(self) -> builtins.bool:
        '''Okta Web Browser Home Page.

        :schema: Hide#Web
        '''
        result = self._values.get("web")
        assert result is not None, "Required property 'web' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Hide(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.OauthCredential",
    jsii_struct_bases=[],
    name_mapping={
        "token_endpoint_auth_method": "tokenEndpointAuthMethod",
        "auto_key_rotation": "autoKeyRotation",
        "client_id": "clientId",
        "client_secret": "clientSecret",
    },
)
class OauthCredential:
    def __init__(
        self,
        *,
        token_endpoint_auth_method: builtins.str,
        auto_key_rotation: typing.Optional[builtins.bool] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Determines how to authenticate the OAuth 2.0 client.

        :param token_endpoint_auth_method: Requested authentication method for the token endpoint.
        :param auto_key_rotation: Requested key rotation mode.
        :param client_id: Unique identifier for the OAuth 2.0 client application.
        :param client_secret: OAuth 2.0 client secret string.

        :schema: OauthCredential
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eab3b008381a12715660692984839aba9aac0beb4fde45e5b15fe378c35bb92)
            check_type(argname="argument token_endpoint_auth_method", value=token_endpoint_auth_method, expected_type=type_hints["token_endpoint_auth_method"])
            check_type(argname="argument auto_key_rotation", value=auto_key_rotation, expected_type=type_hints["auto_key_rotation"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "token_endpoint_auth_method": token_endpoint_auth_method,
        }
        if auto_key_rotation is not None:
            self._values["auto_key_rotation"] = auto_key_rotation
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret

    @builtins.property
    def token_endpoint_auth_method(self) -> builtins.str:
        '''Requested authentication method for the token endpoint.

        :schema: OauthCredential#TokenEndpointAuthMethod
        '''
        result = self._values.get("token_endpoint_auth_method")
        assert result is not None, "Required property 'token_endpoint_auth_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_key_rotation(self) -> typing.Optional[builtins.bool]:
        '''Requested key rotation mode.

        :schema: OauthCredential#AutoKeyRotation
        '''
        result = self._values.get("auto_key_rotation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for the OAuth 2.0 client application.

        :schema: OauthCredential#ClientId
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''OAuth 2.0 client secret string.

        :schema: OauthCredential#ClientSecret
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OauthCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/okta-application-application.SignOnMode")
class SignOnMode(enum.Enum):
    '''
    :schema: SignOnMode
    '''

    AUTO_LOGIN = "AUTO_LOGIN"
    '''AUTO_LOGIN.'''
    BASIC_AUTH = "BASIC_AUTH"
    '''BASIC_AUTH.'''
    BOOKMARK = "BOOKMARK"
    '''BOOKMARK.'''
    BROWSER_PLUGIN = "BROWSER_PLUGIN"
    '''BROWSER_PLUGIN.'''
    CUSTOM = "CUSTOM"
    '''Custom.'''
    OPENID_CONNECT = "OPENID_CONNECT"
    '''OPENID_CONNECT.'''
    SAML_1_1 = "SAML_1_1"
    '''SAML_1_1.'''
    SAML_2_0 = "SAML_2_0"
    '''SAML_2_0.'''
    SECURE_PASSWORD_STORE = "SECURE_PASSWORD_STORE"
    '''SECURE_PASSWORD_STORE.'''
    WS_FEDERATION = "WS_FEDERATION"
    '''WS_FEDERATION.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.SigningCredential",
    jsii_struct_bases=[],
    name_mapping={"kid": "kid"},
)
class SigningCredential:
    def __init__(self, *, kid: typing.Optional[builtins.str] = None) -> None:
        '''Determines the key used for signing assertions for the signOnMode.

        :param kid: Reference for key credential for the app.

        :schema: SigningCredential
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f627b99d10a8a581884fbc3dc3f738712628d62e598d3c5efd086db5e70a0512)
            check_type(argname="argument kid", value=kid, expected_type=type_hints["kid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kid is not None:
            self._values["kid"] = kid

    @builtins.property
    def kid(self) -> typing.Optional[builtins.str]:
        '''Reference for key credential for the app.

        :schema: SigningCredential#Kid
        '''
        result = self._values.get("kid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SigningCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.UserNameTemplate",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "template": "template"},
)
class UserNameTemplate:
    def __init__(
        self,
        *,
        type: "UserNameTemplateType",
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Specifies the template used to generate a user's username when the application is assigned via a group or directly to a user.

        :param type: type of mapping expression.
        :param template: mapping expression for username.

        :schema: UserNameTemplate
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2202cbb15cb922dbf6c924c5db53f5abfc4b3b169a051c0140588a697e0309f)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def type(self) -> "UserNameTemplateType":
        '''type of mapping expression.

        :schema: UserNameTemplate#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("UserNameTemplateType", result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''mapping expression for username.

        :schema: UserNameTemplate#Template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserNameTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/okta-application-application.UserNameTemplateType"
)
class UserNameTemplateType(enum.Enum):
    '''type of mapping expression.

    :schema: UserNameTemplateType
    '''

    NONE = "NONE"
    '''NONE.'''
    BUILT_IN = "BUILT_IN"
    '''BUILT_IN.'''
    CUSTOM = "CUSTOM"
    '''CUSTOM.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/okta-application-application.Visibility",
    jsii_struct_bases=[],
    name_mapping={
        "auto_launch": "autoLaunch",
        "auto_submit_toolbar": "autoSubmitToolbar",
        "hide": "hide",
    },
)
class Visibility:
    def __init__(
        self,
        *,
        auto_launch: builtins.bool,
        auto_submit_toolbar: builtins.bool,
        hide: typing.Union[Hide, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Specifies visibility settings for the application.

        :param auto_launch: Automatically signs in to the app when user signs into Okta.
        :param auto_submit_toolbar: Automatically sign in when user lands on the sign-in page.
        :param hide: Hides this app for specific end-user apps.

        :schema: Visibility
        '''
        if isinstance(hide, dict):
            hide = Hide(**hide)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8ffac4de5eb691e47c2eabe278f74799535cfce4e384969c484123309822aa5)
            check_type(argname="argument auto_launch", value=auto_launch, expected_type=type_hints["auto_launch"])
            check_type(argname="argument auto_submit_toolbar", value=auto_submit_toolbar, expected_type=type_hints["auto_submit_toolbar"])
            check_type(argname="argument hide", value=hide, expected_type=type_hints["hide"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_launch": auto_launch,
            "auto_submit_toolbar": auto_submit_toolbar,
            "hide": hide,
        }

    @builtins.property
    def auto_launch(self) -> builtins.bool:
        '''Automatically signs in to the app when user signs into Okta.

        :schema: Visibility#AutoLaunch
        '''
        result = self._values.get("auto_launch")
        assert result is not None, "Required property 'auto_launch' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def auto_submit_toolbar(self) -> builtins.bool:
        '''Automatically sign in when user lands on the sign-in page.

        :schema: Visibility#AutoSubmitToolbar
        '''
        result = self._values.get("auto_submit_toolbar")
        assert result is not None, "Required property 'auto_submit_toolbar' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def hide(self) -> Hide:
        '''Hides this app for specific end-user apps.

        :schema: Visibility#Hide
        '''
        result = self._values.get("hide")
        assert result is not None, "Required property 'hide' is missing"
        return typing.cast(Hide, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Visibility(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Accessibility",
    "ApplicationCredentials",
    "AuthenticationScheme",
    "CfnApplication",
    "CfnApplicationProps",
    "CfnApplicationPropsRequestObjectSigningAlg",
    "CfnApplicationPropsSettings",
    "CfnApplicationPropsSettingsApp",
    "Hide",
    "OauthCredential",
    "SignOnMode",
    "SigningCredential",
    "UserNameTemplate",
    "UserNameTemplateType",
    "Visibility",
]

publication.publish()

def _typecheckingstub__9e5e0d6b7af284a665c31eeebbb361188c32c3645bfd9aaa922408da68f43f87(
    *,
    error_redirect_url: typing.Optional[builtins.str] = None,
    self_service: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50510ea9d0bfd70909b4eda07a3236948ed596ef6b4accc9a338841047d40b17(
    *,
    oauth_client: typing.Optional[typing.Union[OauthCredential, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    reveal_password: typing.Optional[builtins.bool] = None,
    scheme: typing.Optional[AuthenticationScheme] = None,
    signing: typing.Optional[typing.Union[SigningCredential, typing.Dict[builtins.str, typing.Any]]] = None,
    user_name: typing.Optional[builtins.str] = None,
    user_name_template: typing.Optional[typing.Union[UserNameTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e14307e4ae5cd49316c1e4ceff89d997fd1557b77c834eeaaa0ab72e392cdc0f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    label: builtins.str,
    sign_on_mode: SignOnMode,
    accessibility: typing.Optional[typing.Union[Accessibility, typing.Dict[builtins.str, typing.Any]]] = None,
    credentials: typing.Optional[typing.Union[ApplicationCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    request_object_signing_alg: typing.Optional[CfnApplicationPropsRequestObjectSigningAlg] = None,
    settings: typing.Optional[typing.Union[CfnApplicationPropsSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    visibility: typing.Optional[typing.Union[Visibility, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c5575a18819e112143c64a476cc3f11a0f8d61a205c79acb8c0725760ab7f5(
    *,
    label: builtins.str,
    sign_on_mode: SignOnMode,
    accessibility: typing.Optional[typing.Union[Accessibility, typing.Dict[builtins.str, typing.Any]]] = None,
    credentials: typing.Optional[typing.Union[ApplicationCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    request_object_signing_alg: typing.Optional[CfnApplicationPropsRequestObjectSigningAlg] = None,
    settings: typing.Optional[typing.Union[CfnApplicationPropsSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    visibility: typing.Optional[typing.Union[Visibility, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb947efcfb36748963768f0e74ef6612962e651de9ac3d8fe211581897cc0c5e(
    *,
    app: typing.Optional[typing.Union[CfnApplicationPropsSettingsApp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46ce325b9bc68b1b495c38e220df317d4624e6f12babc6403d58075a9468ed9(
    *,
    auth_url: typing.Optional[builtins.str] = None,
    site_url: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883582e449d78067e082daab9e55ac04d6c30e78324339d92d273e7b1eb1c761(
    *,
    ios: builtins.bool,
    web: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eab3b008381a12715660692984839aba9aac0beb4fde45e5b15fe378c35bb92(
    *,
    token_endpoint_auth_method: builtins.str,
    auto_key_rotation: typing.Optional[builtins.bool] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f627b99d10a8a581884fbc3dc3f738712628d62e598d3c5efd086db5e70a0512(
    *,
    kid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2202cbb15cb922dbf6c924c5db53f5abfc4b3b169a051c0140588a697e0309f(
    *,
    type: UserNameTemplateType,
    template: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8ffac4de5eb691e47c2eabe278f74799535cfce4e384969c484123309822aa5(
    *,
    auto_launch: builtins.bool,
    auto_submit_toolbar: builtins.bool,
    hide: typing.Union[Hide, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass
