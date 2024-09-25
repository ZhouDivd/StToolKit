function exportToPDF(contentId, filename) {
    const { jsPDF } = window.jspdf;
    const content = document.querySelector(contentId);
    
    // 设置更高的缩放比例以提高质量
    const scale = 2;
    const options = {
        scale: scale,
        useCORS: true,
        logging: true,
    };

    html2canvas(content, options).then(canvas => {
        const imgData = canvas.toDataURL('image/jpeg', 1.0);
        const pdf = new jsPDF('p', 'mm', 'a4');
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = pdf.internal.pageSize.getHeight();
        const imgWidth = canvas.width;
        const imgHeight = canvas.height;
        const ratio = Math.min(pdfWidth / imgWidth, pdfHeight / imgHeight);
        const imgX = (pdfWidth - imgWidth * ratio) / 2;
        const imgY = 30;

        pdf.addImage(imgData, 'JPEG', imgX, imgY, imgWidth * ratio, imgHeight * ratio);
        pdf.save(filename);
    }).catch(error => {
        console.error('Error generating PDF:', error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const exportButton = document.querySelector('#export-pdf');
    if (exportButton) {
        exportButton.addEventListener('click', function() {
            const contentId = this.getAttribute('data-content-id');
            const filename = this.getAttribute('data-filename');
            exportToPDF(contentId, filename);
        });
    }
});