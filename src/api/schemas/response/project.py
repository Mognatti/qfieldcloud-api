from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Project(BaseModel):
    id: str
    name: str
    owner: str
    description: Optional[str] = None
    private: bool
    is_public: bool
    created_at: datetime
    updated_at: datetime
    data_last_packaged_at: Optional[datetime] = None
    data_last_updated_at: Optional[datetime] = None
    restricted_data_last_updated_at: Optional[datetime] = None
    can_repackage: bool
    needs_repackaging: bool
    status: str
    user_role: str
    user_role_origin: str
    shared_datasets_project_id: Optional[str] = None
    is_shared_datasets_project: bool
    is_featured: bool
    is_attachment_download_on_demand: bool
    file_storage_bytes: int
