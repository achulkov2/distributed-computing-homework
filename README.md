# distributed-computing-homework

## Description 
First part of my homework for the Distributed Computing course.
Implements an API for a simple online-store.
Objects are stored in a PostgreSQL database.

## Objects

### Item
* **Description**: An object holding all item information. 
* **Fields**: 
  * **name**, string, up to 500 characters: The name of the item.
  * **code**, string, up to 500 characters: The code corresponding to the item.
  * **category**, string, up to 500 characters: The category corresponding to the item.
  * **id**, int: A unique id added implicitly by the backend upon item creation.

## API

### createItem
* **Description**: Adds an item to the store.
* **HTTP request**: POST
* **URL**: /api/items
* **Required body JSON parameters**: name, code, category
* **Return type**: JSON
* **Returns**: Created item.

### deleteItem
* **Description**: Deletes an item from the store.
* **HTTP request**: DELETE
* **URL**: /api/items/{id}
* **Return type**: JSON
* **Returns**: Deletion confirmation.

### updateItem
* **Description**: Update item info.
* **HTTP request**: PUT
* **URL**: /api/items/{id}
* **Accepted body JSON parameters**: name, code, category
* **Return type**: JSON
* **Returns**: Modified item.

### getItems
* **Description**: Get a list of all items sorted by id.
* **HTTP request**: GET
* **URL**: /api/items
* **Return type**: JSON
* **Returns**: List of requested items.

### getItemsPage
* **Description**: Ge a list of items with pagination. Splits the items sorted by id into pages of the provided size and returns the requested page. 
* **HTTP request**: GET
* **URL**: /api/items/list?{page}&{page_size}
* **Return type**: JSON
* **Returns**: List of requested items.

### getItem
* **Description**: Get item info for a single item.
* **HTTP request**: GET
* **URL**: /api/items/{id}
* **Return type**: JSON
* **Returns**: Requested item.

## Authentication API

### registerUser
* **Description**: Register a new user.
* **HTTP request**: POST
* **URL**: /auth/signup
* **Required body JSON parameters**: username, email, password
* **Return type**: JSON
* **Returns**: Created user. The password is hashed.

### getAuthTokens
* **Description**: Exchange credentials for a pair of tokens.
* **HTTP request**: POST
* **URL**: /auth/login
* **Required body JSON parameters**: username, password
* **Return type**: JSON
* **Returns**: A pair of access and refresh tokens with a lifetime of 5 minutes and 1 day accordingly.

### refreshAuthTokens
* **Description**: Request a new pair of token using the refresh token.
* **HTTP request**: POST
* **URL**: /auth/refresh
* **Required body JSON parameters**: refresh
* **Return type**: JSON
* **Returns**: A new pair of access and refresh tokens with a lifetime of 5 minutes and 1 day accordingly.

### validateToken
* **Description**: Request a new pair of token using the refresh token.
* **HTTP request**: POST
* **URL**: /auth/validate
* **Required body JSON parameters**: token
* **Return type**: JSON
* **Returns**: A response indicating whether the token is valid.

## Postman documentation

The postman documentation dump can be found [here](online-shop.postman_collection.json).
