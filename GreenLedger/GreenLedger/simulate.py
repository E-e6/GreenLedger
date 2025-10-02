import time, json

users = {"You": 0, "Alice": 25, "Bob": 20}

def add_action(user, points):
    users[user] += points
    log = {"user": user, "points": points, "total": users[user], "timestamp": time.time()}
    with open("log.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    print(f"✅ {user} earned {points} EcoCredits! Total: {users[user]}")

if __name__ == "__main__":
    add_action("You", 10)
    add_action("You", 5)
