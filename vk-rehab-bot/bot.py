#!/usr/bin/env python3
"""
Бот для ВКонтакте - AI-ассистент по медицинской реабилитации
Использует GigaChat API для генерации ответов
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Добавляем путь к docs/ для импорта detect_mode
sys.path.append(str(Path(__file__).parent.parent / 'docs'))

from detect_mode import detect_mode, MODE_MODIFIERS

# Загружаем переменные окружения
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

if not VK_TOKEN or not GIGACHAT_API_KEY:
    raise ValueError("Не найдены VK_TOKEN или GIGACHAT_API_KEY в .env файле")

# Загрузка системного промпта
PROMPT_FILE = Path(__file__).parent / 'prompts.md'

with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
    SYSTEM_PROMPT = f.read()


class RehabBot:
    """Главный класс бота"""
    
    def __init__(self, vk_token: str, gigachat_api_key: str):
        self.vk_token = vk_token
        self.gigachat_api_key = gigachat_api_key
        self.system_prompt = SYSTEM_PROMPT
    
    def process_message(self, user_message: str) -> str:
        """
        Обработка сообщения пользователя
        
        Args:
            user_message: Текст сообщения от пользователя
            
        Returns:
            Ответ бота
        """
        # 1. Определяем режим работы
        mode = detect_mode(user_message)
        mode_modifier = MODE_MODIFIERS[mode]
        
        # 2. Формируем полный промпт
        full_prompt = f"{self.system_prompt}\n\n{mode_modifier}"
        
        # 3. Отправляем запрос в GigaChat (TODO: реализовать)
        response = self._call_gigachat(full_prompt, user_message)
        
        return response
    
    def _call_gigachat(self, system_prompt: str, user_message: str) -> str:
        """
        Вызов GigaChat API
        
        TODO: Реализовать интеграцию с GigaChat API
        См. docs/agent-update.md для примеров кода
        """
        # Пример структуры:
        # messages = [
        #     {"role": "system", "content": system_prompt},
        #     {"role": "user", "content": user_message}
        # ]
        # response = api.chat(messages=messages)
        # return response
        
        return "🔵 Бот в разработке. Добавьте интеграцию с GigaChat API."


def main():
    """Главная функция"""
    bot = RehabBot(VK_TOKEN, GIGACHAT_API_KEY)
    
    print("🚀 Бот запущен!")
    print(f"📝 Системный промпт загружен: {len(SYSTEM_PROMPT)} символов")
    print("💬 Тестирование режимов...\n")
    
    # Тестовые сообщения
    test_messages = [
        "Подготовь конспект по реабилитации при депрессии",
        "Есть пациент 45 лет с паническими атаками",
        "Не хочу жить, всё плохо",
        "Привет, как дела?"
    ]
    
    for msg in test_messages:
        mode = detect_mode(msg)
        print(f"📨 Сообщение: {msg}")
        print(f"🔍 Режим: {mode.value}")
        print(f"💬 Ответ: {bot.process_message(msg)}")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
