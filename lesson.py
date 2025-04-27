def circle_area(pi):
    def cicle_calc(range):
        return pi * range * range
    return cicle_calc

fn1 = circle_area(3.14)
fn2 = circle_area(3.141592)

result1 = fn1(10)
result2 = fn2(10)

print(result1)
print(result2)