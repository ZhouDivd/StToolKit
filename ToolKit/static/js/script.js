// 删除或注释掉这个函数
// function openToolPage(page) {
//     window.open(page, '_blank');
// }

// 当 DOM 加载完成后执行的函数
document.addEventListener('DOMContentLoaded', function() {
    console.log('结构工具箱已加载');
    
    // 为所有按钮添加点击事件监听器
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            console.log(`点击了 ${this.textContent} 按钮`);
        });
    });
});

// 这里可以添加更多的 JavaScript 函数来处理其他交互