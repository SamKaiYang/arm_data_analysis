#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import statistics


## TODO: left right
path = '/home/iclab/Documents/nex/Arm data analysis/220207/NRPL_LOG_1.txt'
f = open(path, 'r')
Index = []
G0A0ActPos = []
G0A0CmdPos = []
G0A1ActPos = []
G0A1CmdPos = []
G0A2ActPos = []
G0A2CmdPos = []
G0A3ActPos = []
G0A3CmdPos = []
G0A4ActPos = []
G0A4CmdPos = []
G0A5ActPos = []
G0A5CmdPos = []

with open(path) as f:
    for line in f.readlines():
        # s = line.split('         ')
        s = line.split()
        Index.append(int(s[0]))
        G0A0ActPos.append(float(s[1]))
        G0A0CmdPos.append(float(s[2]))
        G0A1ActPos.append(float(s[3]))
        G0A1CmdPos.append(float(s[4]))
        G0A2ActPos.append(float(s[5]))
        G0A2CmdPos.append(float(s[6]))
        G0A3ActPos.append(float(s[7]))
        G0A3CmdPos.append(float(s[8]))
        G0A4ActPos.append(float(s[9]))
        G0A4CmdPos.append(float(s[10]))
        G0A5ActPos.append(float(s[11]))
        G0A5CmdPos.append(float(s[12]))

# print(Index)
# print(G0A5CmdPos)
print("actaul與command最大差異值計算(單位角度)")
print("---Line左右位移, Y軸正負移動---")
A0_diff = []
for item in range(len(Index)):
    difference = G0A0ActPos[item]-G0A0CmdPos[item]
    A0_diff.append(difference)

print("軸1 max diff:",max(A0_diff))

A1_diff = []
for item in range(len(Index)):
    difference = G0A1ActPos[item]-G0A1CmdPos[item]
    A1_diff.append(difference)

print("軸2 max diff:",max(A1_diff))

A2_diff = []
for item in range(len(Index)):
    difference = G0A2ActPos[item]-G0A2CmdPos[item]
    A2_diff.append(difference)

print("軸3 max diff:",max(A2_diff))

A3_diff = []
for item in range(len(Index)):
    difference = G0A3ActPos[item]-G0A3CmdPos[item]
    A3_diff.append(difference)

print("軸4 max diff:",max(A3_diff))

A4_diff = []
for item in range(len(Index)):
    difference = G0A4ActPos[item]-G0A4CmdPos[item]
    A4_diff.append(difference)

print("軸5 max diff:",max(A4_diff))

A5_diff = []
for item in range(len(Index)):
    difference = G0A5ActPos[item]-G0A5CmdPos[item]
    A5_diff.append(difference)

print("軸6 max diff:",max(A5_diff))

## TODO: up down
path = '/home/iclab/Documents/nex/Arm data analysis/220207/NRPL_LOG_2.txt'
f = open(path, 'r')
Index = []
G0A0ActPos = []
G0A0CmdPos = []
G0A1ActPos = []
G0A1CmdPos = []
G0A2ActPos = []
G0A2CmdPos = []
G0A3ActPos = []
G0A3CmdPos = []
G0A4ActPos = []
G0A4CmdPos = []
G0A5ActPos = []
G0A5CmdPos = []

with open(path) as f:
    for line in f.readlines():
        # s = line.split('         ')
        s = line.split()
        Index.append(int(s[0]))
        G0A0ActPos.append(float(s[1]))
        G0A0CmdPos.append(float(s[2]))
        G0A1ActPos.append(float(s[3]))
        G0A1CmdPos.append(float(s[4]))
        G0A2ActPos.append(float(s[5]))
        G0A2CmdPos.append(float(s[6]))
        G0A3ActPos.append(float(s[7]))
        G0A3CmdPos.append(float(s[8]))
        G0A4ActPos.append(float(s[9]))
        G0A4CmdPos.append(float(s[10]))
        G0A5ActPos.append(float(s[11]))
        G0A5CmdPos.append(float(s[12]))

# print(Index)
# print(G0A5CmdPos)
print("---Line上下位移, Z軸正負移動---")
A0_diff = []
for item in range(len(Index)):
    difference = G0A0ActPos[item]-G0A0CmdPos[item]
    A0_diff.append(difference)

print("軸1 max diff:",max(A0_diff))

A1_diff = []
for item in range(len(Index)):
    difference = G0A1ActPos[item]-G0A1CmdPos[item]
    A1_diff.append(difference)

print("軸2 max diff:",max(A1_diff))

A2_diff = []
for item in range(len(Index)):
    difference = G0A2ActPos[item]-G0A2CmdPos[item]
    A2_diff.append(difference)

print("軸3 max diff:",max(A2_diff))

A3_diff = []
for item in range(len(Index)):
    difference = G0A3ActPos[item]-G0A3CmdPos[item]
    A3_diff.append(difference)

print("軸4 max diff:",max(A3_diff))

A4_diff = []
for item in range(len(Index)):
    difference = G0A4ActPos[item]-G0A4CmdPos[item]
    A4_diff.append(difference)

print("軸5 max diff:",max(A4_diff))

A5_diff = []
for item in range(len(Index)):
    difference = G0A5ActPos[item]-G0A5CmdPos[item]
    A5_diff.append(difference)

print("軸6 max diff:",max(A5_diff))

## TODO: forward backward
path = '/home/iclab/Documents/nex/Arm data analysis/220207/NRPL_LOG_3.txt'
f = open(path, 'r')
Index = []
G0A0ActPos = []
G0A0CmdPos = []
G0A1ActPos = []
G0A1CmdPos = []
G0A2ActPos = []
G0A2CmdPos = []
G0A3ActPos = []
G0A3CmdPos = []
G0A4ActPos = []
G0A4CmdPos = []
G0A5ActPos = []
G0A5CmdPos = []

with open(path) as f:
    for line in f.readlines():
        # s = line.split('         ')
        s = line.split()
        Index.append(int(s[0]))
        G0A0ActPos.append(float(s[1]))
        G0A0CmdPos.append(float(s[2]))
        G0A1ActPos.append(float(s[3]))
        G0A1CmdPos.append(float(s[4]))
        G0A2ActPos.append(float(s[5]))
        G0A2CmdPos.append(float(s[6]))
        G0A3ActPos.append(float(s[7]))
        G0A3CmdPos.append(float(s[8]))
        G0A4ActPos.append(float(s[9]))
        G0A4CmdPos.append(float(s[10]))
        G0A5ActPos.append(float(s[11]))
        G0A5CmdPos.append(float(s[12]))

# print(Index)
# print(G0A5CmdPos)
print("---Line前後位移, X軸正負移動---")
A0_diff = []
for item in range(len(Index)):
    difference = G0A0ActPos[item]-G0A0CmdPos[item]
    A0_diff.append(difference)

print("軸1 max diff:",max(A0_diff))

A1_diff = []
for item in range(len(Index)):
    difference = G0A1ActPos[item]-G0A1CmdPos[item]
    A1_diff.append(difference)

print("軸2 max diff:",max(A1_diff))

A2_diff = []
for item in range(len(Index)):
    difference = G0A2ActPos[item]-G0A2CmdPos[item]
    A2_diff.append(difference)

print("軸3 max diff:",max(A2_diff))

A3_diff = []
for item in range(len(Index)):
    difference = G0A3ActPos[item]-G0A3CmdPos[item]
    A3_diff.append(difference)

print("軸4 max diff:",max(A3_diff))

A4_diff = []
for item in range(len(Index)):
    difference = G0A4ActPos[item]-G0A4CmdPos[item]
    A4_diff.append(difference)

print("軸5 max diff:",max(A4_diff))

A5_diff = []
for item in range(len(Index)):
    difference = G0A5ActPos[item]-G0A5CmdPos[item]
    A5_diff.append(difference)

print("軸6 max diff:",max(A5_diff))

## TODO: MP 5 points movement
path = '/home/iclab/Documents/nex/Arm data analysis/220207/NRPL_LOG_4.txt'
f = open(path, 'r')
Index = []
G0A0ActPos = []
G0A0CmdPos = []
G0A1ActPos = []
G0A1CmdPos = []
G0A2ActPos = []
G0A2CmdPos = []
G0A3ActPos = []
G0A3CmdPos = []
G0A4ActPos = []
G0A4CmdPos = []
G0A5ActPos = []
G0A5CmdPos = []

with open(path) as f:
    for line in f.readlines():
        # s = line.split('         ')
        s = line.split()
        Index.append(int(s[0]))
        G0A0ActPos.append(float(s[1]))
        G0A0CmdPos.append(float(s[2]))
        G0A1ActPos.append(float(s[3]))
        G0A1CmdPos.append(float(s[4]))
        G0A2ActPos.append(float(s[5]))
        G0A2CmdPos.append(float(s[6]))
        G0A3ActPos.append(float(s[7]))
        G0A3CmdPos.append(float(s[8]))
        G0A4ActPos.append(float(s[9]))
        G0A4CmdPos.append(float(s[10]))
        G0A5ActPos.append(float(s[11]))
        G0A5CmdPos.append(float(s[12]))

# print(Index)
# print(G0A5CmdPos)
print("---Line斜平面5點移動---")
A0_diff = []
for item in range(len(Index)):
    difference = G0A0ActPos[item]-G0A0CmdPos[item]
    A0_diff.append(difference)

print("軸1 max diff:",max(A0_diff))

A1_diff = []
for item in range(len(Index)):
    difference = G0A1ActPos[item]-G0A1CmdPos[item]
    A1_diff.append(difference)

print("軸2 max diff:",max(A1_diff))

A2_diff = []
for item in range(len(Index)):
    difference = G0A2ActPos[item]-G0A2CmdPos[item]
    A2_diff.append(difference)

print("軸3 max diff:",max(A2_diff))

A3_diff = []
for item in range(len(Index)):
    difference = G0A3ActPos[item]-G0A3CmdPos[item]
    A3_diff.append(difference)

print("軸4 max diff:",max(A3_diff))

A4_diff = []
for item in range(len(Index)):
    difference = G0A4ActPos[item]-G0A4CmdPos[item]
    A4_diff.append(difference)

print("軸5 max diff:",max(A4_diff))

A5_diff = []
for item in range(len(Index)):
    difference = G0A5ActPos[item]-G0A5CmdPos[item]
    A5_diff.append(difference)

print("軸6 max diff:",max(A5_diff))

## TODO: SW 8 points movement
path = '/home/iclab/Documents/nex/Arm data analysis/220207/NRPL_LOG_5.txt'
f = open(path, 'r')
Index = []
G0A0ActPos = []
G0A0CmdPos = []
G0A1ActPos = []
G0A1CmdPos = []
G0A2ActPos = []
G0A2CmdPos = []
G0A3ActPos = []
G0A3CmdPos = []
G0A4ActPos = []
G0A4CmdPos = []
G0A5ActPos = []
G0A5CmdPos = []

with open(path) as f:
    for line in f.readlines():
        # s = line.split('         ')
        s = line.split()
        Index.append(int(s[0]))
        G0A0ActPos.append(float(s[1]))
        G0A0CmdPos.append(float(s[2]))
        G0A1ActPos.append(float(s[3]))
        G0A1CmdPos.append(float(s[4]))
        G0A2ActPos.append(float(s[5]))
        G0A2CmdPos.append(float(s[6]))
        G0A3ActPos.append(float(s[7]))
        G0A3CmdPos.append(float(s[8]))
        G0A4ActPos.append(float(s[9]))
        G0A4CmdPos.append(float(s[10]))
        G0A5ActPos.append(float(s[11]))
        G0A5CmdPos.append(float(s[12]))

# print(Index)
# print(G0A5CmdPos)
print("---Line立方體8點移動---")
A0_diff = []
for item in range(len(Index)):
    difference = G0A0ActPos[item]-G0A0CmdPos[item]
    A0_diff.append(difference)

print("軸1 max diff:",max(A0_diff))

A1_diff = []
for item in range(len(Index)):
    difference = G0A1ActPos[item]-G0A1CmdPos[item]
    A1_diff.append(difference)

print("軸2 max diff:",max(A1_diff))

A2_diff = []
for item in range(len(Index)):
    difference = G0A2ActPos[item]-G0A2CmdPos[item]
    A2_diff.append(difference)

print("軸3 max diff:",max(A2_diff))

A3_diff = []
for item in range(len(Index)):
    difference = G0A3ActPos[item]-G0A3CmdPos[item]
    A3_diff.append(difference)

print("軸4 max diff:",max(A3_diff))

A4_diff = []
for item in range(len(Index)):
    difference = G0A4ActPos[item]-G0A4CmdPos[item]
    A4_diff.append(difference)

print("軸5 max diff:",max(A4_diff))

A5_diff = []
for item in range(len(Index)):
    difference = G0A5ActPos[item]-G0A5CmdPos[item]
    A5_diff.append(difference)

print("軸6 max diff:",max(A5_diff))

