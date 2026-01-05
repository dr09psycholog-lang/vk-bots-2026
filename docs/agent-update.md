# Инструкция по обновлению агента

## Шаг 1: Использование системного промпта

Скопируйте содержимое из `vk-rehab-bot/prompts.md` и используйте его как `system_prompt` при обращении к GigaChat/LLM API.

```python
from detect_mode import detect_mode, MODE_MODIFIERS

# Загрузите системный промпт
with open('vk-rehab-bot/prompts.md', 'r', encoding='utf-8') as f:
    system_prompt = f.read()

# Обработайте сообщение пользователя
user_message = "Подготовь к зачёту по реабилитации при депрессии"
mode = detect_mode(user_message)
mode_modifier = MODE_MODIFIERS[mode]

# Сформируйте запрос
messages = [
    {"role": "system", "content": system_prompt + "\n\n" + mode_modifier},
    {"role": "user", "content": user_message}
]

# Отправьте в API
response = api.chat(messages=messages)
```

## Шаг 2: Интеграция с ВКонтакте

```python
from vkbottle import Bot
from detect_mode import detect_mode, MODE_MODIFIERS

bot = Bot(token="YOUR_VK_TOKEN")

@bot.on.message()
async def handler(message):
    user_text = message.text
    mode = detect_mode(user_text)
    
    # Формируем промпт с модификатором
    full_prompt = system_prompt + "\n\n" + MODE_MODIFIERS[mode]
    
    # Отправляем в GigaChat
    response = await get_ai_response(full_prompt, user_text)
    
    await message.answer(response)

bot.run_forever()
```

## Шаг 3: Интеграция с Telegram

```python
from aiogram import Bot, Dispatcher, types
from detect_mode import detect_mode, MODE_MODIFIERS

bot = Bot(token="YOUR_TG_TOKEN")
dp = Dispatcher(bot)

@dp.message_handler()
async def handler(message: types.Message):
    user_text = message.text
    mode = detect_mode(user_text)
    
    full_prompt = system_prompt + "\n\n" + MODE_MODIFIERS[mode]
    response = await get_ai_response(full_prompt, user_text)
    
    await message.answer(response)
```

## Что изменилось

✅ Роль для студентов-медиков и клинических психологов  
✅ Классификации: МКБ-10, МКБ-11, DSM-5  
✅ 4 режима: Обычный, Лекция, Консультация, Кризис  
✅ Этические ограничения и обработка кризисов  
✅ Обязательный дисклеймер  
✅ Few-shot примеры

## Дополнительно

Для тестирования режимов:

```bash
python -m docs.detect_mode
```

Это покажет примеры определения режимов для разных типов запросов.
