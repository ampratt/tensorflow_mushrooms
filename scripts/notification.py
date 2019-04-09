from win10toast import ToastNotifier
import time

def sendCompletedNotification(title, body):
    toaster = ToastNotifier()
    toaster.show_toast(title,
                   body)
                #    icon_path=None,
                #    duration=10000,
                #    threaded=False)
    # Wait for threaded notification to finish
    # while toaster.notification_active(): time.sleep(0.1)

sendCompletedNotification("SUCCESS", "Program finished running")

# import notify2

# def parseFeed():
#     notify2.init('notification')
#     n = notify2.Notification("Title", "Body")
#     n.set_urgency(notify2.URGENCY_NORMAL)
#     n.set_timeout(notify2.EXPIRES_NEVER)
#     n.show()

# parseFeed()