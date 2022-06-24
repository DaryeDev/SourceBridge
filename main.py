from sourceBridge import SourceBridge
SourceBridge = SourceBridge()

if SourceBridge.compatibleGameRunning:
    while True:
        try:
            SourceBridge.run(input("> "))
        except Exception as e:
            print(e)