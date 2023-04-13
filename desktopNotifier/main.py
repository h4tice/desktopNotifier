from plyer import notification

notification_title="IMPORTANT!!"
notification_message="Don't forget to breathe :))"

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=5,            #waiting time on screen
    toast=False
)

