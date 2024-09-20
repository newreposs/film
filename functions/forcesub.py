from pyrogram.enums import ChatType

async def handle_force_subscribe(client, message):
    user_id = message.from_user.id
    start_time = datetime.now()
    await add_user_to_database(client, message)

    try:
        # Kullanıcının kanalda olup olmadığını kontrol et
        user = await client.get_chat_member(Config.AUTH_CHANNEL, user_id)
        
        # Eğer kullanıcı banlıysa mesajı sil
        if user.status == ChatMemberStatus.BANNED:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message.id,
                revoke=True
            )
            return 400
    except UserNotParticipant:
        pass
        date = start_time + timedelta(seconds=120)
        
        try:
            # Davet linki oluştur
            invite_link = await client.create_chat_invite_link(chat_id=Config.AUTH_CHANNEL, creates_join_request=True)
        except ChatAdminRequired:
            LOGGER.error("Bot'un Forcesub kanalında yönetici olduğundan emin olun.")
            return

        btn = [
            [
                InlineKeyboardButton(
                    Translation.BUTTON_TEXT, url=invite_link.invite_link
                )
            ]
        ]
        
        # Mesajın gruptan mı yoksa DM'den mi geldiğini kontrol et
        if message.chat.type == ChatType.PRIVATE:
            # Eğer DM'den geldiyse özel mesaj olarak davet linki gönder
            await client.send_message(
                chat_id=user_id,
                text=f"Sana Yardımcı Olabilmem İçin Kanalıma Katılman Gerekir Lütfen Katıldıktan Sonra Dizinin/Filmin İsmini Tekrar Gönder.\n\n{invite_link.invite_link}",
                reply_markup=InlineKeyboardMarkup(btn),
                reply_to_message_id=message.id,
            )
        else:
            # Eğer gruptan mesaj geldiyse grupta cevap ver
            await client.send_message(
                chat_id=message.chat.id,
                text=f"Merhaba @{message.from_user.username}, Yardımcı Olabilmem İçin Kanalıma Katılman Gerekir. Lütfen Katıldıktan Sonra Dizinin/Filmin İsmini Tekrar Gönder.\n\n{invite_link.invite_link}",
                reply_markup=InlineKeyboardMarkup(btn),
                reply_to_message_id=message.id,
            )
        
        return 400
    
    except FloodWait as e:
        # FloodWait hatası alırsan, bekle ve sonra devam et
        await asyncio.sleep(e.value)
        return 400
    
    except Exception as e:
        # Diğer hatalar için hata mesajı gönder
        await client.send_message(
            chat_id=user_id,
            text="Bir şeyler ters gitti.",
            disable_web_page_preview=True,
            reply_to_message_id=message.id,
        )
        LOGGER.info(e)
        return 400
