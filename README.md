# VSCL Team Logo Downloader
<img width="812" alt="image" src="https://github.com/user-attachments/assets/6732f157-d57a-4d46-bd81-e2537cf1e35a" />



Этот Python скрипт автоматизирует процесс скачивания логотипов команд со страницы турнира VSCL.RU. Он имеет графический пользовательский интерфейс (GUI), созданный с помощью Tkinter, что упрощает указание целевого URL и желаемой выходной директории.

## Возможности

*   **Интерфейс на основе GUI:** Удобный интерфейс для ввода URL и выбора выходной папки.
*   **Веб-скрейпинг с BeautifulSoup4:** Анализирует HTML-код целевой веб-страницы для поиска ссылок на логотипы команд.
*   **Скачивание изображений с Requests:** Эффективно скачивает изображения логотипов по найденным URL.
*   **Обработка изображений с Pillow (PIL):** Обрабатывает сохранение изображений в формате PNG, обеспечивая совместимость.
*   **Многопоточность:** Скачивает логотипы в отдельном потоке, чтобы предотвратить зависание GUI во время процесса загрузки, обеспечивая отзывчивый пользовательский интерфейс.
*   **Обработка ошибок:** Корректно обрабатывает распространенные проблемы, такие как неработающие ссылки, ошибки сети и недопустимые форматы изображений, предоставляя информативные обновления статуса в GUI.
*   **Санитарная обработка имен файлов:** Очищает имена файлов, заменяя потенциально проблемные символы, обеспечивая совместимость с различными операционными системами.
*   **Обновления статуса:** Отображает ход загрузки и любые сообщения об ошибках в GUI.

## Требования

*   Python 3.x
*   Requests: `pip install requests`
*   BeautifulSoup4: `pip install beautifulsoup4`
*   Pillow (PIL): `pip install Pillow`

## Использование (клонирование)

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/r3dri/Team-Logo-Downloader
    cd team-logo-downloader
    ```

2.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Запустите скрипт:**

    ```bash
    python TeamParserVSCL.py
    ```

4.  **Введите URL:** Вставьте URL целевой веб-страницы в поле "URL".
5.  **Выберите выходную папку:** Нажмите кнопку "Browse Output Folder", чтобы выбрать каталог, в котором будут сохранены логотипы.
6.  **Скачайте логотипы:** Нажмите кнопку "Download Logos", чтобы начать процесс загрузки. Статус загрузки будет отображаться в строке состояния.


## Использование (Программа)

1.  **Установите последнюю версию программы:**
[Последний релиз](https://github.com/r3dri/Team-Logo-Downloader/releases)

2.  **Запустите файл TeamLogoDownloader.exe :**

3.  **Введите URL:** Вставьте URL целевой веб-страницы в поле "URL".
4.  **Выберите выходную папку:** Нажмите кнопку "Browse Output Folder", чтобы выбрать каталог, в котором будут сохранены логотипы.
5.  **Скачайте логотипы:** Нажмите кнопку "Download Logos", чтобы начать процесс загрузки. Статус загрузки будет отображаться в строке состояния.
## Пример

Предположим, вы хотите скачать логотипы команд со страницы турнира по адресу `https://www.vscl.ru/tournaments/teams`. Вы должны:

1.  Запустить скрипт.
2.  Ввести `https://www.vscl.ru/tournaments/teams` в поле URL.
3.  Выбрать желаемую выходную директорию (например, `logos`).
4.  Нажать кнопку "Download Logos".

Затем скрипт скачает логотипы команд со страницы и сохранит их в виде PNG-файлов в директории `logos`.
