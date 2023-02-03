'''
# tf-github-repository

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::GitHub::Repository` v1.0.0.

## Description

This resource allows you to create and manage repositories within your
GitHub organization or personal account.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/github/TF-GitHub-Repository/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::GitHub::Repository \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-GitHub-Repository \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::GitHub::Repository`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-github-repository+v1.0.0).
* Issues related to `TF::GitHub::Repository` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/github/TF-GitHub-Repository/docs/README.md).

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


class CfnRepository(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-github-repository.CfnRepository",
):
    '''A CloudFormation ``TF::GitHub::Repository``.

    :cloudformationResource: TF::GitHub::Repository
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        allow_merge_commit: typing.Optional[builtins.bool] = None,
        allow_rebase_merge: typing.Optional[builtins.bool] = None,
        allow_squash_merge: typing.Optional[builtins.bool] = None,
        archived: typing.Optional[builtins.bool] = None,
        archive_on_destroy: typing.Optional[builtins.bool] = None,
        auto_init: typing.Optional[builtins.bool] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[builtins.bool] = None,
        has_issues: typing.Optional[builtins.bool] = None,
        has_projects: typing.Optional[builtins.bool] = None,
        has_wiki: typing.Optional[builtins.bool] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[builtins.bool] = None,
        license_template: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Sequence[typing.Union["PagesDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        private: typing.Optional[builtins.bool] = None,
        template: typing.Optional[typing.Sequence[typing.Union["TemplateDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Create a new ``TF::GitHub::Repository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the repository.
        :param allow_merge_commit: Set to ``false`` to disable merge commits on the repository.
        :param allow_rebase_merge: Set to ``false`` to disable rebase merges on the repository.
        :param allow_squash_merge: Set to ``false`` to disable squash merges on the repository.
        :param archived: Specifies if the repository should be archived. Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving. Default: false`. **NOTE** Currently, the API does not support unarchiving.
        :param archive_on_destroy: Set to ``true`` to archive the repository instead of deleting on destroy.
        :param auto_init: Set to ``true`` to produce an initial commit in the repository.
        :param default_branch: (Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created, and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the initial repository creation and create the target branch inside of the repository prior to setting this attribute.
        :param delete_branch_on_merge: Automatically delete head branch after a pull request is merged. Defaults to ``false``. Default: false`.
        :param description: A description of the repository.
        :param gitignore_template: Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".
        :param has_downloads: Set to ``true`` to enable the (deprecated) downloads features on the repository.
        :param has_issues: Set to ``true`` to enable the GitHub Issues features on the repository.
        :param has_projects: Set to ``true`` to enable the GitHub Projects features on the repository. Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.
        :param has_wiki: Set to ``true`` to enable the GitHub Wiki features on the repository.
        :param homepage_url: URL of a page describing the project.
        :param is_template: Set to ``true`` to tell GitHub that this is a template repository.
        :param license_template: Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".
        :param pages: 
        :param private: Set to ``true`` to create a private repository. Repositories are created as public (e.g. open source) by default.
        :param template: 
        :param topics: The list of topics of the repository.
        :param visibility: Can be ``public`` or ``private``. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.
        :param vulnerability_alerts: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1efa50e86034a9819934cb1beb1d570d13ec9e49da17384dcc8c1e01f91eba43)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryProps(
            name=name,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            archive_on_destroy=archive_on_destroy,
            auto_init=auto_init,
            default_branch=default_branch,
            delete_branch_on_merge=delete_branch_on_merge,
            description=description,
            gitignore_template=gitignore_template,
            has_downloads=has_downloads,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            homepage_url=homepage_url,
            is_template=is_template,
            license_template=license_template,
            pages=pages,
            private=private,
            template=template,
            topics=topics,
            visibility=visibility,
            vulnerability_alerts=vulnerability_alerts,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEtag")
    def attr_etag(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.Etag``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEtag"))

    @builtins.property
    @jsii.member(jsii_name="attrFullName")
    def attr_full_name(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.FullName``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFullName"))

    @builtins.property
    @jsii.member(jsii_name="attrGitCloneUrl")
    def attr_git_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.GitCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGitCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrHtmlUrl")
    def attr_html_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.HtmlUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHtmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrHttpCloneUrl")
    def attr_http_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.HttpCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHttpCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeId")
    def attr_node_id(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.NodeId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNodeId"))

    @builtins.property
    @jsii.member(jsii_name="attrRepoId")
    def attr_repo_id(self) -> jsii.Number:
        '''Attribute ``TF::GitHub::Repository.RepoId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRepoId"))

    @builtins.property
    @jsii.member(jsii_name="attrSshCloneUrl")
    def attr_ssh_clone_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.SshCloneUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrSvnUrl")
    def attr_svn_url(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.SvnUrl``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSvnUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::GitHub::Repository.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnRepositoryProps":
        '''Resource props.'''
        return typing.cast("CfnRepositoryProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allow_merge_commit": "allowMergeCommit",
        "allow_rebase_merge": "allowRebaseMerge",
        "allow_squash_merge": "allowSquashMerge",
        "archived": "archived",
        "archive_on_destroy": "archiveOnDestroy",
        "auto_init": "autoInit",
        "default_branch": "defaultBranch",
        "delete_branch_on_merge": "deleteBranchOnMerge",
        "description": "description",
        "gitignore_template": "gitignoreTemplate",
        "has_downloads": "hasDownloads",
        "has_issues": "hasIssues",
        "has_projects": "hasProjects",
        "has_wiki": "hasWiki",
        "homepage_url": "homepageUrl",
        "is_template": "isTemplate",
        "license_template": "licenseTemplate",
        "pages": "pages",
        "private": "private",
        "template": "template",
        "topics": "topics",
        "visibility": "visibility",
        "vulnerability_alerts": "vulnerabilityAlerts",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        allow_merge_commit: typing.Optional[builtins.bool] = None,
        allow_rebase_merge: typing.Optional[builtins.bool] = None,
        allow_squash_merge: typing.Optional[builtins.bool] = None,
        archived: typing.Optional[builtins.bool] = None,
        archive_on_destroy: typing.Optional[builtins.bool] = None,
        auto_init: typing.Optional[builtins.bool] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[builtins.bool] = None,
        has_issues: typing.Optional[builtins.bool] = None,
        has_projects: typing.Optional[builtins.bool] = None,
        has_wiki: typing.Optional[builtins.bool] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        is_template: typing.Optional[builtins.bool] = None,
        license_template: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Sequence[typing.Union["PagesDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        private: typing.Optional[builtins.bool] = None,
        template: typing.Optional[typing.Sequence[typing.Union["TemplateDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This resource allows you to create and manage repositories within your GitHub organization or personal account.

        :param name: The name of the repository.
        :param allow_merge_commit: Set to ``false`` to disable merge commits on the repository.
        :param allow_rebase_merge: Set to ``false`` to disable rebase merges on the repository.
        :param allow_squash_merge: Set to ``false`` to disable squash merges on the repository.
        :param archived: Specifies if the repository should be archived. Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving. Default: false`. **NOTE** Currently, the API does not support unarchiving.
        :param archive_on_destroy: Set to ``true`` to archive the repository instead of deleting on destroy.
        :param auto_init: Set to ``true`` to produce an initial commit in the repository.
        :param default_branch: (Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created, and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the initial repository creation and create the target branch inside of the repository prior to setting this attribute.
        :param delete_branch_on_merge: Automatically delete head branch after a pull request is merged. Defaults to ``false``. Default: false`.
        :param description: A description of the repository.
        :param gitignore_template: Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".
        :param has_downloads: Set to ``true`` to enable the (deprecated) downloads features on the repository.
        :param has_issues: Set to ``true`` to enable the GitHub Issues features on the repository.
        :param has_projects: Set to ``true`` to enable the GitHub Projects features on the repository. Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.
        :param has_wiki: Set to ``true`` to enable the GitHub Wiki features on the repository.
        :param homepage_url: URL of a page describing the project.
        :param is_template: Set to ``true`` to tell GitHub that this is a template repository.
        :param license_template: Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".
        :param pages: 
        :param private: Set to ``true`` to create a private repository. Repositories are created as public (e.g. open source) by default.
        :param template: 
        :param topics: The list of topics of the repository.
        :param visibility: Can be ``public`` or ``private``. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.
        :param vulnerability_alerts: 

        :schema: CfnRepositoryProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd04612ca22f8a576a39eeb53ba51034bdaf18f4e184e6b92d8bb5f7bfd6256)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_merge_commit", value=allow_merge_commit, expected_type=type_hints["allow_merge_commit"])
            check_type(argname="argument allow_rebase_merge", value=allow_rebase_merge, expected_type=type_hints["allow_rebase_merge"])
            check_type(argname="argument allow_squash_merge", value=allow_squash_merge, expected_type=type_hints["allow_squash_merge"])
            check_type(argname="argument archived", value=archived, expected_type=type_hints["archived"])
            check_type(argname="argument archive_on_destroy", value=archive_on_destroy, expected_type=type_hints["archive_on_destroy"])
            check_type(argname="argument auto_init", value=auto_init, expected_type=type_hints["auto_init"])
            check_type(argname="argument default_branch", value=default_branch, expected_type=type_hints["default_branch"])
            check_type(argname="argument delete_branch_on_merge", value=delete_branch_on_merge, expected_type=type_hints["delete_branch_on_merge"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument gitignore_template", value=gitignore_template, expected_type=type_hints["gitignore_template"])
            check_type(argname="argument has_downloads", value=has_downloads, expected_type=type_hints["has_downloads"])
            check_type(argname="argument has_issues", value=has_issues, expected_type=type_hints["has_issues"])
            check_type(argname="argument has_projects", value=has_projects, expected_type=type_hints["has_projects"])
            check_type(argname="argument has_wiki", value=has_wiki, expected_type=type_hints["has_wiki"])
            check_type(argname="argument homepage_url", value=homepage_url, expected_type=type_hints["homepage_url"])
            check_type(argname="argument is_template", value=is_template, expected_type=type_hints["is_template"])
            check_type(argname="argument license_template", value=license_template, expected_type=type_hints["license_template"])
            check_type(argname="argument pages", value=pages, expected_type=type_hints["pages"])
            check_type(argname="argument private", value=private, expected_type=type_hints["private"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
            check_type(argname="argument vulnerability_alerts", value=vulnerability_alerts, expected_type=type_hints["vulnerability_alerts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if allow_merge_commit is not None:
            self._values["allow_merge_commit"] = allow_merge_commit
        if allow_rebase_merge is not None:
            self._values["allow_rebase_merge"] = allow_rebase_merge
        if allow_squash_merge is not None:
            self._values["allow_squash_merge"] = allow_squash_merge
        if archived is not None:
            self._values["archived"] = archived
        if archive_on_destroy is not None:
            self._values["archive_on_destroy"] = archive_on_destroy
        if auto_init is not None:
            self._values["auto_init"] = auto_init
        if default_branch is not None:
            self._values["default_branch"] = default_branch
        if delete_branch_on_merge is not None:
            self._values["delete_branch_on_merge"] = delete_branch_on_merge
        if description is not None:
            self._values["description"] = description
        if gitignore_template is not None:
            self._values["gitignore_template"] = gitignore_template
        if has_downloads is not None:
            self._values["has_downloads"] = has_downloads
        if has_issues is not None:
            self._values["has_issues"] = has_issues
        if has_projects is not None:
            self._values["has_projects"] = has_projects
        if has_wiki is not None:
            self._values["has_wiki"] = has_wiki
        if homepage_url is not None:
            self._values["homepage_url"] = homepage_url
        if is_template is not None:
            self._values["is_template"] = is_template
        if license_template is not None:
            self._values["license_template"] = license_template
        if pages is not None:
            self._values["pages"] = pages
        if private is not None:
            self._values["private"] = private
        if template is not None:
            self._values["template"] = template
        if topics is not None:
            self._values["topics"] = topics
        if visibility is not None:
            self._values["visibility"] = visibility
        if vulnerability_alerts is not None:
            self._values["vulnerability_alerts"] = vulnerability_alerts

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the repository.

        :schema: CfnRepositoryProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_merge_commit(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable merge commits on the repository.

        :schema: CfnRepositoryProps#AllowMergeCommit
        '''
        result = self._values.get("allow_merge_commit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_rebase_merge(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable rebase merges on the repository.

        :schema: CfnRepositoryProps#AllowRebaseMerge
        '''
        result = self._values.get("allow_rebase_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_squash_merge(self) -> typing.Optional[builtins.bool]:
        '''Set to ``false`` to disable squash merges on the repository.

        :schema: CfnRepositoryProps#AllowSquashMerge
        '''
        result = self._values.get("allow_squash_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def archived(self) -> typing.Optional[builtins.bool]:
        '''Specifies if the repository should be archived.

        Defaults to ``false``. **NOTE** Currently, the API does not support unarchiving.

        :default: false`. **NOTE** Currently, the API does not support unarchiving.

        :schema: CfnRepositoryProps#Archived
        '''
        result = self._values.get("archived")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def archive_on_destroy(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to archive the repository instead of deleting on destroy.

        :schema: CfnRepositoryProps#ArchiveOnDestroy
        '''
        result = self._values.get("archive_on_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_init(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to produce an initial commit in the repository.

        :schema: CfnRepositoryProps#AutoInit
        '''
        result = self._values.get("auto_init")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_branch(self) -> typing.Optional[builtins.str]:
        '''(Deprecated: Use ``github_branch_default`` resource instead) The name of the default branch of the repository.

        **NOTE:** This can only be set after a repository has already been created,
        and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
        initial repository creation and create the target branch inside of the repository prior to setting this attribute.

        :schema: CfnRepositoryProps#DefaultBranch
        '''
        result = self._values.get("default_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_branch_on_merge(self) -> typing.Optional[builtins.bool]:
        '''Automatically delete head branch after a pull request is merged.

        Defaults to ``false``.

        :default: false`.

        :schema: CfnRepositoryProps#DeleteBranchOnMerge
        '''
        result = self._values.get("delete_branch_on_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the repository.

        :schema: CfnRepositoryProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gitignore_template(self) -> typing.Optional[builtins.str]:
        '''Use the `name of the template <https://github.com/github/gitignore>`_ without the extension. For example, "Haskell".

        :schema: CfnRepositoryProps#GitignoreTemplate
        '''
        result = self._values.get("gitignore_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def has_downloads(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the (deprecated) downloads features on the repository.

        :schema: CfnRepositoryProps#HasDownloads
        '''
        result = self._values.get("has_downloads")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_issues(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Issues features on the repository.

        :schema: CfnRepositoryProps#HasIssues
        '''
        result = self._values.get("has_issues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_projects(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Projects features on the repository.

        Per the GitHub `documentation <https://developer.github.com/v3/repos/#create>`_ when in an organization that has disabled repository projects it will default to ``false`` and will otherwise default to ``true``. If you specify ``true`` when it has been disabled it will return an error.

        :schema: CfnRepositoryProps#HasProjects
        '''
        result = self._values.get("has_projects")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def has_wiki(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to enable the GitHub Wiki features on the repository.

        :schema: CfnRepositoryProps#HasWiki
        '''
        result = self._values.get("has_wiki")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def homepage_url(self) -> typing.Optional[builtins.str]:
        '''URL of a page describing the project.

        :schema: CfnRepositoryProps#HomepageUrl
        '''
        result = self._values.get("homepage_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_template(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to tell GitHub that this is a template repository.

        :schema: CfnRepositoryProps#IsTemplate
        '''
        result = self._values.get("is_template")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def license_template(self) -> typing.Optional[builtins.str]:
        '''Use the `name of the template <https://github.com/github/choosealicense.com/tree/gh-pages/_licenses>`_ without the extension. For example, "mit" or "mpl-2.0".

        :schema: CfnRepositoryProps#LicenseTemplate
        '''
        result = self._values.get("license_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pages(self) -> typing.Optional[typing.List["PagesDefinition"]]:
        '''
        :schema: CfnRepositoryProps#Pages
        '''
        result = self._values.get("pages")
        return typing.cast(typing.Optional[typing.List["PagesDefinition"]], result)

    @builtins.property
    def private(self) -> typing.Optional[builtins.bool]:
        '''Set to ``true`` to create a private repository.

        Repositories are created as public (e.g. open source) by default.

        :schema: CfnRepositoryProps#Private
        '''
        result = self._values.get("private")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def template(self) -> typing.Optional[typing.List["TemplateDefinition"]]:
        '''
        :schema: CfnRepositoryProps#Template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.List["TemplateDefinition"]], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of topics of the repository.

        :schema: CfnRepositoryProps#Topics
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Can be ``public`` or ``private``.

        If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, visibility can also be ``internal``. The ``visibility`` parameter overrides the ``private`` parameter.

        :schema: CfnRepositoryProps#Visibility
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vulnerability_alerts(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnRepositoryProps#VulnerabilityAlerts
        '''
        result = self._values.get("vulnerability_alerts")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.PagesDefinition",
    jsii_struct_bases=[],
    name_mapping={"cname": "cname", "source": "source"},
)
class PagesDefinition:
    def __init__(
        self,
        *,
        cname: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Sequence[typing.Union["SourceDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param cname: 
        :param source: 

        :schema: PagesDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__541952db18a705404ef2354b288826af4eb9877efa13dee489b339d1d2dbb023)
            check_type(argname="argument cname", value=cname, expected_type=type_hints["cname"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cname is not None:
            self._values["cname"] = cname
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def cname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: PagesDefinition#Cname
        '''
        result = self._values.get("cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[typing.List["SourceDefinition"]]:
        '''
        :schema: PagesDefinition#Source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.List["SourceDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.SourceDefinition",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "path": "path"},
)
class SourceDefinition:
    def __init__(
        self,
        *,
        branch: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: 
        :param path: 

        :schema: SourceDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0363051891bbb52dc69b55340f43d05cce6b0bf80c111ae979abb42844cb3789)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "branch": branch,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def branch(self) -> builtins.str:
        '''
        :schema: SourceDefinition#Branch
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SourceDefinition#Path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-github-repository.TemplateDefinition",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner", "repository": "repository"},
)
class TemplateDefinition:
    def __init__(self, *, owner: builtins.str, repository: builtins.str) -> None:
        '''
        :param owner: 
        :param repository: 

        :schema: TemplateDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6682b41f97b28f363e4a408bb896c92d00e1b4078f9917711cddbf1180302fd)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner": owner,
            "repository": repository,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''
        :schema: TemplateDefinition#Owner
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''
        :schema: TemplateDefinition#Repository
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRepository",
    "CfnRepositoryProps",
    "PagesDefinition",
    "SourceDefinition",
    "TemplateDefinition",
]

publication.publish()

def _typecheckingstub__1efa50e86034a9819934cb1beb1d570d13ec9e49da17384dcc8c1e01f91eba43(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    allow_merge_commit: typing.Optional[builtins.bool] = None,
    allow_rebase_merge: typing.Optional[builtins.bool] = None,
    allow_squash_merge: typing.Optional[builtins.bool] = None,
    archived: typing.Optional[builtins.bool] = None,
    archive_on_destroy: typing.Optional[builtins.bool] = None,
    auto_init: typing.Optional[builtins.bool] = None,
    default_branch: typing.Optional[builtins.str] = None,
    delete_branch_on_merge: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    gitignore_template: typing.Optional[builtins.str] = None,
    has_downloads: typing.Optional[builtins.bool] = None,
    has_issues: typing.Optional[builtins.bool] = None,
    has_projects: typing.Optional[builtins.bool] = None,
    has_wiki: typing.Optional[builtins.bool] = None,
    homepage_url: typing.Optional[builtins.str] = None,
    is_template: typing.Optional[builtins.bool] = None,
    license_template: typing.Optional[builtins.str] = None,
    pages: typing.Optional[typing.Sequence[typing.Union[PagesDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    private: typing.Optional[builtins.bool] = None,
    template: typing.Optional[typing.Sequence[typing.Union[TemplateDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    topics: typing.Optional[typing.Sequence[builtins.str]] = None,
    visibility: typing.Optional[builtins.str] = None,
    vulnerability_alerts: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd04612ca22f8a576a39eeb53ba51034bdaf18f4e184e6b92d8bb5f7bfd6256(
    *,
    name: builtins.str,
    allow_merge_commit: typing.Optional[builtins.bool] = None,
    allow_rebase_merge: typing.Optional[builtins.bool] = None,
    allow_squash_merge: typing.Optional[builtins.bool] = None,
    archived: typing.Optional[builtins.bool] = None,
    archive_on_destroy: typing.Optional[builtins.bool] = None,
    auto_init: typing.Optional[builtins.bool] = None,
    default_branch: typing.Optional[builtins.str] = None,
    delete_branch_on_merge: typing.Optional[builtins.bool] = None,
    description: typing.Optional[builtins.str] = None,
    gitignore_template: typing.Optional[builtins.str] = None,
    has_downloads: typing.Optional[builtins.bool] = None,
    has_issues: typing.Optional[builtins.bool] = None,
    has_projects: typing.Optional[builtins.bool] = None,
    has_wiki: typing.Optional[builtins.bool] = None,
    homepage_url: typing.Optional[builtins.str] = None,
    is_template: typing.Optional[builtins.bool] = None,
    license_template: typing.Optional[builtins.str] = None,
    pages: typing.Optional[typing.Sequence[typing.Union[PagesDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    private: typing.Optional[builtins.bool] = None,
    template: typing.Optional[typing.Sequence[typing.Union[TemplateDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    topics: typing.Optional[typing.Sequence[builtins.str]] = None,
    visibility: typing.Optional[builtins.str] = None,
    vulnerability_alerts: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__541952db18a705404ef2354b288826af4eb9877efa13dee489b339d1d2dbb023(
    *,
    cname: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Sequence[typing.Union[SourceDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0363051891bbb52dc69b55340f43d05cce6b0bf80c111ae979abb42844cb3789(
    *,
    branch: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6682b41f97b28f363e4a408bb896c92d00e1b4078f9917711cddbf1180302fd(
    *,
    owner: builtins.str,
    repository: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
