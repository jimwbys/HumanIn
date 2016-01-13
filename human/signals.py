from blinker import Namespace

signals = Namespace()

post_created = signals.signal("entry-created")
post_updated = signals.signal("entry-updated")
post_deleted = signals.signal("entry-deleted")