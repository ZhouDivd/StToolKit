document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('plate-cutting-form');
    const resultDiv = document.getElementById('result');
    const conclusionDiv = document.getElementById('conclusion');
    const conclusionText = document.getElementById('conclusion-text');
    const exportPdfButton = document.getElementById('export-pdf');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const thickness = document.getElementById('thickness').value;
        const holeDiameter = document.getElementById('hole_diameter').value;
        const materialStrength = document.getElementById('material_strength').value;
        const safetyFactor = document.getElementById('safety_factor').value;

        fetch('/calculate/plate-cutting', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                thickness, 
                hole_diameter: holeDiameter, 
                material_strength: materialStrength, 
                safety_factor: safetyFactor 
            }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('cutting-force').textContent = `${data.cutting_force.toFixed(2)} kN`;
            document.getElementById('min-edge-distance').textContent = `${data.min_edge_distance.toFixed(2)} mm`;
            document.getElementById('min-spacing').textContent = `${data.min_spacing.toFixed(2)} mm`;
            
            resultDiv.style.display = 'block';
            
            conclusionText.innerHTML = data.conclusion;
            conclusionDiv.style.display = 'block';
            exportPdfButton.style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
            resultDiv.innerHTML = '<p>计算出错，请重试。</p>';
        });
    });
});