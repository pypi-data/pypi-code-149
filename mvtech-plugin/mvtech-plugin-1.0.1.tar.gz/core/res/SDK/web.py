from fastapi import FastAPI
import typing
import uvicorn

try:
    from . import models
    from .base import clearLog, checkModel, log
except Exception:
    import models
    from base import clearLog, checkModel, log

app = FastAPI(title="MVTECH",
              version="0.0.1",
              description="自写sdk, 增加 test接口可以测试适配器，适配器并不为单例的，第一执行的组件")

# web 调用　自写方法　关键
plugins = None


class Server(object):

    def __init__(self, plus):

        global plugins
        plugins = plus

    @staticmethod
    @app.post("/actions/{action_name}")
    def actions(
            action_name,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL] = None):

        clearLog()

        action = plugins.actions[action_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        input_data = data_body.get("input_data")
        adapter_data = data_body.get("adapter_data")

        # 执行 外部run 相关操作
        output = action._run(input_data, adapter_data)

        return output

    @staticmethod
    @app.post("/actions/{action_name}/test")
    def actions_test(
            action_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL] = None):

        clearLog()

        action = plugins.actions[action_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        adapter_data = data_body.get("adapter_data")

        output = action._test(adapter_data)

        return output

    @staticmethod
    @app.post("/triggers/{trigger_name}")
    def triggers(trigger_name: str,
                 baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL]):

        clearLog()

        # 外部类
        trigger = plugins.triggers[trigger_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        input_data = data_body.get("input_data")
        adapter_data = data_body.get("adapter_data")
        next_step = data_body.get("nextStep")
        # 执行　外部run 相关操作
        output = trigger._run(input_data, adapter_data, next_step)

        return output

    @staticmethod
    @app.post("/triggers/{trigger_name}/test")
    def trigger_test(
            trigger_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL] = None):

        clearLog()

        # 外部类
        trigger = plugins.triggers[trigger_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        adapter_data = data_body.get("adapter_data")
        output = trigger._test(adapter_data)

        return output

    @staticmethod
    @app.post("/alarm_receivers/{alarm_receiver_name}")
    def alarm_receivers(
            alarm_receiver_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL]):

        clearLog()

        # 外部类
        alarm_receiver = plugins.alarm_receivers[alarm_receiver_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        input_data = data_body.get("input_data")
        adapter_data = data_body.get("adapter_data")
        # dispatcher_url = data_body.get("dispatcher").get("url")
        next_step = data_body.get("nextStep")
        # 执行　外部run 相关操作
        output = alarm_receiver._run(input_data, adapter_data, next_step)

        return output

    @staticmethod
    @app.post("/alarm_receivers/{alarm_receiver_name}/test")
    def alarm_receivers_test(
            alarm_receiver_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL] = None):

        clearLog()

        # 外部类
        alarm_receiver = plugins.alarm_receivers[alarm_receiver_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        adapter_data = data_body.get("adapter_data")

        output = alarm_receiver._test(adapter_data)

        return output

    @staticmethod
    @app.post("/indicator_receivers/{indicator_receiver_name}")
    def indicator_receivers(
            indicator_receiver_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL]):

        clearLog()

        # 外部类
        indicator_receiver = plugins.indicator_receivers[
            indicator_receiver_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        input_data = data_body.get("input_data")
        adapter_data = data_body.get("adapter_data")
        # dispatcher_url = data_body.get("dispatcher").get("url")
        next_step = data_body.get("nextStep")
        # 执行　外部run 相关操作
        output = indicator_receiver._run(input_data, adapter_data, next_step)

        return output

    @staticmethod
    @app.post("/indicator_receivers/{indicator_receiver_name}/test")
    def indicator_receivers_test(
            indicator_receiver_name: str,
            baseInputMdl: typing.Optional[models.PLUGIN_BASE_MODEL] = None):

        clearLog()

        # 外部类
        indicator_receiver = plugins.indicator_receivers[
            indicator_receiver_name]

        # 取出body
        data = baseInputMdl.dict()
        checkModel(data, models.PLUGIN_BASE_MODEL)
        data_body = data.get("body")

        # 获取input
        adapter_data = data_body.get("adapter_data")

        output = indicator_receiver._test(adapter_data)

        return output

    def runserver(self):
        portV = 8888
        log("attention", f"mvtech web start  http://0.0.0.0:{portV}/docs#")
        uvicorn.run(app, host="0.0.0.0", port=portV)
