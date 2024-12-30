from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Author(BaseModel):
    name: str
    email: str
    date: str


class Committer(BaseModel):
    name: str
    email: str
    date: str


class Tree(BaseModel):
    sha: str
    url: str


class Verification(BaseModel):
    verified: bool
    reason: str
    signature: str
    payload: str
    verified_at: str


class Commit(BaseModel):
    author: Author
    committer: Committer
    message: str
    tree: Tree
    url: str
    comment_count: int
    verification: Verification


class Author1(BaseModel):
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


class Committer1(BaseModel):
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


class Parent(BaseModel):
    sha: str
    url: str
    html_url: str


class RepoOneCommitInfoModel(BaseModel):
    sha: Optional[str] = None
    node_id: Optional[str] = None
    commit: Optional[Commit] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    comments_url: Optional[str] = None
    author: Optional[Author1] = None
    committer: Optional[Committer1] = None
    parents: Optional[List[Parent]] = None
