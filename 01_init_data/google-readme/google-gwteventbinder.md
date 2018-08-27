## What is EventBinder?


GWT's EventBus is great - it allows you to write maintainable GWT applications
by decoupling the components of your application, making them easy to add,
modify, or remove. However, using EventBus in GWT can require a lot of 
boilerplate in the form of implementing events, defining handler interfaces for
them, and implementing those interfaces all over your code in anonymous classes.
EventBinder automates away these boring details using a strategy similar to the
`@UiHandler` annotation defined by UiBinder.

## How do I use it?

Easy - just define your event, register handler methods for it, and then fire 
it.

### Defining events

With EventBinder, events are just immutable value types extending 
`GenericEvent`. If your event doesn't have any arguments, defining it
only takes one line:

```java
public class SaveClickedEvent extends GenericEvent {}
```

To create an event with arguments, just create a normal Java value type:

```java
public class EmailLoadedEvent extends GenericEvent {
  private final String subject;
  private final String body;

  public EmailLoadedEvent(String subject, String body) {
    this.subject = subject;
    this.body = body;
  }

  public String getSubject() { return subject; }
  public String getBody() { return body; }
}
```

That's it - no need to implement `getAssociatedType` or `dispatch` from
`GwtEvent` or to define handler interfaces.

### Registering event handlers

Event handlers are methods annotated with the `@EventHandler` annotation. It
works the same way as `@UiHandler` - the name of the method is ignored, and
the argument to the method is checked to determine what type of event to
handle. In order to get this to work, you must also define an `EventBinder` 
interface and invoke `bindEventHandlers` on it in the same way you would for a 
`UiBinder`. Here's an example:

```java
class EmailPresenter {
  interface MyEventBinder extends EventBinder<EmailPresenter> {}
  private final MyEventBinder eventBinder = GWT.create(MyEventBinder.class);

  EmailPresenter(EventBus eventBus) {
    eventBinder.bindEventHandlers(this, eventBus);
  }

  @EventHandler
  void onEmailLoaded(EmailLoadedEvent event) {
    view.setSubject(email.getSubject());
    view.setBody(email.getBody());
  }
}
```

After `bindEventHandlers` is called, `onEmailLoaded` will be invoked whenever an
`EmailLoadedEvent` is fired on the given event bus.

It's possible to handle several events in one method. In this case you must
enumerate these event classes in `handles` property of `@EventHandler` annotation
and event parameter must be a superclass for all of these events. Also if
`handles` is specified and you don't need event parameter you may omit it.

```java
class SuperEvent extends GenericEvent { }

class EventOne extends SuperEvent { }

class EventTwo extends SuperEvent { }

class FormPresenter {
  interface MyEventBinder extends EventBinder<FormPresenter> {}
  private final MyEventBinder eventBinder = GWT.create(MyEventBinder.class);

  FormPresenter(EventBus eventBus) {
    eventBinder.bindEventHandlers(this, eventBus);
  }

  @EventHandler
  void onEventOne(EventOne event) {
    // handler for EventOne
  }

  @EventHandler(handles = {EventOne.class, EventTwo.class})
  void onEventOneAndTwo(SuperEvent event) {
    // handler for EventOne and EventTwo
  }

  @EventHandler(handles = {EventOne.class, EventTwo.class})
  void onEventOneAndTwo2() {
    // handler for EventOne and EventTwo without parameter
  }
}
```

### Firing events

The last step is easy and doesn't require anything special from EventBinder -
just construct an event and fire it on the event bus:

```java
eventBus.fireEvent(new EmailLoadedEvent("Hello world!", "How are you?"));
```

Firing this event will cause all `@EventHandler`s for `EmailLoadedEvent` in the
application to be invoked in an undefined order. That's it, you're done!

## How do I install it?

If you're using Maven, you can add the following to your `<dependencies>`
section:

```xml
    <dependency>
      <groupId>com.google.gwt.eventbinder</groupId>
      <artifactId>eventbinder</artifactId>
      <version>1.1.0</version>
    </dependency>
```

You can also download the [jar][1] directly or check out the source using git
from <https://github.com/google/eventbinder.git> and build it yourself. Once
you've installed EventBinder, be sure to inherit the module in your .gwt.xml
file like this:

```xml
    <inherits name='com.google.web.bindery.event.EventBinder'/>
```

## Where can I learn more?

 * For more details on the EventBinder API, consult the [Javadoc][2].
 * Check out the [sample app][3] for a full example of using EventBinder.
 * For general advice on architecting GWT applications, see [this video][4]
   and [this document][5]

## Version history

### 1.1.0
 * Ability to handle multiple events with a single handler mehtod (thanks to @ymakhno)

### 1.0.2
 * Compatibility with GWT 2.6 (thanks to @tbroyer).

### 1.0.1
 * Preliminary compatibility with GWT 2.6.
 * EventBinder now searches for `@EventHandler` annotation in superclasses as well as the current class.

### 1.0.0
 * Initial release.

[0]: https://github.com/google/gwteventbinder/issues/1
[1]: http://search.maven.org/remotecontent?filepath=com/google/gwt/eventbinder/eventbinder/1.1.0/eventbinder-1.1.0.jar
[2]: http://google.github.io/gwteventbinder/javadoc/
[3]: https://github.com/google/gwteventbinder/tree/master/eventbinder-sample/src/main/java/sample/client
[4]: http://www.youtube.com/watch?v=PDuhR18-EdM
[5]: https://developers.google.com/web-toolkit/articles/mvp-architecture
