import os
from pathlib import Path
import sys
from dotenv import load_dotenv
import supervisely_lib as sly


root_source_dir = str(Path(sys.argv[0]).parents[1])
print(f"App source directory: {root_source_dir}")
sys.path.append(root_source_dir)

# only for convenient debug
debug_env_path = os.path.join(root_source_dir, "debug.env")
secret_debug_env_path = os.path.join(root_source_dir, "secret_debug.env")
load_dotenv(debug_env_path)
load_dotenv(secret_debug_env_path, override=True)

my_app = sly.AppService()
api = my_app.public_api
task_id = my_app.task_id

#@TODO: for debug
#sly.fs.clean_dir(my_app.data_dir)

team_id = int(os.environ['context.teamId'])
workspace_id = int(os.environ['context.workspaceId'])
project_id = int(os.environ['modal.state.slyProjectId'])

user_id = int(os.environ['context.userId'])
user_login = os.environ['context.userLogin']

project_info = api.project.get_info_by_id(project_id)
if project_info is None:  # for debug
    raise ValueError(f"Project with id={project_id} not found")
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))

dataset_infos = []
video_infos = []
for dataset in api.dataset.get_list(project_id):
    dataset_infos.append(dataset)
    video_infos.append(api.video.get_list(dataset.id))


