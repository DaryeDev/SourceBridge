import sourceBridge

while True:
    try:
        sourceBridge.run(input("> "))
    except Exception as e:
        print(e)