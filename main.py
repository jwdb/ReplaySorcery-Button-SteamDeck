class Plugin:
    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def RecordSorcerySave(self, *args):
        import os
        os.system("replay-sorcery save")

    async def RecordSorceryRestart(self, *args):
        import os
        os.system("nohup /home/deck/replay-sorcery-binary &")

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass