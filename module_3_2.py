def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    user = sender
    user1 = recipient
    for i in recipient or sender:
        if i != '@' :
            continue
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        elif '.com' != user1[len(recipient) - 4:] and '.ru' != user1[len(recipient) - 3:] and '.net' != user1[
                                                                                                 len(recipient) - 4:]:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        elif '.com' != user[len(sender) - 4:] and '.ru' != user[len(sender) - 3:] and '.net' != user[len(sender) - 4:]:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == 'university.help@gmail.com':
            print( f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
