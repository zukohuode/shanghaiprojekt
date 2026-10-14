#referalsysbot
import asyncio
from aiogram import Bot,  Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, CommandObject
from aiogram.utils.deep_linking import create_start_link

bot = Bot(token="YOUR_BOT_TOKEN"
          )
dp = Dispatcher() 

@dp.message(CommandStart())
async def start(message: types.Message, command: CommandObject):
    if command.args:
        # User started the bot with a referral link
        referrer_id = command.args
        await message.answer(f"Welcome! You were referred by user ID: {referrer_id}")
    else:
        # User started the bot without a referral link
        await message.answer("Welcome! Use a referral link to get started.")

    # Create a referral link for the user
    referral_link = await create_start_link(bot, payload=str(message.from_user.id))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Share your referral link", url=referral_link)]
    ])
    await message.answer("Share this link to invite others:", reply_markup=keyboard)

