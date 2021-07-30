def cross(u:complex,v:complex) -> complex:
    return u.real * v.imag - u.imag * v.real

golden_ratio = (5**.5 - 1)/2
inverse_golden_ratio = 1-golden_ratio