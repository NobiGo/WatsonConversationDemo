# coding:utf-8
import LogID
import json

conversation = LogID.getConversation()

# 获取Workspaces列表
def get_workspaces_list(conversation = conversation):
    workspaces = conversation.list_workspaces()
    jsonFile = json.dumps(workspaces, indent=2)
    print(jsonFile)
    print ("================获取Workspaces列表成功==================")
    return jsonFile

# 创建Workspaces列表
# conversation.create_workspace
#

get_workspaces_list(LogID.getConversation())
