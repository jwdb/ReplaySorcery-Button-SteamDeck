class Plugin:
    import subprocess
    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def RecordSorcerySave(self, *args):
        subprocess.run(["replay-sorcery", "save"])


    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass