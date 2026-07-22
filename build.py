import os
import json
import re
from PIL import Image

json_file = 'gallery.json'
existing_titles = {}

# Папки для оптимизированного контента
PREVIEWS_DIR = '_previews'
THUMBS_DIR = '_thumbs'

# Сохраняем старые кастомные названия
if os.path.exists(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            if '_titles' in old_data:
                existing_titles = old_data['_titles']
    except Exception as e:
        print(f"Не удалось прочитать старый JSON: {e}")

def natural_sort_key(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Функция для генерации легковесных копий
def process_image(folder, filename):
    orig_path = os.path.join(folder, filename)
    base_name = os.path.splitext(filename)[0]
    webp_filename = f"{base_name}.webp"
    
    preview_folder = os.path.join(PREVIEWS_DIR, folder)
    thumb_folder = os.path.join(THUMBS_DIR, folder)
    
    ensure_dir(preview_folder)
    ensure_dir(thumb_folder)
    
    preview_path = os.path.join(preview_folder, webp_filename)
    thumb_path = os.path.join(thumb_folder, webp_filename)
    
    # Инкрементальная проверка: если файлы уже есть, не тратим время процессора
    if os.path.exists(preview_path) and os.path.exists(thumb_path):
        return
        
    try:
        with Image.open(orig_path) as img:
            # Преобразуем в RGB если картинка в RGBA/CMYK (для сохранения в WebP)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # 1. Генерация превью для слайдера (Max 1200px по широкой стороне)
            if not os.path.exists(preview_path):
                p_img = img.copy()
                p_img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
                p_img.save(preview_path, "WEBP", quality=80)
            
            # 2. Генерация превью для трека миниатюр (Max 300px)
            if not os.path.exists(thumb_path):
                t_img = img.copy()
                t_img.thumbnail((300, 300), Image.Resampling.LANCZOS)
                t_img.save(thumb_path, "WEBP", quality=75)
    except Exception as e:
        print(f"Ошибка обработки изображения {orig_path}: {e}")

data = {}
titles = {}
valid_folders = []

# Шаг 1: Собираем папки
for folder_name in os.listdir('.'):
    # Игнорируем служебные директории оптимизации и скрытые файлы
    if os.path.isdir(folder_name) and not folder_name.startswith('.') and folder_name not in [PREVIEWS_DIR, THUMBS_DIR]:
        images = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        
        if len(images) >= 2:
            sorted_images = sorted(images, key=natural_sort_key)
            creation_time = os.path.getctime(folder_name)
            valid_folders.append((creation_time, folder_name, sorted_images))

# Шаг 2: Сортируем хронологически
valid_folders.sort(key=lambda x: x[0])

print("Оптимизация графических ассетов и генерация кэша...")

# Шаг 3: Заполняем словари и оптимизируем картинки
for _, folder_name, sorted_images in valid_folders:
    data[folder_name] = sorted_images
    
    # Запускаем обработку каждой картинки в папке
    for img_file in sorted_images:
        process_image(folder_name, img_file)
    
    if folder_name in existing_titles:
        titles[folder_name] = existing_titles[folder_name]
    else:
        second_img_full_name = sorted_images[1]
        second_img_name = os.path.splitext(second_img_full_name)[0]
        titles[folder_name] = second_img_name

# Собираем итоговый объект
final_data = {'_titles': titles}
final_data.update(data)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("Анализ завершен! gallery.json обновлен. Оптимизированные кэш-директории созданы.")

input("\nНажмите Enter, чтобы закрыть окно...")