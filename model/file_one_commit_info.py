from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class _Links(BaseModel):
    self: str
    git: str
    html: str


class FileOneCommitInfoModel(BaseModel):
    name: Optional[str] = None
    path: Optional[str] = None
    sha: Optional[str] = None
    size: Optional[int] = None
    url: Optional[str] = None
    html_url: Optional[str] = None
    git_url: Optional[str] = None
    download_url: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
    encoding: Optional[str] = None
    _links: Optional[_Links] = None
