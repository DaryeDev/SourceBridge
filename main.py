from sourceBridge import SourceBridge
SourceBridge = SourceBridge()

if SourceBridge.compatibleGameRunning:
    while True:
        try:
            command = input("> ")
            SourceBridge.run(command)
            if command in ["quit", "exit"]:
                break
        except Exception as e:
            print(e)