#!/usr/bin/env python
import numpy as np

ladder_module_map = np.array([[32, 36, 40, 44, 48, 52, 56, 60, 64, 20, 24, 28],
                              [36, 40, 44, 48, 52, 56, 60, 64, 68, 24, 28, 32],
                              [40, 44, 48, 52, 56, 60, 64, 68, 72, 28, 32, 36],
                              [44, 48, 52, 56, 60, 64, 68, 72, 76, 32, 36, 40],
                              [48, 52, 56, 60, 64, 68, 72, 76, 80, 36, 40, 44],
                              [52, 56, 60, 64, 68, 72, 76, 80, 84, 40, 44, 48],
                              [56, 60, 64, 68, 72, 76, 80, 84, 88, 44, 48, 52],
                              [60, 64, 68, 72, 76, 80, 84, 88, 92, 48, 52, 56]])

bin_edge_map = np.array([[-3, -2, 1.08],
                         [-2, -1, 1.35],
                         [-1, 0.2, 1.58],
                         [0.2, 1.1, 1.54],
                         [1.1, 2.2, 1.33],
                         [2.2, np.pi, 1.35]])


def module_map(detid, ladder_index):
    last_digits = detid % 100
    module = ladder_module_map[:, ladder_index].tolist().index(last_digits)
    return module


def r_color_map(r):
    return -12. * r + 279.


def pix_quadrant(gx_, gy_):
    quad = 0
    if gx_ > 0 and gy_ > 0:
        quad = 1
    elif gx_ < 0 < gy_:
        quad = 2
    elif gx_ < 0 and gy_ < 0:
        quad = 3
    elif gy_ < 0 < gx_:
        quad = 4

    return quad


def edge_pix_map(row_, col_):

    if 8 < col_ < 46:
        edge_col = False
    elif 60 < col_ < 96:
        edge_col = False
    elif 112 < col_ < 148:
        edge_col = False
    elif 164 < col_ < 200:
        edge_col = False
    elif 216 < col_ < 252:
        edge_col = False
    elif 268 < col_ < 304:
        edge_col = False
    elif 320 < col_ < 356:
        edge_col = False
    elif 372 < col_ < 408:
        edge_col = False
    else:
        edge_col = True

    if 8 < row_ < 72:
        edge_row = False
    elif 88 < row_ < 152:
        edge_row = False
    else:
        edge_row = True

    return edge_row, edge_col


def ladder_quad_map(ladder):
    ladder = str(ladder)

    ladder_map = {
        '-6' : 3,
        '-5' : 3,
        '-4' : 3,
        '-3' : 4,
        '-2' : 4,
        '-1' : 4,
        '1' : 1,
        '2' : 1,
        '3' : 1,
        '4' : 2,
        '5' : 2,
        '6' : 2,
    }

    return ladder_map[ladder]


def roc_map(row, col):
    row_map = [[0, 79],
               [80, 159]]
    col_map = [[0, 51],
               [52, 103],
               [104, 155],
               [156, 207],
               [208, 259],
               [260, 311],
               [312, 363],
               [364, 415]]
    for i, ind in enumerate(row_map):
        if ind[0] <= row <= ind[1]:
            row_index = i
            break
    for i, ind in enumerate(col_map):
        if ind[0] <= col <= ind[1]:
            col_index = i
            break
    return row_index, col_index


def ladder_map(detid):
    if 303075300 < detid < 303075400:
        ladder = 0
    elif 303071200 < detid < 303071300:
        ladder = 1
    elif 303067100 < detid < 303067200:
        ladder = 2
    elif 303063000 < detid < 303063100:
        ladder = 3
    elif 303058900 < detid < 303059000:
        ladder = 4
    elif 303054800 < detid < 303054900:
        ladder = 5
    elif 303050700 < detid < 303050800:
        ladder = 6
    elif 303046600 < detid < 303046700:
        ladder = 7
    elif 303042500 < detid < 303042600:
        ladder = 8
    elif 303087600 < detid < 303087700:
        ladder = 9
    elif 303083500 < detid < 303083600:
        ladder = 10
    elif 303079400 < detid < 303079500:
        ladder = 11

    return ladder


def rocPhi(roc, ladder):
    link = int(roc)/8
    return float(ladder) - 0.5 + (0.5/2.) + (float(link) * 0.5)


def rocID(col, row):
    rocRow = int(row)/80
    rocCol = int(col)/52
    rocID = rocCol + rocRow*8
    return int(rocID)


def ladderType(ladder):
    if ladder % 2 == 0:
        ladType = 'inner'
    else:
        ladType = 'outer'


