import os

import supervisely as sly

from dataset_tools.convert.coco import to_supervisely as coco_to_supervisely


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    raise NotImplementedError


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project_path = os.path.join(sly.app.get_data_dir(), "supervisely project")
    project_path = coco_to_supervisely(
        original_ds_names=["train2017", "val2017", "test2017"], dst_path=project_path
    )
    if project_path is not None:
        project_id, _ = sly.upload_project(
            dir=project_path,
            api=api,
            workspace_id=workspace_id,
            project_name=project_name,
            log_progress=True,
        )
        project_info = api.project.get_info_by_id(project_id)
        return project_info
