from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Owner(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: bool


class License(BaseModel):
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str


class Permissions(BaseModel):
    admin: bool
    maintain: bool
    push: bool
    triage: bool
    pull: bool


class Organization(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: bool


class RepoInfoModel(BaseModel):
    id: Optional[int] = None
    node_id: Optional[str] = None
    name: Optional[str] = None
    full_name: Optional[str] = None
    private: Optional[bool] = None
    owner: Optional[Owner] = None
    html_url: Optional[str] = None
    description: Optional[str] = None
    fork: Optional[bool] = None
    url: Optional[str] = None
    forks_url: Optional[str] = None
    keys_url: Optional[str] = None
    collaborators_url: Optional[str] = None
    teams_url: Optional[str] = None
    hooks_url: Optional[str] = None
    issue_events_url: Optional[str] = None
    events_url: Optional[str] = None
    assignees_url: Optional[str] = None
    branches_url: Optional[str] = None
    tags_url: Optional[str] = None
    blobs_url: Optional[str] = None
    git_tags_url: Optional[str] = None
    git_refs_url: Optional[str] = None
    trees_url: Optional[str] = None
    statuses_url: Optional[str] = None
    languages_url: Optional[str] = None
    stargazers_url: Optional[str] = None
    contributors_url: Optional[str] = None
    subscribers_url: Optional[str] = None
    subscription_url: Optional[str] = None
    commits_url: Optional[str] = None
    git_commits_url: Optional[str] = None
    comments_url: Optional[str] = None
    issue_comment_url: Optional[str] = None
    contents_url: Optional[str] = None
    compare_url: Optional[str] = None
    merges_url: Optional[str] = None
    archive_url: Optional[str] = None
    downloads_url: Optional[str] = None
    issues_url: Optional[str] = None
    pulls_url: Optional[str] = None
    milestones_url: Optional[str] = None
    notifications_url: Optional[str] = None
    labels_url: Optional[str] = None
    releases_url: Optional[str] = None
    deployments_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    pushed_at: Optional[str] = None
    git_url: Optional[str] = None
    ssh_url: Optional[str] = None
    clone_url: Optional[str] = None
    svn_url: Optional[str] = None
    homepage: Optional[str] = None
    size: Optional[int] = None
    stargazers_count: Optional[int] = None
    watchers_count: Optional[int] = None
    language: Optional[str] = None
    has_issues: Optional[bool] = None
    has_projects: Optional[bool] = None
    has_downloads: Optional[bool] = None
    has_wiki: Optional[bool] = None
    has_pages: Optional[bool] = None
    has_discussions: Optional[bool] = None
    forks_count: Optional[int] = None
    mirror_url: Optional[Any] = None
    archived: Optional[bool] = None
    disabled: Optional[bool] = None
    open_issues_count: Optional[int] = None
    license: Optional[License] = None
    allow_forking: Optional[bool] = None
    is_template: Optional[bool] = None
    web_commit_signoff_required: Optional[bool] = None
    topics: Optional[List[str]] = None
    visibility: Optional[str] = None
    forks: Optional[int] = None
    open_issues: Optional[int] = None
    watchers: Optional[int] = None
    default_branch: Optional[str] = None
    permissions: Optional[Permissions] = None
    temp_clone_token: Optional[str] = None
    custom_properties: Optional[Dict[str, Any]] = None
    organization: Optional[Organization] = None
    network_count: Optional[int] = None
    subscribers_count: Optional[int] = None
