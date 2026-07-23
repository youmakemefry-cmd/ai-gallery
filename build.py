import os
import json
import re
from PIL import Image
from pathlib import Path

# ==============================================================================
# НАСТРОЙКИ ПУТЕЙ И КОНФИГУРАЦИИ
# ==============================================================================
json_file = 'gallery.json'
existing_titles = {}

# Папки для сгенерированного кэша (Next-Gen форматы)
THUMBS_DIR = "thumbs"
SLIDER_DIR = "slider"
os.makedirs(THUMBS_DIR, exist_ok=True)
os.makedirs(SLIDER_DIR, exist_ok=True)

# Сохраняем старые кастомные названия, если они есть
if os.path.exists(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            if '_titles' in old_data:
                existing_titles = old_data['_titles']
    except Exception as e:
        print(f"Не удалось прочитать старый JSON: {e}")

data = {}
titles = {}

def natural_sort_key(text):
    """Функция для натуральной сортировки (1, 2, 10, а не 1, 10, 2)"""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

def process_images_for_performance(folder_path, images):
    """
    Пиллар 2: Переход на Next-Gen форматы и генерация миниатюр.
    Создает зеркальные папки _thumbs (250x250) и _slider (~1000px).
    """
    out_thumb_folder = os.path.join(THUMBS_DIR, folder_path)
    out_slider_folder = os.path.join(SLIDER_DIR, folder_path)
    os.makedirs(out_thumb_folder, exist_ok=True)
    os.makedirs(out_slider_folder, exist_ok=True)

    for img_name in images:
        original_path = os.path.join(folder_path, img_name)
        base_name = os.path.splitext(img_name)[0]
        webp_name = f"{base_name}.webp"
        
        thumb_path = os.path.join(out_thumb_folder, webp_name)
        slider_path = os.path.join(out_slider_folder, webp_name)
        
        # Пропускаем, если файлы уже сгенерированы (экономит время при билде)
        if os.path.exists(thumb_path) and os.path.exists(slider_path):
            continue
            
        try:
            with Image.open(original_path) as img:
                # Конвертация в RGB для корректного сохранения в WebP
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                # 1. Генерация версии для основного слайдера (ширина ~1000px)
                slider_width = 1000
                if img.width > slider_width:
                    ratio = slider_width / float(img.width)
                    slider_height = int(float(img.height) * float(ratio))
                    slider_img = img.resize((slider_width, slider_height), Image.Resampling.LANCZOS)
                    slider_img.save(slider_path, "WEBP", quality=85)
                else:
                    img.save(slider_path, "WEBP", quality=85)
                    
                # 2. Генерация миниатюры (250x250)
                width, height = img.size
                min_dim = min(width, height)
                # Квадратный кроп по центру
                left = (width - min_dim)/2
                top = (height - min_dim)/2
                right = (width + min_dim)/2
                bottom = (height + min_dim)/2
                
                thumb_img = img.crop((left, top, right, bottom))
                thumb_img.thumbnail((250, 250), Image.Resampling.LANCZOS)
                thumb_img.save(thumb_path, "WEBP", quality=80)
                
                print(f"Сгенерирован кэш для: {original_path}")
        except Exception as e:
            print(f"Ошибка при обработке {original_path}: {e}")

valid_folders = []

# Шаг 1: Собираем папки
for folder_name in os.listdir('.'):
    # Игнорируем скрытые папки и папки с кэшем (_thumbs, _slider)
    if os.path.isdir(folder_name) and not folder_name.startswith('.') and folder_name not in [THUMBS_DIR, SLIDER_DIR]:
        images = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        
        if len(images) >= 2:
            sorted_images = sorted(images, key=natural_sort_key)
            creation_time = os.path.getctime(folder_name)
            valid_folders.append((creation_time, folder_name, sorted_images))

# Шаг 2: Сортируем папки хронологически
valid_folders.sort(key=lambda x: x[0])

# Шаг 3: Заполняем словари и генерируем Next-Gen графику
print("Начинаю сборку галереи и генерацию WebP кэша...")
for _, folder_name, sorted_images in valid_folders:
    
    # Запускаем оптимизацию изображений для текущей папки
    process_images_for_performance(folder_name, sorted_images)
    
    data[folder_name] = sorted_images
    
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

print("gallery.json пересобран. 3-Пиллара: графический кэш (WebP) успешно обновлен!")