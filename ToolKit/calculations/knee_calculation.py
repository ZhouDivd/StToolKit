def calculate(data):
    # 实现牛腿计算的具体逻辑
    force = data.get('force', 0)
    length = data.get('length', 0)
    moment = force * length
    return {"moment": moment}