from pyteal import *

def approval_program():
    return Seq([
        App.globalPut(Bytes("EcoCredits"), Int(0)),
        Return(Int(1))
    ])

def clear_state_program():
    return Return(Int(1))

if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        f.write(compileTeal(approval_program(), mode=Mode.Application, version=6))
    with open("clear.teal", "w") as f:
        f.write(compileTeal(clear_state_program(), mode=Mode.Application, version=6))
    print("✅ PyTeal compiled to approval.teal and clear.teal")
