def calculate(data):
    thickness = float(data['thickness'])
    hole_diameter = float(data['hole_diameter'])
    material_strength = float(data['material_strength'])
    safety_factor = float(data['safety_factor'])

    # 计算逻辑（这里使用简化的示例）
    cutting_force = 0.8 * thickness * hole_diameter * material_strength * safety_factor
    min_edge_distance = 1.5 * hole_diameter
    min_spacing = 2 * hole_diameter

    # 生成结论
    conclusion = f"""
    根据计算结果，对于厚度为 {thickness} mm 的板材，孔径为 {hole_diameter} mm，材料强度为 {material_strength} MPa，
    考虑安全系数 {safety_factor}，得出以下结论：

    1. 所需冲切力为 {cutting_force:.2f} kN。
    2. 最小边距应不小于 {min_edge_distance:.2f} mm。
    3. 最小间距应不小于 {min_spacing:.2f} mm。

    请确保在实际应用中遵守这些计算结果，以保证结构的安全性和可靠性。
    """

    return {
        "cutting_force": cutting_force,
        "min_edge_distance": min_edge_distance,
        "min_spacing": min_spacing,
        "conclusion": conclusion
    }
