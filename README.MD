#### What are flask blueprints?
Basically, a flask blueprint is a way for you to organize your flask application into smaller and re-usable application

Just like a normal flask application, a blueprint defines a collection of views, templates and static assets.

It should be noted that a blueprint is not a ‘plug and play’ app, it cannot run on it’s own every blueprint must be registered on a real Flask application before it can be used.

#### Why should you use blueprints
* The main reason why you should use blueprints is to de-couple your application into smaller re-usable components.
* This makes the code more maintainable and easier to debug.