# pip install python-telegram-bot markdown beautifulsoup4
# pip install python-telegram-bot==13.7

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import markdown
from bs4 import BeautifulSoup

TOKEN = input('YOUR_TELEGRAM_BOT_TOKEN:')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Markdown to Telegram bot!")

def convert_to_telegram_markdown(text):
    # Convert Markdown to HTML
    html = markdown.markdown(text)

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Convert <a> tags to Telegram Markdown hyperlinks
    for a_tag in soup.find_all('a'):
        url = a_tag.get('href')
        text = a_tag.get_text()
        markdown_link = f"[{text}]({url})"
        a_tag.replace_with(markdown_link)

    # Remove unnecessary HTML tags
    for tag in soup.find_all(['p']):
        tag.unwrap()

    # Get the modified HTML
    modified_html = str(soup)

    # Replace HTML tags with Telegram Markdown equivalents
    telegram_md = modified_html.replace('<strong>', '*').replace('</strong>', '*') \
                               .replace('<em>', '_').replace('</em>', '_') \
                               .replace('<code>', '`').replace('</code>', '`') \
                               .replace('<pre>', '`').replace('</pre>', '`')

    # Replace "&amp;" with "&"
    telegram_md = telegram_md.replace('&amp;', '&')

    return telegram_md

def handle_message(update, context):
    message = update.message.text
    converted_message = convert_to_telegram_markdown(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=converted_message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()