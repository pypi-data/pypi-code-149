import asyncio
import threading

from kordar_task import write_logger


class AsyncTaskHandler:

    def __init__(self, work_size=5, queue_buff_len=20):
        self.__container = {}
        self.__worker_pool_size = work_size
        self.__task_queue_buff_len = queue_buff_len
        self.__task_queue = asyncio.Queue(queue_buff_len)

    def start_work_pool(self, name=None):

        async def __do_msg_handler(body):
            """
            获取处理器，并执行
            :param body:
            :return:
            """
            target = self.__container.get(body.task_id())
            if target is not None:
                await target.execute(body)
            else:
                write_logger('kordar_task[%s] is not FOUND!' % body.task_id(), t="warning")

        async def start_one_worker(q, index):
            """
            启动一个Worker工作流
            :return:
            """
            write_logger("Worker ID = %s is started." % index)
            while True:
                try:
                    # 有消息则取出队列的Request，并执行绑定的业务方法
                    body = await q.get()
                    if body is None:
                        # None is the signal to stop.
                        write_logger("worker %s body is empty!" % index, "debug")
                        q.task_done()
                        continue
                    else:
                        write_logger("worker is running, this id is %s" % index, "debug")
                        await __do_msg_handler(body)
                        q.task_done()
                        await asyncio.sleep(0.05)
                except Exception as e:
                    write_logger('except: %s' % e, t="error")

        async def main():
            """
            启动worker工作池
            :return:
            """
            async with asyncio.TaskGroup() as tg:
                for index in range(self.__worker_pool_size):
                    tg.create_task(start_one_worker(self.__task_queue, index))

        def run():
            asyncio.run(main())

        t = threading.Thread(target=run, name=name)
        t.daemon = True
        t.start()


    def send(self, body):
        self.__task_queue.put_nowait(body)

    def add_task(self, task_obj):
        task_id = task_obj.id()
        if task_id in self.__container:
            raise ValueError('repeated func , taskId =  %s' % task_id)
        # 添加msg与api的绑定关系
        self.__container[task_id] = task_obj
        write_logger("Add func taskId = %s" % task_id)

    def close(self):
        pass
