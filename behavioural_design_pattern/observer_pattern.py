"""
The Observer Pattern (also known as Observable Pattern) is a behavioral design pattern where an object (the subject or observable) maintains a list of dependents (called observers) and automatically notifies them of any state changes, typically by calling one of their methods. It allows an object to send notifications to multiple other objects without knowing who or how many are listening.
Example: Notification System in Python

Let’s implement an Observable (which we will call NewsPublisher) that sends updates (news) to multiple Observers (subscribers). Whenever the NewsPublisher has new news, it will notify all registered observers.

Explanation:

    Observer (Interface):
        The Observer is an abstract class that defines an interface update(), which will be called by the Observable (in this case, NewsPublisher) to notify the observers (subscribers).

    Concrete Observer (Subscriber):
        Subscriber is a concrete implementation of the Observer. It has a name attribute to distinguish each subscriber and implements the update() method to handle the notification. In this case, it prints the received news.

    Observable (NewsPublisher):
        NewsPublisher maintains a list of subscribers. It has the following methods:
            subscribe(): Adds an observer to the list of subscribers.
            unsubscribe(): Removes an observer from the list.
            notify_subscribers(): Notifies all subscribed observers by calling their update() method.
            add_news(): Adds news and calls notify_subscribers() to broadcast the news to all subscribers.

    Client Code:
        We create two subscribers (Alice and Bob) and a NewsPublisher. Both subscribers are added to the list of subscribers.
        When news_publisher.add_news() is called, all current subscribers are notified of the news.
        After Bob unsubscribes, only Alice will receive future updates.
"""

from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete Observer: Subscriber
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received notification: {message}")

# Observable: NewsPublisher
class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.subscribers.remove(observer)

    def notify_subscribers(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)

    def add_news(self, news: str):
        print(f"NewsPublisher: New news added: {news}")
        self.notify_subscribers(news)

# Usage
subscriber1 = Subscriber("Alice")
subscriber2 = Subscriber("Bob")

news_publisher = NewsPublisher()

# Subscribing to the news publisher
news_publisher.subscribe(subscriber1)
news_publisher.subscribe(subscriber2)

# Adding news and notifying subscribers
news_publisher.add_news("Breaking News: Python 4.0 Released!")

# Unsubscribe one observer
news_publisher.unsubscribe(subscriber2)

# Adding more news
news_publisher.add_news("Update: Python 4.0 gets a new feature!")
