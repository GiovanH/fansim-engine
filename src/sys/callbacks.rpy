init -1000 python:
    class CallbackManager():
        KNOWN_HOOKS = [
            "RouteStart",
            "RouteFinish"
        ]

        def __init__(self):
            self.callbacks = {h: [] for h in self.KNOWN_HOOKS}

        def add(self, hookname, fn):
            self.callbacks[hookname].append(fn)

        def on(self, hookname, *args, **kwargs):
            for fn in self.callbacks[hookname]:
                fn(*args, **kwargs)

    fse_callbacks = CallbackManager()