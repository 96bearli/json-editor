def main(*args, **kwargs):
    import json_editor_ui
    return json_editor_ui.main(*args, **kwargs)


def reload_modules():
    import sys
    if sys.version_info.major >= 3:
        from importlib import reload
    else:
        from imp import reload
    
    import data_tree
    import batch_name
    import json_editor_dcc_core
    import json_editor_system
    import json_editor_ui
    reload(data_tree)
    reload(batch_name)
    reload(json_editor_dcc_core)
    reload(json_editor_system)
    reload(json_editor_ui)
    

def startup():
    # from maya import cmds
    # cmds.optionVar(query="") # example of finding a maya optionvar
    pass




