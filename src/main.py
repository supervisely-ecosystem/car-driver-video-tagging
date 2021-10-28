import sly_globals as g

import supervisely_lib as sly

# @my_app.callback("generate")
# @sly.timeit
# def generate_random_string(api: sly.Api, task_id, context, state, app_logger):
#     return


def main():
    sly.logger.info("Script arguments",  extra={}) # "length: ": LENGTH

    api = sly.Api.from_env()

    data = {
        "userId": g.user_id,
        "userLogin": g.user_login,
        "projectName": g.project_info.name,
        "datasetName": g.dataset_infos[g.dataset_index].name,
        "videoName": g.current_video.name,
    }

    state = {
        "videoId": g.current_video.id,
        "currentFrame": 0
    }

    initial_events = [
        # {
        #     "state": None,
        #     "context": None,
        #     "command": "preprocessing",
        # }
    ]

    # Run application service
    g.my_app.run(data=data, state=state, initial_events=initial_events)


if __name__ == "__main__":
    sly.main_wrapper("main", main)