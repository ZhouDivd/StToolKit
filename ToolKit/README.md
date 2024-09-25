# 结构工具箱

这是一个基于 Flask 的 Web 应用程序，提供各种结构计算工具。

## 项目结构
project_root/
│
├── static/
│ ├── css/
│ │ ├── main.css
│ │ ├── plate-cutting.css
│ │ ├── knee-calculation.css
│ │ └── embedded-part.css
│ │
│ ├── js/
│ │ ├── main.js
│ │ ├── plate-cutting.js
│ │ ├── knee-calculation.js
│ │ ├── embedded-part.js
│ │ └── export-pdf.js
│ │
│ └── images/
│ ├── plate-cutting.jpg
│ ├── knee-calculation.jpg
│ └── embedded-part.jpg
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── plate-cutting.html
│ ├── knee-calculation.html
│ └── embedded-part.html
│
├── calculations/
│ ├── init.py
│ ├── plate_cutting.py
│ ├── knee_calculation.py
│ └── embedded_part.py
│
├── app.py
├── save_conversation.py
└── README.md
