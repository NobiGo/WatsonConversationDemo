# coding:utf-8
import LogID
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import chardet

conversation = LogID.getConversation()
workspace_id = 'e98116f5-3573-49de-9dfd-96bc6509fbda'

# Replace with the context obtained from the initial request
context = {}


def getResult(conversation=conversation, workspace_id=workspace_id, textFile="口干"):
    response = conversation.message(
        workspace_id=workspace_id,
        message_input={"text": textFile},
        context=context
    )
    # print type(response["intents"])

    if response["intents"]:
        return response["intents"][0]["intent"]
    else:
        return None;


# 测试
print getResult(conversation, workspace_id,textFile="========")
