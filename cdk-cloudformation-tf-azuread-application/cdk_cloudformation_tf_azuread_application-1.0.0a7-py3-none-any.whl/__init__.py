'''
# tf-azuread-application

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AzureAD::Application` v1.0.0.

## Description

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/azuread/TF-AzureAD-Application/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AzureAD::Application \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AzureAD-Application \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AzureAD::Application`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-azuread-application+v1.0.0).
* Issues related to `TF::AzureAD::Application` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/azuread/TF-AzureAD-Application/docs/README.md).

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
    jsii_type="@cdk-cloudformation/tf-azuread-application.AccessTokenDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_properties": "additionalProperties",
        "essential": "essential",
        "source": "source",
    },
)
class AccessTokenDefinition:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
        essential: typing.Optional[builtins.bool] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param additional_properties: 
        :param essential: 
        :param source: 

        :schema: AccessTokenDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e5d187257a6b0108253ad50bf708d3abe812b7f2e1d7bdd27b879163b72da6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if essential is not None:
            self._values["essential"] = essential
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: AccessTokenDefinition#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: AccessTokenDefinition#AdditionalProperties
        '''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def essential(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: AccessTokenDefinition#Essential
        '''
        result = self._values.get("essential")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AccessTokenDefinition#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessTokenDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.ApiDefinition",
    jsii_struct_bases=[],
    name_mapping={"oauth2_permission_scope": "oauth2PermissionScope"},
)
class ApiDefinition:
    def __init__(
        self,
        *,
        oauth2_permission_scope: typing.Optional[typing.Sequence[typing.Union["Oauth2PermissionScopeDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param oauth2_permission_scope: 

        :schema: ApiDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f957dd1f84bf03df1075e59634ff5501afdc5a00665d41231883e0dae7d9be6)
            check_type(argname="argument oauth2_permission_scope", value=oauth2_permission_scope, expected_type=type_hints["oauth2_permission_scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if oauth2_permission_scope is not None:
            self._values["oauth2_permission_scope"] = oauth2_permission_scope

    @builtins.property
    def oauth2_permission_scope(
        self,
    ) -> typing.Optional[typing.List["Oauth2PermissionScopeDefinition"]]:
        '''
        :schema: ApiDefinition#Oauth2PermissionScope
        '''
        result = self._values.get("oauth2_permission_scope")
        return typing.cast(typing.Optional[typing.List["Oauth2PermissionScopeDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.AppRoleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_member_types": "allowedMemberTypes",
        "description": "description",
        "display_name": "displayName",
        "enabled": "enabled",
        "id": "id",
        "is_enabled": "isEnabled",
        "value": "value",
    },
)
class AppRoleDefinition:
    def __init__(
        self,
        *,
        allowed_member_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_member_types: 
        :param description: 
        :param display_name: 
        :param enabled: 
        :param id: 
        :param is_enabled: 
        :param value: 

        :schema: AppRoleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b6a2a5d9ec9b2fb7922fedec87015633be67a3777835dcfa25403f7e0bf203)
            check_type(argname="argument allowed_member_types", value=allowed_member_types, expected_type=type_hints["allowed_member_types"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_member_types is not None:
            self._values["allowed_member_types"] = allowed_member_types
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def allowed_member_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: AppRoleDefinition#AllowedMemberTypes
        '''
        result = self._values.get("allowed_member_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AppRoleDefinition#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AppRoleDefinition#DisplayName
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: AppRoleDefinition#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AppRoleDefinition#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: AppRoleDefinition#IsEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: AppRoleDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppRoleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnApplication(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-azuread-application.CfnApplication",
):
    '''A CloudFormation ``TF::AzureAD::Application``.

    :cloudformationResource: TF::AzureAD::Application
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: typing.Optional[typing.Sequence[typing.Union[ApiDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        app_role: typing.Optional[typing.Sequence[typing.Union[AppRoleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        available_to_other_tenants: typing.Optional[builtins.bool] = None,
        display_name: typing.Optional[builtins.str] = None,
        fallback_public_client_enabled: typing.Optional[builtins.bool] = None,
        group_membership_claims: typing.Optional[builtins.str] = None,
        homepage: typing.Optional[builtins.str] = None,
        identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logout_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        oauth2_allow_implicit_flow: typing.Optional[builtins.bool] = None,
        oauth2_permissions: typing.Optional[typing.Sequence[typing.Union["Oauth2PermissionsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        optional_claims: typing.Optional[typing.Sequence[typing.Union["OptionalClaimsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[builtins.bool] = None,
        public_client: typing.Optional[builtins.bool] = None,
        reply_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        required_resource_access: typing.Optional[typing.Sequence[typing.Union["RequiredResourceAccessDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        sign_in_audience: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["TimeoutsDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        web: typing.Optional[typing.Sequence[typing.Union["WebDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``TF::AzureAD::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api: 
        :param app_role: A collection of ``app_role`` blocks as documented below. For more information see `official documentation on Application Roles <https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles>`_.
        :param available_to_other_tenants: Is this Azure AD Application available to other tenants? Defaults to ``false``. This property is deprecated and has been replaced by the ``sign_in_audience`` property. Default: false``. This property is deprecated and has been replaced by the ``sign_in_audience` property.
        :param display_name: The display name for the application.
        :param fallback_public_client_enabled: The fallback application type as public client, such as an installed application running on a mobile device. Defaults to ``false``. Default: false`.
        :param group_membership_claims: Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to ``SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup`` or ``All``. Default: SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup``or``All`.
        :param homepage: The URL to the application's home page. This property is deprecated and has been replaced by the ``homepage_url`` property in the ``web`` block.
        :param identifier_uris: The user-defined URI(s) that uniquely identify an application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        :param logout_url: The URL of the logout page. This property is deprecated and has been replaced by the ``logout_url`` property in the ``web`` block.
        :param name: The name of the optional claim.
        :param oauth2_allow_implicit_flow: Does this Azure AD Application allow OAuth 2.0 implicit flow tokens? Defaults to ``false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled`` property in the ``implicit_grant`` block. Default: false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled``property in the``implicit_grant` block.
        :param oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by ``oauth2_permissions`` blocks as documented below. This block is deprecated and has been replaced by the ``oauth2_permission_scope`` block in the ``api`` block.
        :param optional_claims: 
        :param owners: A list of object IDs of principals that will be granted ownership of the application. It's recommended to specify the object ID of the authenticated principal running Terraform, to ensure sufficient permissions that the application can be subsequently updated.
        :param prevent_duplicate_names: If ``true``, will return an error when an existing Application is found with the same name. Defaults to ``false``. Default: false`.
        :param public_client: Is this Azure AD Application a public client? Defaults to ``false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled`` property. Default: false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled` property.
        :param reply_urls: A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to. This property is deprecated and has been replaced by the ``redirect_uris`` property in the ``web`` block.
        :param required_resource_access: 
        :param sign_in_audience: The Microsoft account types that are supported for the current application. Must be one of ``AzureADMyOrg`` or ``AzureADMultipleOrgs``. Defaults to ``AzureADMyOrg``. Default: AzureADMyOrg`.
        :param timeouts: 
        :param type: The type of the application: ``webapp/api`` or ``native``. Defaults to ``webapp/api``. For ``native`` apps type ``identifier_uris`` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**. Default: webapp/api``. For ``native``apps type``identifier_uris` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**.
        :param web: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__950d3eb1a0fdd146244959f4147ec0b5491013121b6d268b236e5bba7fca77e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            api=api,
            app_role=app_role,
            available_to_other_tenants=available_to_other_tenants,
            display_name=display_name,
            fallback_public_client_enabled=fallback_public_client_enabled,
            group_membership_claims=group_membership_claims,
            homepage=homepage,
            identifier_uris=identifier_uris,
            logout_url=logout_url,
            name=name,
            oauth2_allow_implicit_flow=oauth2_allow_implicit_flow,
            oauth2_permissions=oauth2_permissions,
            optional_claims=optional_claims,
            owners=owners,
            prevent_duplicate_names=prevent_duplicate_names,
            public_client=public_client,
            reply_urls=reply_urls,
            required_resource_access=required_resource_access,
            sign_in_audience=sign_in_audience,
            timeouts=timeouts,
            type=type,
            web=web,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::Application.ApplicationId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::Application.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrObjectId")
    def attr_object_id(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::Application.ObjectId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrObjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AzureAD::Application.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnApplicationProps":
        '''Resource props.'''
        return typing.cast("CfnApplicationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api": "api",
        "app_role": "appRole",
        "available_to_other_tenants": "availableToOtherTenants",
        "display_name": "displayName",
        "fallback_public_client_enabled": "fallbackPublicClientEnabled",
        "group_membership_claims": "groupMembershipClaims",
        "homepage": "homepage",
        "identifier_uris": "identifierUris",
        "logout_url": "logoutUrl",
        "name": "name",
        "oauth2_allow_implicit_flow": "oauth2AllowImplicitFlow",
        "oauth2_permissions": "oauth2Permissions",
        "optional_claims": "optionalClaims",
        "owners": "owners",
        "prevent_duplicate_names": "preventDuplicateNames",
        "public_client": "publicClient",
        "reply_urls": "replyUrls",
        "required_resource_access": "requiredResourceAccess",
        "sign_in_audience": "signInAudience",
        "timeouts": "timeouts",
        "type": "type",
        "web": "web",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        api: typing.Optional[typing.Sequence[typing.Union[ApiDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        app_role: typing.Optional[typing.Sequence[typing.Union[AppRoleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        available_to_other_tenants: typing.Optional[builtins.bool] = None,
        display_name: typing.Optional[builtins.str] = None,
        fallback_public_client_enabled: typing.Optional[builtins.bool] = None,
        group_membership_claims: typing.Optional[builtins.str] = None,
        homepage: typing.Optional[builtins.str] = None,
        identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logout_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        oauth2_allow_implicit_flow: typing.Optional[builtins.bool] = None,
        oauth2_permissions: typing.Optional[typing.Sequence[typing.Union["Oauth2PermissionsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        optional_claims: typing.Optional[typing.Sequence[typing.Union["OptionalClaimsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        owners: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_duplicate_names: typing.Optional[builtins.bool] = None,
        public_client: typing.Optional[builtins.bool] = None,
        reply_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        required_resource_access: typing.Optional[typing.Sequence[typing.Union["RequiredResourceAccessDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        sign_in_audience: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["TimeoutsDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        web: typing.Optional[typing.Sequence[typing.Union["WebDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Manages an Application within Azure Active Directory.

        -> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both ``Read and write owned by applications`` and ``Sign in and read user profile`` within the ``Windows Azure Active Directory`` API.

        :param api: 
        :param app_role: A collection of ``app_role`` blocks as documented below. For more information see `official documentation on Application Roles <https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles>`_.
        :param available_to_other_tenants: Is this Azure AD Application available to other tenants? Defaults to ``false``. This property is deprecated and has been replaced by the ``sign_in_audience`` property. Default: false``. This property is deprecated and has been replaced by the ``sign_in_audience` property.
        :param display_name: The display name for the application.
        :param fallback_public_client_enabled: The fallback application type as public client, such as an installed application running on a mobile device. Defaults to ``false``. Default: false`.
        :param group_membership_claims: Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to ``SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup`` or ``All``. Default: SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup``or``All`.
        :param homepage: The URL to the application's home page. This property is deprecated and has been replaced by the ``homepage_url`` property in the ``web`` block.
        :param identifier_uris: The user-defined URI(s) that uniquely identify an application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
        :param logout_url: The URL of the logout page. This property is deprecated and has been replaced by the ``logout_url`` property in the ``web`` block.
        :param name: The name of the optional claim.
        :param oauth2_allow_implicit_flow: Does this Azure AD Application allow OAuth 2.0 implicit flow tokens? Defaults to ``false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled`` property in the ``implicit_grant`` block. Default: false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled``property in the``implicit_grant` block.
        :param oauth2_permissions: A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by ``oauth2_permissions`` blocks as documented below. This block is deprecated and has been replaced by the ``oauth2_permission_scope`` block in the ``api`` block.
        :param optional_claims: 
        :param owners: A list of object IDs of principals that will be granted ownership of the application. It's recommended to specify the object ID of the authenticated principal running Terraform, to ensure sufficient permissions that the application can be subsequently updated.
        :param prevent_duplicate_names: If ``true``, will return an error when an existing Application is found with the same name. Defaults to ``false``. Default: false`.
        :param public_client: Is this Azure AD Application a public client? Defaults to ``false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled`` property. Default: false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled` property.
        :param reply_urls: A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to. This property is deprecated and has been replaced by the ``redirect_uris`` property in the ``web`` block.
        :param required_resource_access: 
        :param sign_in_audience: The Microsoft account types that are supported for the current application. Must be one of ``AzureADMyOrg`` or ``AzureADMultipleOrgs``. Defaults to ``AzureADMyOrg``. Default: AzureADMyOrg`.
        :param timeouts: 
        :param type: The type of the application: ``webapp/api`` or ``native``. Defaults to ``webapp/api``. For ``native`` apps type ``identifier_uris`` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**. Default: webapp/api``. For ``native``apps type``identifier_uris` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**.
        :param web: 

        :schema: CfnApplicationProps
        '''
        if isinstance(timeouts, dict):
            timeouts = TimeoutsDefinition(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c5fe466db4cfe807e9bc725b1cfa495d39f25a6dd0300fa8dae4e9420f5adf)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument app_role", value=app_role, expected_type=type_hints["app_role"])
            check_type(argname="argument available_to_other_tenants", value=available_to_other_tenants, expected_type=type_hints["available_to_other_tenants"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument fallback_public_client_enabled", value=fallback_public_client_enabled, expected_type=type_hints["fallback_public_client_enabled"])
            check_type(argname="argument group_membership_claims", value=group_membership_claims, expected_type=type_hints["group_membership_claims"])
            check_type(argname="argument homepage", value=homepage, expected_type=type_hints["homepage"])
            check_type(argname="argument identifier_uris", value=identifier_uris, expected_type=type_hints["identifier_uris"])
            check_type(argname="argument logout_url", value=logout_url, expected_type=type_hints["logout_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument oauth2_allow_implicit_flow", value=oauth2_allow_implicit_flow, expected_type=type_hints["oauth2_allow_implicit_flow"])
            check_type(argname="argument oauth2_permissions", value=oauth2_permissions, expected_type=type_hints["oauth2_permissions"])
            check_type(argname="argument optional_claims", value=optional_claims, expected_type=type_hints["optional_claims"])
            check_type(argname="argument owners", value=owners, expected_type=type_hints["owners"])
            check_type(argname="argument prevent_duplicate_names", value=prevent_duplicate_names, expected_type=type_hints["prevent_duplicate_names"])
            check_type(argname="argument public_client", value=public_client, expected_type=type_hints["public_client"])
            check_type(argname="argument reply_urls", value=reply_urls, expected_type=type_hints["reply_urls"])
            check_type(argname="argument required_resource_access", value=required_resource_access, expected_type=type_hints["required_resource_access"])
            check_type(argname="argument sign_in_audience", value=sign_in_audience, expected_type=type_hints["sign_in_audience"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument web", value=web, expected_type=type_hints["web"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api is not None:
            self._values["api"] = api
        if app_role is not None:
            self._values["app_role"] = app_role
        if available_to_other_tenants is not None:
            self._values["available_to_other_tenants"] = available_to_other_tenants
        if display_name is not None:
            self._values["display_name"] = display_name
        if fallback_public_client_enabled is not None:
            self._values["fallback_public_client_enabled"] = fallback_public_client_enabled
        if group_membership_claims is not None:
            self._values["group_membership_claims"] = group_membership_claims
        if homepage is not None:
            self._values["homepage"] = homepage
        if identifier_uris is not None:
            self._values["identifier_uris"] = identifier_uris
        if logout_url is not None:
            self._values["logout_url"] = logout_url
        if name is not None:
            self._values["name"] = name
        if oauth2_allow_implicit_flow is not None:
            self._values["oauth2_allow_implicit_flow"] = oauth2_allow_implicit_flow
        if oauth2_permissions is not None:
            self._values["oauth2_permissions"] = oauth2_permissions
        if optional_claims is not None:
            self._values["optional_claims"] = optional_claims
        if owners is not None:
            self._values["owners"] = owners
        if prevent_duplicate_names is not None:
            self._values["prevent_duplicate_names"] = prevent_duplicate_names
        if public_client is not None:
            self._values["public_client"] = public_client
        if reply_urls is not None:
            self._values["reply_urls"] = reply_urls
        if required_resource_access is not None:
            self._values["required_resource_access"] = required_resource_access
        if sign_in_audience is not None:
            self._values["sign_in_audience"] = sign_in_audience
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type
        if web is not None:
            self._values["web"] = web

    @builtins.property
    def api(self) -> typing.Optional[typing.List[ApiDefinition]]:
        '''
        :schema: CfnApplicationProps#Api
        '''
        result = self._values.get("api")
        return typing.cast(typing.Optional[typing.List[ApiDefinition]], result)

    @builtins.property
    def app_role(self) -> typing.Optional[typing.List[AppRoleDefinition]]:
        '''A collection of ``app_role`` blocks as documented below.

        For more information see `official documentation on Application Roles <https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles>`_.

        :schema: CfnApplicationProps#AppRole
        '''
        result = self._values.get("app_role")
        return typing.cast(typing.Optional[typing.List[AppRoleDefinition]], result)

    @builtins.property
    def available_to_other_tenants(self) -> typing.Optional[builtins.bool]:
        '''Is this Azure AD Application available to other tenants?

        Defaults to ``false``. This property is deprecated and has been replaced by the ``sign_in_audience`` property.

        :default: false``. This property is deprecated and has been replaced by the ``sign_in_audience` property.

        :schema: CfnApplicationProps#AvailableToOtherTenants
        '''
        result = self._values.get("available_to_other_tenants")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name for the application.

        :schema: CfnApplicationProps#DisplayName
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fallback_public_client_enabled(self) -> typing.Optional[builtins.bool]:
        '''The fallback application type as public client, such as an installed application running on a mobile device.

        Defaults to ``false``.

        :default: false`.

        :schema: CfnApplicationProps#FallbackPublicClientEnabled
        '''
        result = self._values.get("fallback_public_client_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group_membership_claims(self) -> typing.Optional[builtins.str]:
        '''Configures the ``groups`` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to ``SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup`` or ``All``.

        :default: SecurityGroup``. Possible values are ``None``, ``SecurityGroup``, ``DirectoryRole``, ``ApplicationGroup``or``All`.

        :schema: CfnApplicationProps#GroupMembershipClaims
        '''
        result = self._values.get("group_membership_claims")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def homepage(self) -> typing.Optional[builtins.str]:
        '''The URL to the application's home page.

        This property is deprecated and has been replaced by the ``homepage_url`` property in the ``web`` block.

        :schema: CfnApplicationProps#Homepage
        '''
        result = self._values.get("homepage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The user-defined URI(s) that uniquely identify an application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

        :schema: CfnApplicationProps#IdentifierUris
        '''
        result = self._values.get("identifier_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logout_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the logout page.

        This property is deprecated and has been replaced by the ``logout_url`` property in the ``web`` block.

        :schema: CfnApplicationProps#LogoutUrl
        '''
        result = self._values.get("logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the optional claim.

        :schema: CfnApplicationProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_allow_implicit_flow(self) -> typing.Optional[builtins.bool]:
        '''Does this Azure AD Application allow OAuth 2.0 implicit flow tokens? Defaults to ``false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled`` property in the ``implicit_grant`` block.

        :default: false``. This property is deprecated and has been replaced by the ``access_token_issuance_enabled``property in the``implicit_grant` block.

        :schema: CfnApplicationProps#Oauth2AllowImplicitFlow
        '''
        result = self._values.get("oauth2_allow_implicit_flow")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def oauth2_permissions(
        self,
    ) -> typing.Optional[typing.List["Oauth2PermissionsDefinition"]]:
        '''A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by ``oauth2_permissions`` blocks as documented below. This block is deprecated and has been replaced by the ``oauth2_permission_scope`` block in the ``api`` block.

        :schema: CfnApplicationProps#Oauth2Permissions
        '''
        result = self._values.get("oauth2_permissions")
        return typing.cast(typing.Optional[typing.List["Oauth2PermissionsDefinition"]], result)

    @builtins.property
    def optional_claims(
        self,
    ) -> typing.Optional[typing.List["OptionalClaimsDefinition"]]:
        '''
        :schema: CfnApplicationProps#OptionalClaims
        '''
        result = self._values.get("optional_claims")
        return typing.cast(typing.Optional[typing.List["OptionalClaimsDefinition"]], result)

    @builtins.property
    def owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of object IDs of principals that will be granted ownership of the application.

        It's recommended to specify the object ID of the authenticated principal running Terraform, to ensure sufficient permissions that the application can be subsequently updated.

        :schema: CfnApplicationProps#Owners
        '''
        result = self._values.get("owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prevent_duplicate_names(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, will return an error when an existing Application is found with the same name.

        Defaults to ``false``.

        :default: false`.

        :schema: CfnApplicationProps#PreventDuplicateNames
        '''
        result = self._values.get("prevent_duplicate_names")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_client(self) -> typing.Optional[builtins.bool]:
        '''Is this Azure AD Application a public client?

        Defaults to ``false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled`` property.

        :default: false``. This property is deprecated and has been replaced by the ``fallback_public_client_enabled` property.

        :schema: CfnApplicationProps#PublicClient
        '''
        result = self._values.get("public_client")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reply_urls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to. This property is deprecated and has been replaced by the ``redirect_uris`` property in the ``web`` block.

        :schema: CfnApplicationProps#ReplyUrls
        '''
        result = self._values.get("reply_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def required_resource_access(
        self,
    ) -> typing.Optional[typing.List["RequiredResourceAccessDefinition"]]:
        '''
        :schema: CfnApplicationProps#RequiredResourceAccess
        '''
        result = self._values.get("required_resource_access")
        return typing.cast(typing.Optional[typing.List["RequiredResourceAccessDefinition"]], result)

    @builtins.property
    def sign_in_audience(self) -> typing.Optional[builtins.str]:
        '''The Microsoft account types that are supported for the current application.

        Must be one of ``AzureADMyOrg`` or ``AzureADMultipleOrgs``. Defaults to ``AzureADMyOrg``.

        :default: AzureADMyOrg`.

        :schema: CfnApplicationProps#SignInAudience
        '''
        result = self._values.get("sign_in_audience")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["TimeoutsDefinition"]:
        '''
        :schema: CfnApplicationProps#Timeouts
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["TimeoutsDefinition"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the application: ``webapp/api`` or ``native``.

        Defaults to ``webapp/api``. For ``native`` apps type ``identifier_uris`` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**.

        :default: webapp/api``. For ``native``apps type``identifier_uris` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**.

        :schema: CfnApplicationProps#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web(self) -> typing.Optional[typing.List["WebDefinition"]]:
        '''
        :schema: CfnApplicationProps#Web
        '''
        result = self._values.get("web")
        return typing.cast(typing.Optional[typing.List["WebDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.IdTokenDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_properties": "additionalProperties",
        "essential": "essential",
        "source": "source",
    },
)
class IdTokenDefinition:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
        essential: typing.Optional[builtins.bool] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param additional_properties: 
        :param essential: 
        :param source: 

        :schema: IdTokenDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2d162e7850a5aad08c30abbcd7f43470bdd4a07962e8866706b7506b431e89e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if essential is not None:
            self._values["essential"] = essential
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: IdTokenDefinition#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: IdTokenDefinition#AdditionalProperties
        '''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def essential(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: IdTokenDefinition#Essential
        '''
        result = self._values.get("essential")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''
        :schema: IdTokenDefinition#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdTokenDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.ImplicitGrantDefinition",
    jsii_struct_bases=[],
    name_mapping={"access_token_issuance_enabled": "accessTokenIssuanceEnabled"},
)
class ImplicitGrantDefinition:
    def __init__(
        self,
        *,
        access_token_issuance_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param access_token_issuance_enabled: 

        :schema: ImplicitGrantDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8399bf204710effc75133b87c67735a052c26c89c52f3095331fa269ed9c91a)
            check_type(argname="argument access_token_issuance_enabled", value=access_token_issuance_enabled, expected_type=type_hints["access_token_issuance_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token_issuance_enabled is not None:
            self._values["access_token_issuance_enabled"] = access_token_issuance_enabled

    @builtins.property
    def access_token_issuance_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ImplicitGrantDefinition#AccessTokenIssuanceEnabled
        '''
        result = self._values.get("access_token_issuance_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImplicitGrantDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.Oauth2PermissionScopeDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "admin_consent_description": "adminConsentDescription",
        "admin_consent_display_name": "adminConsentDisplayName",
        "enabled": "enabled",
        "type": "type",
        "user_consent_description": "userConsentDescription",
        "user_consent_display_name": "userConsentDisplayName",
        "value": "value",
    },
)
class Oauth2PermissionScopeDefinition:
    def __init__(
        self,
        *,
        id: builtins.str,
        admin_consent_description: typing.Optional[builtins.str] = None,
        admin_consent_display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
        user_consent_description: typing.Optional[builtins.str] = None,
        user_consent_display_name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: The unique identifier of the delegated permission. Must be a valid UUID.
        :param admin_consent_description: Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users.
        :param admin_consent_display_name: Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users.
        :param enabled: Determines if the permission scope is enabled. Defaults to ``true``. Default: true`.
        :param type: Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions. Defaults to ``User``. Possible values are ``User`` or ``Admin``. Default: User``. Possible values are ``User``or``Admin`.
        :param user_consent_description: Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf.
        :param user_consent_display_name: Display name for the delegated permission that appears in the end user consent experience.
        :param value: The value that is used for the ``scp`` claim in OAuth 2.0 access tokens.

        :schema: Oauth2PermissionScopeDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27202c9e123ff76ef91849c43d561fe171a1165a7cb54cd561e9e2e2195928bd)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument admin_consent_description", value=admin_consent_description, expected_type=type_hints["admin_consent_description"])
            check_type(argname="argument admin_consent_display_name", value=admin_consent_display_name, expected_type=type_hints["admin_consent_display_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_consent_description", value=user_consent_description, expected_type=type_hints["user_consent_description"])
            check_type(argname="argument user_consent_display_name", value=user_consent_display_name, expected_type=type_hints["user_consent_display_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if admin_consent_description is not None:
            self._values["admin_consent_description"] = admin_consent_description
        if admin_consent_display_name is not None:
            self._values["admin_consent_display_name"] = admin_consent_display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if type is not None:
            self._values["type"] = type
        if user_consent_description is not None:
            self._values["user_consent_description"] = user_consent_description
        if user_consent_display_name is not None:
            self._values["user_consent_display_name"] = user_consent_display_name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier of the delegated permission.

        Must be a valid UUID.

        :schema: Oauth2PermissionScopeDefinition#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_consent_description(self) -> typing.Optional[builtins.str]:
        '''Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users.

        :schema: Oauth2PermissionScopeDefinition#AdminConsentDescription
        '''
        result = self._values.get("admin_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users.

        :schema: Oauth2PermissionScopeDefinition#AdminConsentDisplayName
        '''
        result = self._values.get("admin_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Determines if the permission scope is enabled.

        Defaults to ``true``.

        :default: true`.

        :schema: Oauth2PermissionScopeDefinition#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions.

        Defaults to ``User``. Possible values are ``User`` or ``Admin``.

        :default: User``. Possible values are ``User``or``Admin`.

        :schema: Oauth2PermissionScopeDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_description(self) -> typing.Optional[builtins.str]:
        '''Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf.

        :schema: Oauth2PermissionScopeDefinition#UserConsentDescription
        '''
        result = self._values.get("user_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the delegated permission that appears in the end user consent experience.

        :schema: Oauth2PermissionScopeDefinition#UserConsentDisplayName
        '''
        result = self._values.get("user_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value that is used for the ``scp`` claim in OAuth 2.0 access tokens.

        :schema: Oauth2PermissionScopeDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Oauth2PermissionScopeDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.Oauth2PermissionsDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "admin_consent_description": "adminConsentDescription",
        "admin_consent_display_name": "adminConsentDisplayName",
        "id": "id",
        "is_enabled": "isEnabled",
        "type": "type",
        "user_consent_description": "userConsentDescription",
        "user_consent_display_name": "userConsentDisplayName",
        "value": "value",
    },
)
class Oauth2PermissionsDefinition:
    def __init__(
        self,
        *,
        admin_consent_description: typing.Optional[builtins.str] = None,
        admin_consent_display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
        user_consent_description: typing.Optional[builtins.str] = None,
        user_consent_display_name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_consent_description: 
        :param admin_consent_display_name: 
        :param id: 
        :param is_enabled: 
        :param type: 
        :param user_consent_description: 
        :param user_consent_display_name: 
        :param value: 

        :schema: Oauth2PermissionsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a48f3a002c17de32e8201b01e7450c4a7d8694430e9022b6be0403f8cf990d)
            check_type(argname="argument admin_consent_description", value=admin_consent_description, expected_type=type_hints["admin_consent_description"])
            check_type(argname="argument admin_consent_display_name", value=admin_consent_display_name, expected_type=type_hints["admin_consent_display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user_consent_description", value=user_consent_description, expected_type=type_hints["user_consent_description"])
            check_type(argname="argument user_consent_display_name", value=user_consent_display_name, expected_type=type_hints["user_consent_display_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admin_consent_description is not None:
            self._values["admin_consent_description"] = admin_consent_description
        if admin_consent_display_name is not None:
            self._values["admin_consent_display_name"] = admin_consent_display_name
        if id is not None:
            self._values["id"] = id
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if type is not None:
            self._values["type"] = type
        if user_consent_description is not None:
            self._values["user_consent_description"] = user_consent_description
        if user_consent_display_name is not None:
            self._values["user_consent_display_name"] = user_consent_display_name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def admin_consent_description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#AdminConsentDescription
        '''
        result = self._values.get("admin_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#AdminConsentDisplayName
        '''
        result = self._values.get("admin_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: Oauth2PermissionsDefinition#IsEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#UserConsentDescription
        '''
        result = self._values.get("user_consent_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_consent_display_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#UserConsentDisplayName
        '''
        result = self._values.get("user_consent_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Oauth2PermissionsDefinition#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Oauth2PermissionsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.OptionalClaimsDefinition",
    jsii_struct_bases=[],
    name_mapping={"access_token": "accessToken", "id_token": "idToken"},
)
class OptionalClaimsDefinition:
    def __init__(
        self,
        *,
        access_token: typing.Optional[typing.Sequence[typing.Union[AccessTokenDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        id_token: typing.Optional[typing.Sequence[typing.Union[IdTokenDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param access_token: 
        :param id_token: 

        :schema: OptionalClaimsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df164420c7ceaad106c7f21981ac427fa7628cb07910c8d07d6d9c2761ec5a71)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument id_token", value=id_token, expected_type=type_hints["id_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if id_token is not None:
            self._values["id_token"] = id_token

    @builtins.property
    def access_token(self) -> typing.Optional[typing.List[AccessTokenDefinition]]:
        '''
        :schema: OptionalClaimsDefinition#AccessToken
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[typing.List[AccessTokenDefinition]], result)

    @builtins.property
    def id_token(self) -> typing.Optional[typing.List[IdTokenDefinition]]:
        '''
        :schema: OptionalClaimsDefinition#IdToken
        '''
        result = self._values.get("id_token")
        return typing.cast(typing.Optional[typing.List[IdTokenDefinition]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OptionalClaimsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.RequiredResourceAccessDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "resource_app_id": "resourceAppId",
        "resource_access": "resourceAccess",
    },
)
class RequiredResourceAccessDefinition:
    def __init__(
        self,
        *,
        resource_app_id: builtins.str,
        resource_access: typing.Optional[typing.Sequence[typing.Union["ResourceAccessDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param resource_app_id: The unique identifier for the resource that the application requires access to. This should be the Application ID of the target application.
        :param resource_access: 

        :schema: RequiredResourceAccessDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__debae0db93edadb458253d402108d5561550171a62d703066a4d2fdfedbfb003)
            check_type(argname="argument resource_app_id", value=resource_app_id, expected_type=type_hints["resource_app_id"])
            check_type(argname="argument resource_access", value=resource_access, expected_type=type_hints["resource_access"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_app_id": resource_app_id,
        }
        if resource_access is not None:
            self._values["resource_access"] = resource_access

    @builtins.property
    def resource_app_id(self) -> builtins.str:
        '''The unique identifier for the resource that the application requires access to.

        This should be the Application ID of the target application.

        :schema: RequiredResourceAccessDefinition#ResourceAppId
        '''
        result = self._values.get("resource_app_id")
        assert result is not None, "Required property 'resource_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_access(
        self,
    ) -> typing.Optional[typing.List["ResourceAccessDefinition"]]:
        '''
        :schema: RequiredResourceAccessDefinition#ResourceAccess
        '''
        result = self._values.get("resource_access")
        return typing.cast(typing.Optional[typing.List["ResourceAccessDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequiredResourceAccessDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.ResourceAccessDefinition",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class ResourceAccessDefinition:
    def __init__(self, *, id: builtins.str, type: builtins.str) -> None:
        '''
        :param id: The unique identifier for one of the ``OAuth2Permission`` or ``AppRole`` instances that the resource application exposes.
        :param type: Specifies whether the ``id`` property references an ``OAuth2Permission`` or an ``AppRole``. Possible values are ``Scope`` or ``Role``.

        :schema: ResourceAccessDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6396054155d6a0d4d3d3efe54667511887b16a074cb386f559bde3f17b2ab56c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "type": type,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier for one of the ``OAuth2Permission`` or ``AppRole`` instances that the resource application exposes.

        :schema: ResourceAccessDefinition#Id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Specifies whether the ``id`` property references an ``OAuth2Permission`` or an ``AppRole``.

        Possible values are ``Scope`` or ``Role``.

        :schema: ResourceAccessDefinition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceAccessDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.TimeoutsDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class TimeoutsDefinition:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: 
        :param delete: 
        :param read: 
        :param update: 

        :schema: TimeoutsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ede5a130dfbb3a67bbfb47ce52c7ad63613a8bdc353347f07ef6be59793c2a)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Delete
        '''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Read
        '''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''
        :schema: TimeoutsDefinition#Update
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeoutsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-azuread-application.WebDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "homepage_url": "homepageUrl",
        "implicit_grant": "implicitGrant",
        "logout_url": "logoutUrl",
        "redirect_uris": "redirectUris",
    },
)
class WebDefinition:
    def __init__(
        self,
        *,
        homepage_url: typing.Optional[builtins.str] = None,
        implicit_grant: typing.Optional[typing.Sequence[typing.Union[ImplicitGrantDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        logout_url: typing.Optional[builtins.str] = None,
        redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param homepage_url: Home page or landing page of the application.
        :param implicit_grant: 
        :param logout_url: The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols.
        :param redirect_uris: A list of URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

        :schema: WebDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f193440fa0fcd2d1426cc10210b4e7ee3bb67f7dc29e202decbb609c57b587c)
            check_type(argname="argument homepage_url", value=homepage_url, expected_type=type_hints["homepage_url"])
            check_type(argname="argument implicit_grant", value=implicit_grant, expected_type=type_hints["implicit_grant"])
            check_type(argname="argument logout_url", value=logout_url, expected_type=type_hints["logout_url"])
            check_type(argname="argument redirect_uris", value=redirect_uris, expected_type=type_hints["redirect_uris"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if homepage_url is not None:
            self._values["homepage_url"] = homepage_url
        if implicit_grant is not None:
            self._values["implicit_grant"] = implicit_grant
        if logout_url is not None:
            self._values["logout_url"] = logout_url
        if redirect_uris is not None:
            self._values["redirect_uris"] = redirect_uris

    @builtins.property
    def homepage_url(self) -> typing.Optional[builtins.str]:
        '''Home page or landing page of the application.

        :schema: WebDefinition#HomepageUrl
        '''
        result = self._values.get("homepage_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def implicit_grant(self) -> typing.Optional[typing.List[ImplicitGrantDefinition]]:
        '''
        :schema: WebDefinition#ImplicitGrant
        '''
        result = self._values.get("implicit_grant")
        return typing.cast(typing.Optional[typing.List[ImplicitGrantDefinition]], result)

    @builtins.property
    def logout_url(self) -> typing.Optional[builtins.str]:
        '''The URL that will be used by Microsoft's authorization service to sign out a user using front-channel, back-channel or SAML logout protocols.

        :schema: WebDefinition#LogoutUrl
        '''
        result = self._values.get("logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.

        :schema: WebDefinition#RedirectUris
        '''
        result = self._values.get("redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessTokenDefinition",
    "ApiDefinition",
    "AppRoleDefinition",
    "CfnApplication",
    "CfnApplicationProps",
    "IdTokenDefinition",
    "ImplicitGrantDefinition",
    "Oauth2PermissionScopeDefinition",
    "Oauth2PermissionsDefinition",
    "OptionalClaimsDefinition",
    "RequiredResourceAccessDefinition",
    "ResourceAccessDefinition",
    "TimeoutsDefinition",
    "WebDefinition",
]

publication.publish()

def _typecheckingstub__75e5d187257a6b0108253ad50bf708d3abe812b7f2e1d7bdd27b879163b72da6(
    *,
    name: builtins.str,
    additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
    essential: typing.Optional[builtins.bool] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f957dd1f84bf03df1075e59634ff5501afdc5a00665d41231883e0dae7d9be6(
    *,
    oauth2_permission_scope: typing.Optional[typing.Sequence[typing.Union[Oauth2PermissionScopeDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b6a2a5d9ec9b2fb7922fedec87015633be67a3777835dcfa25403f7e0bf203(
    *,
    allowed_member_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    id: typing.Optional[builtins.str] = None,
    is_enabled: typing.Optional[builtins.bool] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__950d3eb1a0fdd146244959f4147ec0b5491013121b6d268b236e5bba7fca77e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: typing.Optional[typing.Sequence[typing.Union[ApiDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    app_role: typing.Optional[typing.Sequence[typing.Union[AppRoleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    available_to_other_tenants: typing.Optional[builtins.bool] = None,
    display_name: typing.Optional[builtins.str] = None,
    fallback_public_client_enabled: typing.Optional[builtins.bool] = None,
    group_membership_claims: typing.Optional[builtins.str] = None,
    homepage: typing.Optional[builtins.str] = None,
    identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    logout_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    oauth2_allow_implicit_flow: typing.Optional[builtins.bool] = None,
    oauth2_permissions: typing.Optional[typing.Sequence[typing.Union[Oauth2PermissionsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    optional_claims: typing.Optional[typing.Sequence[typing.Union[OptionalClaimsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    prevent_duplicate_names: typing.Optional[builtins.bool] = None,
    public_client: typing.Optional[builtins.bool] = None,
    reply_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    required_resource_access: typing.Optional[typing.Sequence[typing.Union[RequiredResourceAccessDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    sign_in_audience: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[TimeoutsDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    web: typing.Optional[typing.Sequence[typing.Union[WebDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c5fe466db4cfe807e9bc725b1cfa495d39f25a6dd0300fa8dae4e9420f5adf(
    *,
    api: typing.Optional[typing.Sequence[typing.Union[ApiDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    app_role: typing.Optional[typing.Sequence[typing.Union[AppRoleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    available_to_other_tenants: typing.Optional[builtins.bool] = None,
    display_name: typing.Optional[builtins.str] = None,
    fallback_public_client_enabled: typing.Optional[builtins.bool] = None,
    group_membership_claims: typing.Optional[builtins.str] = None,
    homepage: typing.Optional[builtins.str] = None,
    identifier_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    logout_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    oauth2_allow_implicit_flow: typing.Optional[builtins.bool] = None,
    oauth2_permissions: typing.Optional[typing.Sequence[typing.Union[Oauth2PermissionsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    optional_claims: typing.Optional[typing.Sequence[typing.Union[OptionalClaimsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    prevent_duplicate_names: typing.Optional[builtins.bool] = None,
    public_client: typing.Optional[builtins.bool] = None,
    reply_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    required_resource_access: typing.Optional[typing.Sequence[typing.Union[RequiredResourceAccessDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    sign_in_audience: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[TimeoutsDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    web: typing.Optional[typing.Sequence[typing.Union[WebDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d162e7850a5aad08c30abbcd7f43470bdd4a07962e8866706b7506b431e89e(
    *,
    name: builtins.str,
    additional_properties: typing.Optional[typing.Sequence[builtins.str]] = None,
    essential: typing.Optional[builtins.bool] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8399bf204710effc75133b87c67735a052c26c89c52f3095331fa269ed9c91a(
    *,
    access_token_issuance_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27202c9e123ff76ef91849c43d561fe171a1165a7cb54cd561e9e2e2195928bd(
    *,
    id: builtins.str,
    admin_consent_description: typing.Optional[builtins.str] = None,
    admin_consent_display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    type: typing.Optional[builtins.str] = None,
    user_consent_description: typing.Optional[builtins.str] = None,
    user_consent_display_name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a48f3a002c17de32e8201b01e7450c4a7d8694430e9022b6be0403f8cf990d(
    *,
    admin_consent_description: typing.Optional[builtins.str] = None,
    admin_consent_display_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_enabled: typing.Optional[builtins.bool] = None,
    type: typing.Optional[builtins.str] = None,
    user_consent_description: typing.Optional[builtins.str] = None,
    user_consent_display_name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df164420c7ceaad106c7f21981ac427fa7628cb07910c8d07d6d9c2761ec5a71(
    *,
    access_token: typing.Optional[typing.Sequence[typing.Union[AccessTokenDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    id_token: typing.Optional[typing.Sequence[typing.Union[IdTokenDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__debae0db93edadb458253d402108d5561550171a62d703066a4d2fdfedbfb003(
    *,
    resource_app_id: builtins.str,
    resource_access: typing.Optional[typing.Sequence[typing.Union[ResourceAccessDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6396054155d6a0d4d3d3efe54667511887b16a074cb386f559bde3f17b2ab56c(
    *,
    id: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ede5a130dfbb3a67bbfb47ce52c7ad63613a8bdc353347f07ef6be59793c2a(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f193440fa0fcd2d1426cc10210b4e7ee3bb67f7dc29e202decbb609c57b587c(
    *,
    homepage_url: typing.Optional[builtins.str] = None,
    implicit_grant: typing.Optional[typing.Sequence[typing.Union[ImplicitGrantDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    logout_url: typing.Optional[builtins.str] = None,
    redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
