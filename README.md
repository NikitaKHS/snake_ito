# Змейка ИТО

Игра «Змейка» стилизованная под наш ITO-отдел. Изначально код был на футболке коллеги и я решил дописать его и стилизировать.

## ✅ Что готово?

- **Game Over** с сообщением «ИТО Нуждался в тебе»
- Кнопка «Попробовать ещё раз» после поражения
- Отображение счёта в стиле датацентра (зелёный шрифт, моноширинный)

---

## 📋 Требования

- Python 3.6+
- Модуль `tkinter` (обычно входит в стандартную поставку)

## 🚀 Установка

1. Склонируйте репозиторий или скопируйте файл `snake_ito.py` в папку проекта.
2. Поместите изображение `qsfp_texture.png` рядом со скриптом.
3. Убедитесь, что у вас установлен Python и tkinter.

## ▶️ Запуск

```bash
python snake_ito.py
```

## 🎮 Управление

- Стрелка ↑ — движение вверх
- Стрелка ↓ — движение вниз
- Стрелка ← — движение влево
- Стрелка → — движение вправо

## 🖌️ Стилизация

- **Фон**: чёрный
- **Сегменты**: бирюзовые, как оптоволоконные кабели
- **Шрифт счёта**: моноширинный `Courier`, цвет `lime` для «зелёного логирования»
- **Сообщение Game Over**: красный заголовок, подчёркнутый белым текстом «ИТО Нуждался в тебе»
- **Кнопка перезапуска**: стандартная кнопка tkinter, вписана в общую графику

## 🛠️ Структура кода

- `CableSegment` — обычный сегмент змейки
- `HeadSegment` — голова с подписью `ito`
- `Food` — «еда» в виде изображения QSFP модуля
- `Snake` — логика движения, роста и обработки столкновений

## 🤝 Вклад

Если хотите добавить новые фичи или улучшить стили, присылайте PR в репозиторий.

## 🤝 Фотокарточки

![image](https://github.com/user-attachments/assets/addbf22c-6cb8-454b-9299-04cebd7bcc61)
![image](https://github.com/user-attachments/assets/b65809cf-0e52-47ac-b8ba-8d387eabb7b7)


