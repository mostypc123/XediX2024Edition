import webview

def main():
    # HTML code as a string
    html_code = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Text Editor</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        /* Keyframe animations */
        @keyframes slideInFromBottom {
            from {
                transform: translateY(100%);
            }

            to {
                transform: translateY(0);
            }
        }

        @keyframes slideOutToBottom {
            from {
                transform: translateY(0);
            }

            to {
                transform: translateY(100%);
            }
        }

        /* Dark mode styles */
        body {
            background-color: #153747;
            color: #e5e7eb;
        }

        .bg-dark {
            background-color: #2d3748;
            color: #e5e7eb;
        }

        .text-dark {
            color: #e5e7eb;
        }

        .border-dark {
            border-color: #4a5568;
        }

        .placeholder-dark::placeholder {
            color: #9fa6b2;
        }

        /* Custom notification */
        #customNotification,
        #notificationsPanel {
            animation-duration: 0.5s;
            animation-timing-function: ease-out;
        }

        .animate-slide-in-bottom {
            animation-name: slideInFromBottom;
        }

        .animate-slide-out-bottom {
            animation-name: slideOutToBottom;
        }

        /* Buttons */
        .editor-btn {
            background-color: #4a5568;
            color: #e5e7eb;
        }

        .editor-btn:hover {
            background-color: #718096;
        }

        /* Sidebar styles */
        .sidebar {
            width: 250px;
            background-color: #2d3748;
            color: #e5e7eb;
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            padding: 20px;
        }

        .sidebar a {
            display: block;
            color: #e5e7eb;
            padding: 10px 0;
            text-decoration: none;
        }

        .sidebar a:hover {
            background-color: #4a5568;
        }

        .content {
            margin-left: 250px;
        }

    </style>
</head>

<body class="bg-gray-100 font-sans">
    <div class="sidebar">
        <h1>Menu</h1>
        <a href="#" id="saveBtn" class="editor-menu-item">
            <i class="fas fa-save mr-2"></i> Save
        </a>
        <a href="#" id="loadBtn" class="editor-menu-item">
            <i class="fas fa-file-upload mr-2"></i> Load
        </a>
        <a href="#" id="clearBtn" class="editor-menu-item">
            <i class="fas fa-trash-alt mr-2"></i> Clear
        </a>
        <a href="#" id="addFileBtn" class="editor-menu-item">
            <i class="fas fa-plus mr-2"></i> Add File
        </a>
        <a href="#" id="notificationsBtn" class="editor-menu-item">
            <i class="fas fa-bell mr-2"></i> Notifications
        </a>
    </div>
    
    <div class="content">
        <div class="container mx-auto mt-8 bg-dark shadow-lg max-w-2xl rounded-md p-8 relative">

            <!-- Editor Controls -->
            <div class="flex flex-wrap justify-between mb-4">
                <div class="flex flex-wrap items-center space-x-2 mb-2 lg:mb-0">
                    <!-- Buttons removed from here -->
                </div>
                <!-- Button removed from here -->
            </div>

            <!-- Tabs -->
            <div id="tabs" class="mb-4">
                <!-- Tabs will be dynamically added here -->
            </div>

            <!-- Custom Notification -->
            <div id="customNotification" class="fixed bottom-0 right-0 m-4 bg-green-500 text-white p-4 rounded-md hidden">
                <!-- Custom notification content will be displayed here -->
            </div>

            <!-- Notifications Panel -->
            <div id="notificationsPanel" class="fixed bottom-0 right-0 m-4 p-4 bg-white border border-gray-300 rounded-md hidden">
                <h2 class="text-xl font-bold mb-4">Notifications</h2>
                <ul id="notificationList" class="list-disc pl-8">
                    <!-- Notification items will be added here -->
                </ul>
            </div>

            <!-- Text Editor -->
            <textarea id="editor" class="w-full h-96 p-4 border rounded-md focus:outline-none focus:border-blue-500 bg-dark text-dark placeholder-dark"></textarea>

            <!-- Toolbar -->
            <div id="toolbar" class="flex justify-center mt-4">
                <button id="boldBtn" class="editor-btn px-4 py-2 rounded-md mr-2 focus:outline-none">
                    <i class="fas fa-bold"></i>
                </button>
                <button id="italicBtn" class="editor-btn px-4 py-2 rounded-md mr-2 focus:outline-none">
                    <i class="fas fa-italic"></i>
                </button>
                <button id="underlineBtn" class="editor-btn px-4 py-2 rounded-md mr-2 focus:outline-none">
                    <i class="fas fa-underline"></i>
                </button>
                <button id="strikeThroughBtn" class="editor-btn px-4 py-2 rounded-md mr-2 focus:outline-none">
                    <i class="fas fa-strikethrough"></i>
                </button>
            </div>
            <br>
            <label for="fontSelect" class="mr-2 text-white">Font:</label>
            <select id="fontSelect" class="editor-select text-white bg-gray-800 border border-gray-700 rounded-md px-4 py-2 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200">
                <option value="Arial">Arial</option>
                <option value="Helvetica">Helvetica</option>
                <option value="Verdana">Verdana</option>
                <option value="Times New Roman">Times New Roman</option>
                <option value="Courier New">Courier New</option>
                <option value="Georgia">Georgia</option>
                <option value="Palatino">Palatino</option>
                <option value="Garamond">Garamond</option>
                <option value="Comic Sans MS">Comic Sans MS</option>
                <option value="Arial Black">Arial Black</option>
            </select>
        </div>
    </div>

    <!-- JavaScript -->
    <script>
                document.getElementById('fontSelect').addEventListener('change', function () {
    const selectedFont = this.value;
    editor.style.fontFamily = selectedFont;
});

        document.addEventListener("DOMContentLoaded", function () {
            const tabsContainer = document.getElementById('tabs');
            const editor = document.getElementById('editor');
            const fileInput = document.getElementById('fileInput');
            const customNotification = document.getElementById('customNotification');
            const notificationsPanel = document.getElementById('notificationsPanel');
            const notificationList = document.getElementById('notificationList');

            document.getElementById('addFileBtn').addEventListener('click', function () {
                const fileName = prompt('Enter the file name:');
                if (fileName) {
                    createTab(fileName);
                }
            });

            document.getElementById('fileInput').addEventListener('change', function (event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        const content = e.target.result;
                        const fileName = file.name;
                        createTab(fileName, content);
                    };
                    reader.readAsText(file);
                }
            });

            document.getElementById('saveBtn').addEventListener('click', function () {
                const content = editor.value;
                if (content.trim() !== '') {
                    requestNotificationPermission();
                    showCustomNotification('File saved successfully!', 'bg-green-500');
                    addNotificationToPanel('File saved successfully!');
                } else {
                    showCustomNotification('Cannot save an empty file.', 'bg-red-500');
                    addNotificationToPanel('Cannot save an empty file.');
                }
            });

            document.getElementById('notificationsBtn').addEventListener('click', function () {
                toggleNotificationsPanel();
            });

            document.getElementById('boldBtn').addEventListener('click', function () {
                document.execCommand('bold');
            });

            document.getElementById('italicBtn').addEventListener('click', function () {
                document.execCommand('italic');
            });

            document.getElementById('underlineBtn').addEventListener('click', function () {
                document.execCommand('underline');
            });

            document.getElementById('strikeThroughBtn').addEventListener('click', function () {
                document.execCommand('strikeThrough');
            });

            function createTab(fileName, content = '') {
                const fileExtension = fileName.split('.').pop();
                const tab = document.createElement('button');
                tab.innerHTML = `<i class="fas fa-file mr-2"></i>${fileName}`;
                tab.className = 'editor-btn px-4 py-2 rounded-md mr-2 focus:outline-none';
                tab.addEventListener('click', function () {
                    switchToFile(fileName, content);
                });

                tabsContainer.appendChild(tab);
                switchToFile(fileName, content);
            }

            function switchToFile(fileName, content) {
                editor.value = content;
            }

            function requestNotificationPermission() {
                if (Notification.permission !== 'granted') {
                    Notification.requestPermission().then(permission => {
                        if (permission === 'granted') {
                            // Permission granted, you can now show notifications
                        }
                    });
                }
            }

            function showCustomNotification(message, bgColor) {
                customNotification.textContent = message;
                customNotification.style.backgroundColor = bgColor;
                customNotification.classList.remove('hidden');
                customNotification.classList.add('animate-slide-in-bottom');
                setTimeout(() => {
                    customNotification.classList.add('hidden');
                    customNotification.classList.remove('animate-slide-in-bottom');
                }, 3000);
            }

            function toggleNotificationsPanel() {
                notificationsPanel.classList.toggle('hidden');
            }

            function addNotificationToPanel(message) {
                const notificationItem = document.createElement('li');
                notificationItem.textContent = message;
                notificationList.appendChild(notificationItem);
            }
        });
    </script>
</body>

</html>
    """
    
    # Create a webview window with the HTML code
    webview.create_window('XediX', html=html_code, width=1000, height=800, resizable=True)
    
    # Run the webview app
    webview.start()

if __name__ == '__main__':
    main()
