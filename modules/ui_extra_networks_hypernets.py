import json
import os
import gradio as gr

from modules import shared, ui_extra_networks


class ExtraNetworksPageHypernetworks(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('Hypernetworks')

    def refresh(self, sagemaker_endpoint, request: gr.Request):
        shared.reload_hypernetworks(request)

    def list_items(self):
        for name, path in shared.hypernetworks.items():
            path, ext = os.path.splitext(path)

            yield {
                "name": name,
                "filename": path,
                "preview": self.find_preview(path),
                "description": self.find_description(path),
                "search_term": self.search_terms_from_path(path),
                "prompt": json.dumps(f"<hypernet:{name}:") + " + opts.extra_networks_default_multiplier + " + json.dumps(">"),
                "local_preview": f"{path}.preview.{shared.opts.samples_format}",
            }

    def allowed_directories_for_previews(self):
        return [shared.cmd_opts.hypernetwork_dir]
