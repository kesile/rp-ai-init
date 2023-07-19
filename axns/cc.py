def cc():
    cc = input("\nAre you creating campaign posts? (Y/N) ")
    if cc.lower() == "y": cc = True
    else: cc = False
    return cc