def sqrt2(x, debug=False):
    from numpy import nan

    if x == 0:
        return 0
    elif x < 0:
        return nan

    s = 1.0
    kmax = 100
    tol = 1.0e-14

    for k in range(kmax):
        s0 = s
        s = 0.5 * (s + (x / s))
        delta_s = s - s0

        if abs(delta_s) / x < tol:
            break

    if debug:
        print(f"finally the value of function s={s:20.15f}")

    return s
