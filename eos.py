import numpy as np

# EOS for the crust

def h_crust1(P): #EOS for P between (9.34375e-5, 0.184)
    if P < 0:
        P = 0
    result = 0.00873 + 103.17338*(1-np.exp(-P/0.38527)) + 7.34979*(1-np.exp(-P/0.01211))
    return result

def h_crust2(P): #EOS for P between (4.1725e-8, 9.34375e-5)
    if P < 0:
        P = 0
    result = 0.00015 + 0.00203*(1-np.exp(-P*344827.5)) + 0.10851*(1-np.exp(-P*7692.3076))
    return result


def h_crust3(P): #EOS for P between (1.44875e-11, 4.1725e-8)
    if P < 0:
        P = 0
    result = 0.0000051*(1-np.exp(-P*0.2373e10)) + 0.00014*(1-np.exp(-P*0.4020e8))
    return result

# EOS for the core -- Hadronic models

def h_MDI1_func(P):
    if P < 0:
        P = 0
    result = (4.1844*(P**0.81449)) + (95.00135*(P**0.31736))
    return result

def h_MDI2_func(P):
    if P < 0:
        P = 0
    result = (5.97365 * (P ** 0.77374)) + (89.24 * (P ** 0.30993))
    return result

def h_MDI3_func(P):
    if P < 0:
        P = 0
    result = (15.55 * (P ** 0.666)) + (76.71 * (P ** 0.247))
    return result

def h_MDI4_func(P):
    if P < 0:
        P = 0
    result = (25.99587 * (P ** 0.61209)) + (65.62193 * (P ** 0.15512))
    return result

def h_NLD_func(P):
    if P < 0:
        P = 0
    result = 119.05736 + 304.80445 *(1-np.exp(-P/48.61465)) + 33722.34448 *(1-np.exp(-P/17499.47411))
    return result

def h_HHJ1_func(P):
    if P < 0:
        P = 0
    result = (1.78429 * (P ** 0.93761)) + (106.93652 * (P ** 0.31715))
    return result

def h_HHJ2_func(P):
    if P < 0:
        P = 0
    result = (1.18961 * (P ** 0.96539)) + (108.40302 * (P ** 0.31264))
    return result

def h_Ska_func(P):
    if P < 0:
        P=0
    result = (0.53928 * (P ** 1.01394)) + (94.31452 * (P ** 0.35135))
    return result

def h_Sk14_func(P):
    if P < 0:
        P = 0
    result = (4.75668 * (P ** 0.76537)) + (105.722 * (P ** 0.2745))
    return result

def h_HLPS2_func(P):
    if P < 0:
        P = 0
    result = 172.858*(1-np.exp(-P/22.8644)) + 2777.75*(1-np.exp(-P/1909.97)) + 161.553
    return result

def h_SCVBB_func(P):
    if P < 0:
        P = 0
    result = (0.371414 * (P ** 1.08004)) + (109.258 * (P ** 0.351019))
    return result

def h_W_func(P):
    if P < 0:
        P = 0
    result = (0.261822 * (P ** 1.16851)) + (92.4893 * (P ** 0.307728))
    return result

def h_BGP_func(P):
    if P < 0:
        P = 0
    result = (0.0112475 * (P ** 1.59689)) + (102.302 * (P ** 0.335526))
    return result

def h_BL1_func(P):
    if P < 0:
        P = 0
    result = (0.488686 * (P ** 1.01457)) + (102.26 * (P ** 0.355095))
    return result

def h_BL2_func(P):
    if P < 0:
        P = 0
    result = (1.34241 * (P ** 0.910079)) + (100.756 * (P ** 0.354129))
    return result

def h_DH_func(P):
    if P < 0:
        P = 0
    result = (39.5021 * (P ** 0.541485)) + (96.0528 * (P ** 0.00401285))
    return result

def h_APR1_func(P):
    if P < 0:
        P = 0
    result = (0.000719964 * (P ** 1.85898)) + (108.975 * (P ** 0.340074))
    return result
