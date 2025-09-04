# API Endpoint Tests

This document records the results of testing all API endpoints.

| Endpoint                      | Method  | Description               | Expected Result                | Actual Result | Status |
|------------------------------|---------|---------------------------|--------------------------------|--------------|--------|
| `/api/items/`                | GET     | List all items           | List of all items              | Works        | |
| `/api/items/1/`              | GET     | Retrieve item with ID 1  | Details of item with ID 1      | Works        | |
| `/api/items/`                | POST    | Create a new item        | Item created successfully      | Works        | |
| `/api/items/1/`              | PUT     | Update item with ID 1    | Item updated successfully      | Works        | |
| `/api/items/1/`              | DELETE  | Delete item with ID 1    | Item deleted successfully      | Works        | |
| `/api/items/?search=Test`    | GET     | Search items by name     | Items filtered by name         | Works        | |
| `/api/items/?category=Books` | GET     | Filter items by category | Items filtered by category     | Works        |  |
| `/api/items/?ordering=price` | GET     | Order items by price     | Items ordered by price         | Works        |  |

---

 **All endpoints tested successfully**
