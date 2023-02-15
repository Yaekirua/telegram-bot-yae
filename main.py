import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


token = '5802074402:AAHZ8MM3bTSROwvuwvadFGOlUs1qCwhubTQ'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
  
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=0.9,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=["You:"]
)
  await message.answer(response['choices'][0]['text'])
 
executor.start_polling(dp, skip_updates=True)

