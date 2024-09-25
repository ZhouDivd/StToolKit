import math

def calculate(data):
    # 实现预埋件计算的具体逻辑
    diameter = data.get('diameter', 0)
    depth = data.get('depth', 0)
    volume = math.pi * (diameter/2)**2 * depth
    return {"volume": volume}