# -*- coding=utf-8 -*-
# @Author: Yangjie Li
import math
def method_1(a, b, c, d):
    S = a / (a + b + c)
    return S


def method_2(a, b, c, d):
    S = 2 * a / (2 * a + b + c)
    return S


def method_3(a, b, c, d):
    S = 2 * a / (2 * a + b + c)
    return S


def method_4(a, b, c, d):
    S = 3 * a / (3 * a + b + c)
    return S


def method_5(a, b, c, d):
    S = 2 * a / (2 * a + b + c)
    return S


def method_6(a, b, c, d):
    S = a / (a + 2 * b + 2 * c)
    return S


def method_7(a, b, c, d):
    S = (a + d) / (a + b + c + d)
    return S


def method_8(a, b, c, d):
    S = 2 * (a + d) / (2 * a + b + c + 2 * d)
    return S


def method_9(a, b, c, d):
    S = (a + d) / (a + 2 * b + 2 * c + d)
    return S


def method_10(a, b, c, d):
    S = (a + 0.5 * d) / (a + b + c + d)
    return S


def method_11(a, b, c, d):
    S = (a + d) / (a + 0.5 * b + 0.5 * c + d)
    return S


def method_12(a, b, c, d):
    S = a
    return S


def method_13(a, b, c, d):
    S = a + d
    return S


def method_14(a, b, c, d):
    S = a / (a + b + c + d)
    return S


def method_15(a, b, c, d):
    S = -(b + c)
    return S


def method_16(a, b, c, d):
    S = - (b + c) ** 0.5
    return S


def method_17(a, b, c, d):
    S = -((b + c) ** 2) ** 0.5
    return S


def method_18(a, b, c, d):
    S = -(b + c) ** (2 / 2)
    return S


def method_19(a, b, c, d):
    S = -(b + c)
    return S


def method_20(a, b, c, d):
    S = -(b + c) / (a + b + c + d)
    return S


def method_21(a, b, c, d):
    S = -(b + c)
    return S


def method_22(a, b, c, d):
    S = -(b + c) ** (1 / 1)
    return S


def method_23(a, b, c, d):
    S = -(b + c) / 4 * (a + b + c + d)
    return S


def method_24(a, b, c, d):
    S = -(b + c) ** 2 / (a + b + c + d) ** 2
    return S


def method_25(a, b, c, d):
    n = a + b + c + d
    S = -(n * (b + c) - (b - c) ** 2) / (a + b + c + d) ** 2
    return S


def method_26(a, b, c, d):
    S = -4 * b * c / (a + b + c + d) ** 2
    return S


def method_27(a, b, c, d):
    S = -(b + c) / (2 * a + b + c)
    return S


def method_28(a, b, c, d):
    S = -(b + c) / (2 * a + b + c)
    return S


def method_29(a, b, c, d):
    S = -2 * (1 - (a / ((a + b) * (a + c)) ** 0.5)) ** 0.5
    return S


def method_30(a, b, c, d):
    S = -(2 * (1 - (a / ((a + b) * (a + c)) ** 0.5))) ** 0.5
    return S


def method_31(a, b, c, d):
    S = a / (((a + b) * (a + c)) ** 0.5) ** 2
    return S


def method_32(a, b, c, d):
    n = a + b + c + d
    try:
        S = math.log(a) - math.log(n) - math.log((a + b) / n) - math.log((a + c) / n)
    except ValueError:
        S=0
    return S


def method_33(a, b, c, d):
    S = a / ((a + b) * (a + c)) ** 0.5
    return S


def method_34(a, b, c, d):
    n = a + b + c + d
    S = n * a / ((a + b) * (a + c))
    return S


def method_35(a, b, c, d):
    n = a + b + c + d
    S = n * (a - 0.5) ** 2 / ((a + b) * (a + c))
    return S


def method_36(a, b, c, d):
    S = a * a / ((a + b) * (a + c))
    return S


def method_37(a, b, c, d):
    try:
        S = a / (0.5 * (a * b + a * c) + b * c)
    except ZeroDivisionError:
        S = S = a / (0.5 * (a * b + a * c) + b * c + 1)  ####### mabin
    return S


def method_38(a, b, c, d):
    S = a / ((a + b) * (a + c)) ** 0.5
    return S


def method_39(a, b, c, d):
    S = ((a ** 2) - b * c) / ((a + b) * (a + c))
    return S


def method_40(a, b, c, d):
    n = a + b + c + d
    S = (n * a - (a + b) * (a + c)) / (n * a + (a + b) * (a + c))
    return S


def method_41(a, b, c, d):
    S = (0.5 * a * (2 * a + b + c)) / ((a + b) * (a + c))
    return S


def method_42(a, b, c, d):
    S = 0.5 * a * ((1 / (a + b)) + (1 / (a + c)))
    return S


def method_43(a, b, c, d):
    S = (a / (a + b)) + (a / (a + c))
    return S


def method_44(a, b, c, d):
    n = a + b + c + d
    S = (a * d - b * c) / ((n * (a + b) * (a + c)) ** 0.5)
    return S


def method_45(a, b, c, d):
    x = [a + b, a + c]
    S = a / min(x)
    return S


def method_46(a, b, c, d):
    x = [a + b, a + c]
    S = a / max(x)
    return S


def method_47(a, b, c, d):
    x = [a + b, a + c]
    S = (a / (((a + b) * (a + c)) ** 0.5)) - max(x) / 2
    return S


def method_48(a, b, c, d):
    n = a + b + c + d
    x = [a + b, a + c]
    S = (n * a - (a + b) * (a + c)) / (n * min(x) - (a + b) * (a + c))
    return S


def method_49(a, b, c, d):
    S = ((a / (a + b)) + (a / (a + c)) + (d / (d + b)) + (d / (d + b))) / 4
    return S


def method_50(a, b, c, d):
    S = (a + d) / (((a + b) * (a + c) * (b + d) * (c + d)) ** 0.5)
    return S


def method_51(a, b, c, d):
    n = a + b + c + d
    X2 = (n * (a * d - b * c) ** 2) / ((a + b) * (a + c) * (c + d) * (b + d))
    S = X2
    return S


def method_52(a, b, c, d):
    n = a + b + c + d
    X2 = (n * (a * d - b * c) ** 2) / ((a + b) * (a + c) * (c + d) * (b + d))
    S = (X2 / (n + X2)) ** 0.5
    return S


def method_53(a, b, c, d):
    n = a + b + c + d
    p = (a * d - b * c) / (((a + b) * (a + c) * (b + d) * (c + d)) ** 0.5)
    S = (p / (n + p)) ** 0.5
    try:
        float(S)
    except TypeError:  # mabin
        S = 0
    return S


def method_54(a, b, c, d):
    S = (a * d - b * c) / (((a + b) * (a + c) * (b + d) * (c + d)) ** 0.5)
    return S


def method_55(a, b, c, d):
    try:
        S = math.cos((math.pi * ((b * c) ** 0.5)) / ((a * d) ** 0.5) + (b * c) ** 0.5)
    except ZeroDivisionError:  # mabin
        S = math.cos((math.pi * ((b * c) ** 0.5)) / (((a * d) ** 0.5) + (b * c) ** 0.5) + 1)

    return S


def method_56(a, b, c, d):
    try:
        S = (a + d) / (b + c)
    except ZeroDivisionError:
        S = a + d
    return S


def method_57(a, b, c, d):
    S = (a * d) / ((a + b) * (a + c) * (b + d) * ((c + d) ** 0.5))
    return S


def method_58(a, b, c, d):
    i = ((a * d - b * c) ** 2) - (a + b) * (a + c) * (b + d) * (c + d)
    if i < 0:
        S = 0
    elif i == 0:
        S = ((2 ** 0.5) * (a * d - b * c)) / ((i ** 0.5) + 1)
    else:
        S = ((2 ** 0.5) * (a * d - b * c)) / (i ** 0.5)
    return S


def method_59(a, b, c, d):
    n = a + b + c + d
    S = math.log10((n * ((abs(a * d - b * c) - 0.5 * n) ** 2)) / ((a + b) * (a + c) * (b + d) * (c + d)))
    return S


def method_60(a, b, c, d):
    S = (a * d) / (((a + b) * (a + c) * (b + d) * (c + d)) ** 0.5)
    return S


def method_61(a, b, c, d):
    S = (a * d - b * c) / (a * d + b * c)
    return S


def method_62(a, b, c, d):
    S = -(2 * b * c / (a * d + b * c))
    return S


def method_63(a, b, c, d):
    S = (((a * d) ** 0.5) - ((b * c) ** 0.5)) / (((a * d) ** 0.5) + ((b * c) ** 0.5))
    return S


def method_64(a, b, c, d):
    try:
        S = a / (b + c)
    except:
        S = 1
    return S


def method_65(a, b, c, d):
    S = a / ((a + b) + (a + c) - a)
    return S


def method_66(a, b, c, d):
    S = (a * d - b * c) / ((a + b + c + d) ** 2)
    return S


def method_67(a, b, c, d):
    S = ((a + d) - (b + c)) / (a + b + c + d)
    return S


def method_68(a, b, c, d):
    S = (4 * (a * d - b * c)) / (((a + d) ** 2) + ((b + c) ** 2))
    return S


def method_69(a, b, c, d):
    n = a + b + c + d
    x = max(a, b)
    y = max(c, d)
    z = max(a, c)
    t = max(b, d)
    xx = max(a + c, b + d)
    yy = max(a + b, c + d)
    delta = x + y + z + t
    deltai = xx + yy
    S = (delta - deltai) / (2 * n - deltai)
    return S


def method_70(a, b, c, d):
    n = a + b + c + d
    x = max(a, b)
    y = max(c, d)
    z = max(a, c)
    t = max(b, d)
    xx = max(a + c, b + d)
    yy = max(a + b, c + d)
    delta = x + y + z + t
    deltai = xx + yy
    S = (delta - deltai) / (2 * n)
    return S


def method_71(a, b, c, d):
    S = (((a * d) ** 0.5) + a) / (((a * d) ** 0.5) + a + b + c)
    return S


def method_72(a, b, c, d):
    S = (((a * d) ** 0.5) + a - b - c) / (((a * d) ** 0.5) + a + b + c)
    return S


def method_73(a, b, c, d):
    try:
        S = ((a * b) + (b * c)) / ((a * b) + 2 * (b * c) + (c * d))
    except ZeroDivisionError:
        S = 1
    return S


def method_74(a, b, c, d):
    n = a + b + c + d
    S = ((n ** 2) * (n * a - ((a + b) * (a + c)))) / ((a + b) * (a + c) * (b + d) * (c + d))
    return S


def method_75(a, b, c, d):
    try:
        S = (a * (c + d)) / (c * (a + b))
    except ZeroDivisionError:
        S = 1
    return S


def method_76(a, b, c, d):
    try:
        S = abs((a * (c + d)) / (c * (a + b)))
    except ZeroDivisionError:
        S = 1
    return S


def method_77(a, b, c, d):
    n = a + b + c + d
    S = math.log(1 + a + d) / math.log(1 + n)
    return S


def method_78(a, b, c, d):
    n = a + b + c + d
    S = (math.log(1 + n) - math.log(1 + b + c)) / math.log(1 + n)
    return S


def method_79(a, b, c, d):
    n = a + b + c + d
    S = math.log(1 + a) / math.log(1 + n)
    return S


def method_80(a, b, c, d):
    S = math.log(1 + a) / math.log(1 + a + b + c)
    return S


def method_81(a, b, c, d):
    n = a + b + c + d
    S = (math.log(1 + a * d) - math.log(1 + b * c)) / math.log(1 + n * n / 4)
    return S
