def decide_action(distance, battery):
    # Highest priority first: return ONE string
    if battery < 20:
        return "return_to_dock"
    if distance < 1:
        return "stop"
    if distance <= 3:
        return "slow_down"
    return "continue"

def is_safe_speed(distance, speed):
    return speed < distance / 2

def run_tests():
    print(decide_action(10, 80))   # expect: continue
    print(decide_action(0.5, 80))  # expect: stop
    print(decide_action(10, 15))   # expect: return_to_dock
    print(decide_action(3, 20))    # expect: slow_down
    print(decide_action(10, 20))   # expect: continue
    print(decide_action(0.5, 15))  # expect: stop
    print(is_safe_speed(10, 4))    # expect: True
    print(is_safe_speed(10, 5))    # expect: False
    print(is_safe_speed(10, 3))    # expect: True
    print(is_safe_speed(2, 3))    # expect: False
    for d, s in [(10, 4), (10, 5), (2, 3), (4, 1)]:
        print("distance", d, "speed", s, "->", is_safe_speed(d, s))
if __name__ == "__main__":
    run_tests()
