from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component

@xai_component(color="red")
class HelloNewLibrary(Component):

    def __init__(self):

        self.done = False

    def execute(self, ctx) -> None:
        
        import os 

        creator_name = os.getlogin()
        print("Hello, " + creator_name)

        self.done = True