def st(uq, content, stage, count=0):
    if uq:
        if stage == "inPo":
            print("\nInitial Post Generated\n---\n")
        elif stage == "inFe":
            print("\nInitial Feedback Generated\n---\n")
        elif stage == "rePo":
            print(f"\nPost Iteration #{count} Generated\n---\n")
        elif stage == "reFe":
            print(f"\nFeedback Iteration #{count} Generated\n---\n")
        elif stage == "fiPo":
            print(f"\nFinalized Post Generated\n---\n")
        else: print("Invalid Status")
        print(content)
    else: pass