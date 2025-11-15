from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# 1. إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 2. تعريف دالة الرد على أي رسالة (الأوامر والرسائل العادية)
async def maintenance_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يرسل رسالة 'البوت في حالة صيانة' رداً على أي رسالة أو أمر."""
    
    # النص الذي سيتم إرساله للمستخدم
    maintenance_message = "⚠️ **البوت في حالة صيانة** ⚠️\n\nنعتذر، البوت غير متاح حاليًا. يرجى المحاولة لاحقًا."
    
    # استخدام update.message.reply_text لإرسال الرد
    await update.message.reply_text(maintenance_message, parse_mode='Markdown')

# 3. دالة بدء تشغيل البوت
def main() -> None:
    """وظيفة التشغيل الرئيسية للبوت."""
    
    # استبدل 'YOUR_BOT_TOKEN' بتوكن البوت الخاص بك
    TOKEN = '7234870486:AAEJWkxBz75kvCGKR4BgD-m88MvPiY4LCZg'
    
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # 3.1. إضافة معالج لأمر /start
    # هذا يضمن الرد على /start بنفس رسالة الصيانة
    application.add_handler(CommandHandler("start", maintenance_reply))
    
    # 3.2. إضافة معالج للرسائل النصية العادية (تستثني الأوامر الأخرى لنتحكم بها بشكل منفصل)
    # filters.TEXT: الرسائل النصية
    # ~filters.COMMAND: استثناء أي أمر بخلاف /start (مثل /help، إلخ)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, maintenance_reply))
    
    # 3.3. إضافة معالج لأي أمر آخر غير /start
    # هذا يضمن أن أي أمر آخر يرسله المستخدم يرد برسالة الصيانة
    application.add_handler(MessageHandler(filters.COMMAND & ~filters.Regex(r'^/start'), maintenance_reply))
    
    # 3.4. بدء التشغيل
    print("البوت يعمل الآن...")
    application.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()
