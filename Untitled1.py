{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-f5840cd08213>, line 25)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-f5840cd08213>\"\u001b[1;36m, line \u001b[1;32m25\u001b[0m\n\u001b[1;33m    server.run(host=:0.0.0.0\")\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import telebot\n",
    "from flask import Flask\n",
    "\n",
    "bot = telebot.TeleBot(\"889693565:AAGgfAlXBUIDs9G--0Pw8ufGkbPX4Q6Y_Ek\")\n",
    "TOKEN = \"889693565:AAGgfAlXBUIDs9G--0Pw8ufGkbPX4Q6Y_Ek\"\n",
    "server = Flask(__name__)\n",
    "\n",
    "@bot.message_handler(commands=['start'])\n",
    "def start_message(message):\n",
    "  bot.send_message(message.chat.id, \"Hello\")\n",
    "\n",
    "@bot.message_handler(content_types=['text'])\n",
    "def send_echo(message):\n",
    "\tbot.send_message(message.chat.id, message.text)\n",
    "\n",
    "bot.polling()\n",
    "\n",
    "\n",
    "#@server.route(\"/\")\n",
    "#def webhook():\n",
    "#   bot.remove_webhook()\n",
    " #   bot.set_webhook()\n",
    "  #  return \"!\", 200\n",
    "\n",
    "#if __name__ == \"__main__\":\n",
    " #   server.run(host=\"\", port=int(os.environ.get('PORT', 5000)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\programdata\\anaconda3\\lib\\site-packages (1.1.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (2.10.3)\n",
      "Requirement already satisfied: click>=5.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (7.0)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (1.1.0)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (0.16.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->flask) (1.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install flask\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
