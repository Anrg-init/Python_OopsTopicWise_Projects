class NotificationBase:
    def send(self):
        print("Base notification sent")


class MessageLogger(NotificationBase):
    def send(self):
        super().send()
        print("Message logged")


class EmailService(MessageLogger):
    def send(self):
        super().send()
        print("Email sent")


class SMSService(MessageLogger):
    def send(self):
        super().send()
        print("SMS sent")


class AppNotification(EmailService, SMSService):
    def send(self):
        super().send()
        print("App notification sent")


app = AppNotification()
app.send()

print(AppNotification.mro())
